# 0x12
This write-up explains the steps taken to complete mission 0x10, starting from user `lucy` and escalating to `elena`.

## Mission
As usual, read the objective first:
```bash
lucy@venus:~$ cat mission.txt 
################
# MISSION 0x12 #
################

## EN ##
The password of the user elena is between the characters fu and ck 
```

## Method of solving
In the home directory there is the file `file.yo`. We need to find a line that start with `fu` and end with `ck` in that file.
We could use the grep command in order the get the line and the combination of regular expression of `^`, `$` and `.*`.
```bash
lucy@venus:~$ grep -ra "^fu.*ck$" file.yo 
fu4xZ5lIKYmfPLg9tck
```
Or we can use `sed`:
```bash
lucy@venus:~$ sed -n 's/.*fu\(.*\)ck.*/\1/p' file.yo
4xZ5lIKYmfPLg9t
```
Verify it and get the flag:
```bash
lucy@venus:~$ su - elena
Password: 
elena@venus:~$ id ; whoami
uid=1013(elena) gid=1013(elena) groups=1013(elena)
elena
```

## Key command
`sed -n 's/.*fu\(.*\)ck.*/\1/p' file.yo` 

`grep -ra "^fu.*ck$" file.yo`

***You are welcome!***

