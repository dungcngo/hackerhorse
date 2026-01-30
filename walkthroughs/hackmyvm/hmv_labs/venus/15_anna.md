# 0x15
This write-up explains the steps taken to complete mission 0x15, starting from user `anna` and escalating to `natalia`.

## Mission
As always, read the objective first:
```bash
anna@venus:~$ cat mission.txt 
################
# MISSION 0x15 #
################

## EN ##
Maybe sudo can help you to be natalia.
```

## Method of solving
You can login as `natalia` using `sudo` command and `-u` option with start a new shell.
```bash
anna@venus:~$ sudo -u natalia /bin/bash
GOGETA SSJ12 
```
Result: 
```bash
natalia@venus:/pwned/anna$ id ; whoami
uid=1016(natalia) gid=1016(natalia) groups=1016(natalia)
natalia
```
Get the flag in the home directory of `natalia`.

## Key command
`sudo -u natalia /bin/bash`

***You are welcome!***
	
