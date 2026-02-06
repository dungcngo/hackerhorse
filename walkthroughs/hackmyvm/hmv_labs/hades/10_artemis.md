# 0x10
This write-up explains the steps taken to complete mission 0x10 on hades@hackmyvm.eu, starting from user `artemis` and escalating to `asia`.

## Mission
As always, we read the objective first:
```bash
artemis@hades:~$ cat mission.txt 
################
# MISSION 0x10 #
################

## EN ##
We need /bin/bash so that the user asia gives us her password. 
```
The mission clue for this stage suggested a specific requirement involving the system shell.

## Method of solving
In the home directory, we find an executable binary named `restricted`.
```bash
artemis@hades:~$ ls -la
total 48
drwxr-x--- 2 root    artemis  4096 Apr  5  2024 .
drwxr-xr-x 1 root    root     4096 Apr  5  2024 ..
-rw-r--r-- 1 artemis artemis   220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 artemis artemis  3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 artemis artemis   807 Apr 23  2023 .profile
-rw-r----- 1 root    artemis    22 Apr  5  2024 flagz.txt
-rw-r----- 1 root    artemis   202 Apr  5  2024 mission.txt
-rw---x--- 1 root    artemis 16056 Apr  5  2024 restricted
```

Based on the hint, the program likely checks the current shell environmnet before releasing the secret. Since the current environment was already using `/bin/bash`, simply executing the binary triggered the intended output.
```bash
artemis@hades:~$ ./restricted 
Your SHELL is: /bin/rbash

djqWtkLisbQlrGtLYHCv
```
**Explanation:**
- **Conditional Logic:** Programs in CTF challenges often contain checks for environment variables (like $SHELL, $USER, or $PATH). If the condition is met—in this case, having the shell set to /bin/bash—the program proceeds to print a hardcoded string or read a protected file.
- **Hardcoded Credentials:** The binary contained the cleartext password for the next user. As soon as the shell check passed, it displayed the credential to the terminal.
    
Using the retrieved password, we switch to user `asia` via SSH and get the flag.
```bash
artemis@hades:~$ ssh asia@localhost
...
asia@localhost's password: 
...
asia@hades:~$ id ; whoami
uid=2002(asia) gid=2002(asia) groups=2002(asia)
asia
```

## Key command
`./restricted`


***You are welcome!***
