# 0x01
This write-up walks through how mission 0x01 on venus@hackmyvm.eu was completed moving from the `hacker` user to `sophia`.

## Mission
First, SSH into the target machine using  the provided `hacker` credentials (see https://hackmyvm.eu/venus/index.php):
`ssh hacker@venus.hackmyvm.eu -p 5000`

Once inside, list all the content of home directory including the hidden:
```bash
hacker@venus:~$ ls -la
total 44
drwxr-x--- 1 root   hacker 4096 Apr  5  2024 .
drwxr-xr-x 1 root   root   4096 Apr  5  2024 ..
-rw-r----- 1 root   hacker   31 Apr  5  2024 ...
-rw-r--r-- 1 hacker hacker  283 Jan 18 20:17 .bash_logout
-rw-r--r-- 1 hacker hacker 3736 Jan 27 01:57 .bashrc
-rw-r----- 1 root   hacker   16 Apr  5  2024 .myhiddenpazz
-rwxr-xr-x 1 hacker hacker  807 Apr 23  2023 .profile
-rw-r----- 1 root   hacker  287 Apr  5  2024 mission.txt
-rw-r----- 1 root   hacker 2542 Apr  5  2024 readme.txt
```
Read `mission.txt` file to understand our objectives.
```bash
hacker@venus:~$ cat mission.txt 
################
# MISSION 0x01 #
################

## EN ##
User sophia has saved her password in a hidden file in this folder. Find it and log in as sophia.
```

## Method of solving
From the `ls -la` command the output shows a hiddent file named `.myhiddenpazz`, because whatever a file nor a directory named start with `.` is consider as hidden.
```bash
hacker@venus:~$ cat .myhiddenpazz 
Y1o645M3mR84ejc
```
Got the password for user `sophia`, with this password login as sophia and read the flag:
```bash
hacker@venus:~$ su - sophia
Password: 
Gh0st-2202 && Sh4dow_Err0r estuvieron aqui (10/12/2025)
Y a que no sabes.? PELU tambien jaj (2/01/2026) 
txfu tambien estuvo aqui :x (17/01/2026)
GOGETA lo iso igual xd (18.012026)���
sophia@venus:~$ id
uid=1002(sophia) gid=1002(sophia) groups=1002(sophia)
sophia@venus:~$ cat flagz.txt 
8===LUzzNuv8NB59iztWUIQS===D~~
```

## Key command
	`ls -la`
	
***You are welcome!***
