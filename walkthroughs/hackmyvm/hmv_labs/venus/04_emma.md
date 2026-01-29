# 0x04
This write-up explains the steps taken to complete mission 0x04, starting from user `emma` and escalating to `mia`.

## Mission
In this mission our objective is:
```bash
emma@venus:~$ cat mission.txt 
################
# MISSION 0x04 #
################

## EN ##
User mia has left her password in the file -.
```

## Method of solving
Since the filename is unusual (it uses a symbol), read the file using `./[filename]`
```bash
emma@venus:~$ cat ./-
iKXIYg0pyEH2Hos
```
Switch to user `mia` to verify the password works:
```bash
emma@venus:~$ su - mia
Password: 
GOGETA GT 
mia@venus:~$ id ; whoami
uid=1005(mia) gid=1005(mia) groups=1005(mia)
mia
```
Successfully logged in as `mia`. Now, read the flag.

## Key command
`cat ./-`

***You are welcome!***
