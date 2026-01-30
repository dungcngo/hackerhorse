# 0x11
This write-up explains the steps taken to complete mission 0x10, starting from user `violet` and escalating to `lucy`.

## Mission
As usual, read the mission first:
```bash
violet@venus:~$ cat mission.txt 
################
# MISSION 0x11 #
################

## EN ##
The password of the user lucy is in the line that ends with 0JuAZ (these last 5 characters are not part of her password) 
```

## Method of solving
From the mission the password is in line that ends with `0JuAZ` but these characters aren't include.
We can retrieve it using grep command and use regular expresssion with the dollar sign `$` anchor.
```bash
violet@venus:~$ grep "0JuAZ$" end
OCmMUjebG53giud0JuAZ
```
Or we can use `sed`:
```bash
violet@venus:~$ sed -n 's/0JuAZ$//p' end
OCmMUjebG53giud
```
After, verify it by switching user to `lucy`:
```bash
violet@venus:~$ su - lucy
Password: 
GOGETA SSJ8 
lucy@venus:~$ id ; whoami
uid=1012(lucy) gid=1012(lucy) groups=1012(lucy)
lucy
```
Go get the flag.

## Key command
`grep "0JuAZ$" end`

`sed -n 's/0JuAZ$//p' end`

***You are welcome!***
