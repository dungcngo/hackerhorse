# 0x42
This write-up explains the steps taken to complete mission 0x42, starting from user `sarah` and escalating to `mercy`.

## Mission
As usual, we read the mission first:
```bash
sarah@venus:~$ cat mission.txt 
################
# MISSION 0x42 #
################

## EN ##
The password of mercy is hidden in this directory.
```

## Method of solving
We listed the files in the current directory and noticed an unusual entry that at first glance might look like a directory navigation shortcut (`.` or `..`, but was actually a file name `...`.
```bash
sarah@venus:~$ ls -la 
total 36
drwxr-x--- 2 root  sarah 4096 Apr  5  2024 .
drwxr-xr-x 1 root  root  4096 Apr  5  2024 ..
-rw-r----- 1 root  sarah   16 Apr  5  2024 ...
-rw-r--r-- 1 sarah sarah  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 sarah sarah 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 sarah sarah  807 Apr 23  2023 .profile
-rw-r----- 1 root  sarah   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root  sarah  175 Apr  5  2024 mission.txt
```
In Linux, any file starting with a dot(`.`) is hidden from a standard `ls` command. While we often see `.`(current directory) and `..` (parent directory), a file named `...` is common CTF trich to hide data in plain sight by mimicking those system pointers.
```bash
sarah@venus:~$ cat ./...
ym5yyXZ163uIS8L
```
Using the retrieved password, we switch to user `mercy` and get the flag.
```bash
sarah@venus:~$ su - mercy
Password: 
mercy@venus:~$ id ; whoami
uid=1043(mercy) gid=1043(mercy) groups=1043(mercy)
mercy
```

## Key command
`ls -la`
`cat ...`

***You are welcome!***
