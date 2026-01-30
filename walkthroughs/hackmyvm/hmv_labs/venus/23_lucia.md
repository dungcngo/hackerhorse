# 0x23
This write-up explains the steps taken to complete mission 0x23, starting from user `lucia` and escalating to `isabel`.

## Mission
As usual, we read the objective first:
```bash
lucia@venus:~$ cat mission.txt 
################
# MISSION 0x23 #
################

## EN ##
The user isabel has left her password in a file in the /etc/xdg folder but she does not remember the name, however she has dict.txt that can help her to remember.
```

## Method of solving
Checking the home directory, we find the dictionary file mentioned in the mission.
```bash
lucia@venus:~$ ls -la
total 36
drwxr-x--- 2 root  lucia 4096 Apr  5  2024 .
drwxr-xr-x 1 root  root  4096 Apr  5  2024 ..
-rw-r--r-- 1 lucia lucia  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 lucia lucia 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 lucia lucia  807 Apr 23  2023 .profile
-rw-r----- 1 root  lucia 1998 Apr  5  2024 dict.txt
-rw-r----- 1 root  lucia   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root  lucia  397 Apr  5  2024 mission.txt
```
Since we don't know which word in `dict.txt` matches the filename in `/etc/xdg`, we can use a bash loop to test every word. We pipe the errors (`2>/dev/null`) so only the file that actually exists.
```bash
lucia@venus:~$ for word in $(cat dict.txt); do ls /etc/xdg/$word 2>/dev/null; done
/etc/xdg/readme
```
The loop found a match: `/etc/xdg/readme`. Now, read that file to get the password.
```bash
lucia@venus:~$ cat /etc/xdg/readme
H5ol8Z2mrRsorC0
```
Verify it by switching user to `isabel` and get the flag.
```bash
lucia@venus:~$ su - isabel
Password: 
isabel@venus:~$ id ; whoami
uid=1024(isabel) gid=1024(isabel) groups=1024(isabel)
isabel
```

## Key command
`for word in $(cat dict.txt); do ls /etc/xdg/$word 2>/dev/null; done`
	
***You are welcome!***
