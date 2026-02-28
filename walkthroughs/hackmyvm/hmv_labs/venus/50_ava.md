# 0x50
This write-up explains the steps taken to complete mission 0x50, starting from user `ava` and escalating to `maria`.

## Mission
As always, read the objective first:
```bash
ava@venus:~$ cat mission.txt 
################
# MISSION 0x50 #
################

## EN ##
The password of maria is somewhere...
```

## Method of solving
We checked the local directory, but as expected, no obivous password files were found.
```bash
ava@venus:~$ ls -la
total 32
drwxr-x--- 2 root ava  4096 Apr  5  2024 .
drwxr-xr-x 1 root root 4096 Apr  5  2024 ..
-rw-r--r-- 1 ava  ava   220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 ava  ava  3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 ava  ava   807 Apr 23  2023 .profile
-rw-r----- 1 root ava    31 Apr  5  2024 flagz.txt
-rw-r----- 1 root ava   153 Apr  5  2024 mission.txt
```
The password was hidden within the profile data of a previously encountered user.
```bash
ava@venus:~$ su adela
Password: 
adela@venus:/pwned/ava$ cd ~
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
adela@venus:~$ cat wtf 
.--. .- .--. .- .--. .- .-. .- -.. .. ... .        <--- This is password of user maria
```
```bash
adela@venus:~$ su maria
Password: 
maria@venus:/pwned/adela$ cd ~
maria@venus:~$ ls    
flagz.txt  mission.txt
maria@venus:~$ cat flagz.txt 
8===ZLNu1CHYSYf0PvkK2iqS===D~~
maria@venus:~$ cat mission.txt 
################
# MISSION 0x51 #
################

## EN ##
Congrats!

## ES ##
Felicidades :)
```

## Key command
No thing


***You are welcome!***

