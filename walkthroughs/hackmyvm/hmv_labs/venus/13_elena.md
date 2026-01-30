# 0x13
This write-up explains the steps taken to complete mission 0x13, starting from user `elena` and escalating to `alice`.

## Mission
As always, read the objective:
```bash
elena@venus:~$ cat mission.txt 
################
# MISSION 0x13 #
################

## EN ##
The user alice has her password is in an environment variable. 
```

## Method of solving
You can look the current environment variables of this session using `env` or `printenv` command:
```bash
elena@venus:~$ env
SHELL=/bin/bash
PWD=/pwned/elena
LOGNAME=elena
HOME=/pwned/elena
-----------------
TERM=xterm-256color
USER=elena
PASS=Cgecy2MY2MWbaqt
SHLVL=1
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
MAIL=/var/mail/elena
_=/usr/bin/env
```
There is variable `PASS` that stored the password for user `alice`.
Verify it and go get the flag:
```bash
elena@venus:~$ su - alice
Password: 
 GOGETA SSJ10 FULL 
tornillo copia a GOGETA
alice@venus:~$ id ; whoami
uid=1014(alice) gid=1014(alice) groups=1014(alice)
alice
```

## Key command
`printenv` `env`

***You are welcome!***

