# 0x40
This write-up explains the steps taken to complete mission 0x40, starting from user `adela` and escalating to `sky`.

## Mission
As always, read the mission first:
```bash
adela@venus:~$ cat mission.txt 
################
# MISSION 0x40 #
################

## EN ##
User sky has saved her password to something that can be listened to.
```

## Method of solving
```bash
adela@venus:~$ ls -la
total 36
drwxr-x--- 2 root  adela 4096 Apr  5  2024 .
drwxr-xr-x 1 root  root  4096 Apr  5  2024 ..
-rw-r--r-- 1 adela adela  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 adela adela 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 adela adela  807 Apr 23  2023 .profile
-rw-r----- 1 root  adela   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root  adela  213 Apr  5  2024 mission.txt
-rw-r----- 1 root  adela   44 Apr  5  2024 wtf
```
In the home directory, the file `wtf` is identified as a simple ASCII text file.
```bash
adela@venus:~$ file wtf 
wtf: ASCII text
```
Upon viewing the file, it revealed a sequence of dots and dashes, which is the standard representation for **Morse Code**.
```bash
adela@venus:~$ cat wtf 
.--. .- .--. .- .--. .- .-. .- -.. .. ... .
```

Since the local system lacks Python or specialized decoding tools, you used **CyberChef** to decode the string. By applying the "From Morse Code" operation with a "Space" letter delimiter, the sequence is successfully translated.
- **Result**: PAPAPARADISE (password may be papaparadise)

With the password identified, we switch to user `sky` and get the flag.
```bash
adela@venus:~$ su - sky
Password: 
sky@venus:~$ id ; whoami
uid=1041(sky) gid=1041(sky) groups=1041(sky)
sky
sky@ven
```

## Key command
https://morsecode.world/international/translator.html


***You are welcome!***
