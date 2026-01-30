# 0x16
This write-up explains the steps taken to complete mission 0x16, starting from user `natalia` and escalating to `eva`.

## Mission
As usual, read the mission first:
```bash
natalia@venus:~$ cat mission.txt 
################
# MISSION 0x16 #
################

## EN ##
The password of user eva is encoded in the base64.txt file
```

## Method of solving
In the home directory there is a file that was mentioned about.
You can solve this by using `base64` command and using `-d` option as decode.
```bash
natalia@venus:~$ base64 -d base64.txt 
upsCA3UFu10fDAO
```
Verify it by switching user to `eva` and go get the flag:
```bash
natalia@venus:~$ su - eva 
Password: 
oGOGETA SSJ14 
T sige aqui
eva@venus:~$ id ; whoami
uid=1017(eva) gid=1017(eva) groups=1017(eva)
eva
```

## Key command
`base64 -d base64.txt`

***You are welcome!***
	
