# 0x06
This write-up explains the steps taken to complete mission 0x06 on hades@hackmyvm.eu, starting from user `anthea` and escalating to `aphorodite`.

## Mission
As usual, we read the objective first:
```bash
anthea@hades:~$ cat mission.txt 
################
# MISSION 0x06 #
################

## EN ##
User aphrodite is obsessed with the number 94. 
```
The mission for this stage provided a very specific numerical clue.

## Method of Solving (Environment Variable Manipulation)
In the home directory, we find a binary named `obsessed` with **SUID** permissions, indicating it runs with elevated privileges.
```bash
anthea@hades:~$ ls -la
total 52
drwxr-x--- 2 root      anthea     4096 Apr  5  2024 .
drwxr-xr-x 1 root      root       4096 Apr  5  2024 ..
-rw-r--r-- 1 anthea    anthea      220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 anthea    anthea     3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 anthea    anthea      807 Apr 23  2023 .profile
-r--r----- 1 aphrodite aphrodite    21 Apr  5  2024 aphrodite_pass.txt
-rw-r----- 1 root      anthea       22 Apr  5  2024 flagz.txt
-rw-r----- 1 root      anthea      175 Apr  5  2024 mission.txt
-rwS--s--- 1 root      anthea    16256 Apr  5  2024 obsessed
```
When we first ran the program, it complained that a specific environment variable was missing: `No MYID ENV`. Based on the mission hint, we attempt to set this variable to `94`.

### Step 1: Initialize the Environment Variable
We use the `export` command to create an enviroment variable named `MYID` with the value `94`.
```bash
anthea@hades:~$ export MYID=94
```
After running this command, any program or process launched from that shell will be able to access this enviroment variable.

### Step 2: Observe Program Behavior
When rerunning the program, it showed that is was looking for a dynamic value. Each execution changed the required `MYID` value.

### Step 3: Automate the Matching
To solve this `obsessed`, we realized that the program was likely comparing the `MYID` environment variable against its internal logic or a character representation. By setting `MYID` to the `^` character (which corresponds to ASCII value 94), the program's logic was satisfied.
```bash
anthea@hades:~$ export MYID=^
anthea@hades:~$ ./obsessed 
Current MYID: 94
aphrodite@hades:~$ id
uid=2048(aphrodite) gid=2047(anthea) groups=2047(anthea)
aphrodite@hades:~$ ls  
aphrodite_pass.txt  flagz.txt  mission.txt  obsessed
aphrodite@hades:~$ cat aphrodite_pass.txt 
HPJVaqRzieKQeyyATsFv           <----- This is the retrieved password.
```
**Explanation**:
- **Environment Variables:** These are values used by the shell to pass information to programs. The obsessed binary was coded to check for a variable named MYID.
- **SUID Privilege Escalation:** Because the binary had the SUID bit set, once the "MYID" check passed, it spawned a shell with the privileges of the target user, aphrodite.
- **ASCII Obsession:** The number 94 is the decimal ASCII value for the caret symbol (^). By setting the environment variable to this character, the program's comparison logic (likely checking the byte value) succeeded.

With the identified password, we switch to user `aphrodite` by SSH and get the flag.
```bash
aphrodite@hades:~$ ssh aphrodite@localhost
...
aphrodite@localhost's password: 
...
aphrodite@hades:~$ id ; whoami
uid=2048(aphrodite) gid=2048(aphrodite) groups=2048(aphrodite)
aphrodite
```

## Key command
`export MYID=^`

***You are welcome!***
