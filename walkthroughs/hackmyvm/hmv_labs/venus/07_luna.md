# 0x07
This write-up explains the steps taken to complete mission 0x07, starting from user `luna` and escalating to `eleanor`.

## Mission
As usual, read the objective first:
```bash
luna@venus:~$ cat mission.txt 
################
# MISSION 0x07 #
################

## EN ##
The user eleanor has left her password in a file that occupies 6969 bytes. 
```

## Method of solving
From the mission, the name of the file isn't specified explicitly but the size of the file is.
So, locate the file using `find` command:
```bash
luna@venus:~$ find / -type f -size 6969c 2>/dev/null
/usr/share/moon.txt
```
Searching from root directory and specified the size file as well as suppressing the standard error. Read that file:
```bash
luna@venus:~$ cat /usr/share/moon.txt 
UNDchvln6Bmtu7b
```
Switch to user `eleanor` to verify it:
```bash
luna@venus:~$ su - eleanor
Password: 
GOGETA SSJ3 
eleanor@venus:~$ id ; whoami
uid=1008(eleanor) gid=1008(eleanor) groups=1008(eleanor)
eleanor
```
Go get the flag.

## Key command 
`find / -type f -size 6969c 2>/dev/null`


***You are welcome!***
