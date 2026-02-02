# 0x47
This write-up explains the steps taken to complete mission 0x47, starting from user `zora` and escalating to `belen`.

## Mission
We read the objective first:
```bash
zora@venus:~$ cat mission.txt 
################
# MISSION 0x47 #
################

## EN ##
The user belen has left her password in venus.hmv
```

## Method of solving
We checked the home directory and found a file named `zora_pass.txt`, but the the hint specifically directed me toward an external or internal web resource named `venus.hmv`.
```bash
zora@venus:~$ ls -la
total 36
drwxr-x--- 2 root zora 4096 Apr  5  2024 .
drwxr-xr-x 1 root root 4096 Apr  5  2024 ..
-rw-r--r-- 1 zora zora  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 zora zora 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 zora zora  807 Apr 23  2023 .profile
-rw-r----- 1 root zora   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root zora  173 Apr  5  2024 mission.txt
-rw-r----- 1 root zora   16 Apr  5  2024 zora_pass.txt
```
The address `venus.hmv` suggests a Virtual Host or a local domain defined in the system's `/etc/hosts` files. To retrieve the password, we used `curl` to make an HTTP request to that domain.
```bash
zora@venus:~$ curl venus.hmv
2jA0E8bQ4WrGwWZ
```
Using the retrieved password, we switch to user `belen` and get the flag.
```bash
zora@venus:~$ su - belen
Password: 
belen@venus:~$ id ; whoami
uid=1048(belen) gid=1048(belen) groups=1048(belen)
belen
```

## Key command
`curl -vv venus.hmv`

***You are welcome!***
