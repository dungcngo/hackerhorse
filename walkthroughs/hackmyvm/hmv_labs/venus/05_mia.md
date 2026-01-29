# 0x05
This write-up explains the steps taken to complete mission 0x05, starting from user `mia` and escalating to `camila`.

## Mission
As usual, read the objective for this mission:
```bash
mia@venus:~$ cat mission.txt 
################
# MISSION 0x05 #
################

## EN ##
It seems that the user camila has left her password inside a folder called hereiam.
```

## Method of solving
Because we don't know where the `hereiam` folder is, we locate it using `find`:
```bash
mia@venus:~$ find / -type d -name "hereiam" 2>/dev/null
/opt/hereiam
```
The `find` command here searches from the root `/` for directories (`-type d`) named `hereiam` (`-name hereiam`), suppressing permission errors by redirecting stderr to `/dev/null`.
Move into that folder and read the password:
```bash
mia@venus:~$ cd /opt/hereiam/
mia@venus:/opt/hereiam$ ls -la
total 12
drwxr-xr-x 2 root root 4096 Apr  5  2024 .
drwxr-xr-x 1 root root 4096 Apr  5  2024 ..
-rw-r--r-- 1 root root   16 Apr  5  2024 .here
mia@venus:/opt/hereiam$ cat .here 
F67aDmCAAgOOaOc
```
Switch to user `camila` to verify the password works:
```bash
mia@venus:/opt/hereiam$ su - camila
Password: 
GOGETA SSJ4 
camila@venus:~$ id ; whoami
uid=1006(camila) gid=1006(camila) groups=1006(camila)
camila
```
Successfully logged in as `camila`. Now, read the flag.

## Key command
`find / -type d -name hereiam 2>/dev/null`

***You are welcome!***
