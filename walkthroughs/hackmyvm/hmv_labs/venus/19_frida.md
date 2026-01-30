# 0x19
This write-up explains the steps taken to complete mission 0x19, starting from user `frida` and escalating to `eliza`.

## Mission
As usual, read the mission first:
```bash
frida@venus:~$ cat mission.txt 
################
# MISSION 0x19 #
################

## EN ##
The password of eliza is the only string that is repeated (unsorted) in repeated.txt. 
```

## Method of solving
We can solve this mission by using `uniq`:
```bash
frida@venus:~$ uniq -d repeated.txt 
Fg6b6aoksceQqB9
```
Verify it by switching user to `eliza` and get the flag.
```bash
frida@venus:~$ su - eliza
Password: 
eliza@venus:~$ id ; whoami
uid=1020(eliza) gid=1020(eliza) groups=1020(eliza)
eliza
```

## Key command
`uniq -d repeated.txt`

***You are welcome!***
