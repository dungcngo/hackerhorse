# 0x02
This write-up explains the steps taken to complete mission 0x02 on hades@hackmyvm.eu, starting from user `acantha` and escalating to `alala`.

## Mission
As always, we read the mission first:
```bash
acantha@hades:~$ cat mission.txt 
################
# MISSION 0x02 #
################

## EN ##
The user alala has left us a program, if we insert the 6 correct numbers, she gives us her password!
```
The mission for this stage involved interacting with a custom program to retrieve a password.

## Method of solving
In the home directory, we found an executable binary named `guess`:
```bash
acantha@hades:~$ ls -la
total 48
drwxr-x--- 2 root    acantha  4096 Apr  5  2024 .
drwxr-xr-x 1 root    root     4096 Apr  5  2024 ..
-rw-r--r-- 1 acantha acantha   220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 acantha acantha  3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 acantha acantha   807 Apr 23  2023 .profile
-rw-r----- 1 root    acantha    22 Apr  5  2024 flagz.txt
-rw-r-x--- 1 root    acantha 16064 Apr  5  2024 guess
-rw-r----- 1 root    acantha   275 Apr  5  2024 mission.txt
```

The program requires a 6-digit PIN code to reveal the password. Instead of attempting to burte-force the numbers, we ananlyzed the binary's content using the `strings` command to see if any sensitive information was embedded in the compiled code.
```bash
acantha@hades:~$ strings guess 
/lib64/ld-linux-x86-64.so.2
...
Enter PIN code:
DsYzpJQrCEndEWIMxWxu              <------ This is retrieved password.
NO :_(
...
```
**Explanation**:
- **Static Analysis**: Using `strings` is a form of basic static analysis. It extracts sequence of printable characters from binary files. In many beginner CTF challenges, "secrets" of "passwords" that the program is supposed to print are stored as plain text within the binary's `.rodata` (read-only data) section.
- **Hardcoded Credentials**: The strings stood out as it was positioned right between the "Enter PIN code" prompt and the failure message. This is a clear indicator of a hardcoded string that the program likely prints upon a successful "guess".
- **The Findings**: The string identified in the binary was the actual password for the user `alala`.

Using the identified password, we successfully logged in as user `alala` by SSH and get the flag.
```bash
acantha@hades:~$ ssh alala@localhost
...
alala@hades:~$ id ; whoami
uid=2044(alala) gid=2044(alala) groups=2044(alala)
alala
```

## Key command
`string ./guess`

***You are welcome!***
