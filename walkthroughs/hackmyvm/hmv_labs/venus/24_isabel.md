# 0x24
This write-up explains the steps taken to complete mission 0x24, starting from user `isabel` and escalating to `freya`.

## Mission
As usual, read the objective first:
```bash
isabel@venus:~$ cat mission.txt 
################
# MISSION 0x24 #
################

## EN ##
The password of the user freya is the only string that is not repeated in different.txt 
```
 
## Method of solving
Checking the home directory and found `different.txt`, a large file containing many strings.
```bash
isabel@venus:~$ ls -la
total 180
drwxr-x--- 2 root   isabel   4096 Apr  5  2024 .
drwxr-xr-x 1 root   root     4096 Apr  5  2024 ..
-rw-r--r-- 1 isabel isabel    220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 isabel isabel   3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 isabel isabel    807 Apr 23  2023 .profile
-rw-r----- 1 root   isabel 150544 Apr  5  2024 different.txt
-rw-r----- 1 root   isabel     31 Apr  5  2024 flagz.txt
-rw-r----- 1 root   isabel    245 Apr  5  2024 mission.txt
```
To find the unique string, we can use the `sort` command followed by `uniq -u`. This is necessary because `uniq` only detects duplicate lines that are adjacent to each other.
```bash
isabel@venus:~$ sort different.txt | uniq -u
EEDyYFDwYsmYawj
```
`sort different.txt`: sort the contents of the file in lexicographical oder.
`uniq -u`: filters and keeps only the lines that are not repeated.
Verify this password by switching user to `freya` and get the flag.
```bash
isabel@venus:~$ su - freya
Password: 
freya@venus:~$ id ; whoami
uid=1025(freya) gid=1025(freya) groups=1025(freya)
freya
```

## Key command
`sort different.txt | uniq -u`
	
***You are welcome!***
