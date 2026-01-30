# 0x17
This write-up explains the steps taken to complete mission 0x17, starting from user `eva` and escalating to `clara`.

## Mission
As always, read the objective first:
```bash
eva@venus:~$ cat mission.txt 
################
# MISSION 0x17 #
################

## EN ##
The password of the clara user is found in a file modified on May 1, 1968. 
```

## Method of solving
Solved this using:
```bash
eva@venus:~$ find / -type f -mtime +20440 2>/dev/null | xargs cat
39YziWp5gSvgQN9
```
We estimated the number of days between 1970 and the challenge year (in my case we used 2026:
```bash
2026 - 1970 = 56 years
56 * 365 = 20440 days (rough approximation, leap years ignored for simplicity)
```
And `xargs` take each filename from the input and passes it as an argument to `cat`.
Verify it and get the flag:
```bash
eva@venus:~$ su - clara
Password: 
clara@venus:~$ id ; whoami
uid=1018(clara) gid=1018(clara) groups=1018(clara)
clara
```

## Key command
`find / -type f -mtime +20075 2>/dev/null | xargs cat`


***You are welcome!***
