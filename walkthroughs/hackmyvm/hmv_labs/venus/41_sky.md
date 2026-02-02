# 0x41
This write-up explains the steps taken to complete mission 0x41, starting from user `sky` and escalating to `sarah`.

## Mission
As usual, we read the objective first:
```bash
sky@venus:~$ cat mission.txt 
################
# MISSION 0x41 #
################

## EN ##
User sarah uses header in http://localhost/key.php
```

## Method of solving
We examine the home directory, but since the hint specifically mention a URL and a "header", the objective is clearly to interact with the local web server using `curl`.
```bash
sky@venus:~$ ls -la
total 36
drwxr-x--- 2 root sky  4096 Apr  5  2024 .
drwxr-xr-x 1 root root 4096 Apr  5  2024 ..
-rw-r----- 1 root sky    31 Apr  5  2024 .bash_history
-rw-r--r-- 1 sky  sky   220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 sky  sky  3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 sky  sky   807 Apr 23  2023 .profile
-rw-r----- 1 root sky    31 Apr  5  2024 flagz.txt
-rw-r----- 1 root sky   184 Apr  5  2024 mission.txt
```

When accessing the URL normally, the server prompted for a specific condition: `Key header is true?`. This indicated that the PHP script was checking for a custom HTTP header. 
```bash
sky@venus:~$ curl -H "Key: abc" http://localhost/key.php

Key header is true?
```
After several attempts with different header names, we identified the correct key-value pair.
```bash
sky@venus:~$ curl -H "Key: true" http://localhost/key.php

LWOHeRgmIxg7fuS
```
Using the retrieved password, we switching to user `sarah` and get the flag.
```bash
sky@venus:~$ su - sarah
Password: 
sarah@venus:~$ id ; whoami
uid=1042(sarah) gid=1042(sarah) groups=1042(sarah)
sarah
```

##Key command
`curl -vv -i -H "Key: true" http://localhost/key.php`


***You are welcome!***
