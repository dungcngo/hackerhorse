# 0x03
This write-up explains the steps taken to complete mission 0x03, starting from user `angela` and escalating to `emma`.

## Mission
As usual, read the objective:
```bash
angela@venus:~$ cat mission.txt 
################
# MISSION 0x03 #
################

## EN ##
The password of the user emma is in line 4069 of the file findme.txt
```

## Method of solving
In the home directory there is a file named `findme.txt` and the password for user `emma` is in line 4069. To find exactly line 4069 use `sed` command.
```bash
angela@venus:~$ sed -n "4069p" findme.txt 
fIvltaGaq0OUH8O
```
The `sed` command prints a specific line from a file. `-n` suppresses other output, and `"4069"` tells `sed` to print line 4069 only.
After retrieving the password, switch to `emma` user:
```bash
angela@venus:~$ su - emma
Password: 
GOGETA CALLOKEN ✨
emma@venus:~$ id ; whoami
uid=1004(emma) gid=1004(emma) groups=1004(emma)
emma
```
That comfirms the privelege escalation was successful. Print out the flag.

## Key command
`sed -n '4069p' findme.txt`

***You are welcome!***
