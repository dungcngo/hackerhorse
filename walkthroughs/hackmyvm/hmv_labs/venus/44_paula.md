# 0x44
This write-up explains the steps taken to complete mission 0x44, starting from user `paula` and escalating to `karla`.

## Mission
As always, we read the objective first:
```bash
paula@venus:~$ cat mission.txt 
################
# MISSION 0x44 #
################

## EN ##
The user karla trusts me, she is part of my group of friends. 
```

## Method of solving
We checked my current user identity and discovered that user `paula` is a member of a secondary group named `hidden`.
```bash
paula@venus:~$ id
uid=1044(paula) gid=1044(paula) groups=1044(paula),1053(hidden)
```
Since the mission hinted at a "group of friend", we searched the entire filesystem for files belonging to the `hidden` group that we might have permission to read.
```bash
paula@venus:~$ find / -group hidden 2>/dev/null
/usr/src/.karl-a
paula@venus:~$ cat /usr/src/.karl-a 
gYAmvWY3I7yDKRf
```
Using the retrieve password, we switch to user `karla` and get the flag.
```bash
paula@venus:~$ su - karla
Password: 
karla@venus:~$ id ; whoami
uid=1045(karla) gid=1045(karla) groups=1045(karla)
karla
```

## Key command 
`id `
`find / -group hidden 2>/dev/null`

***You are welcome!***
	
