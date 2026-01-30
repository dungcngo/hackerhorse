# 0x14
This write-up explains the steps taken to complete mission 0x14, starting from user `alice` and escalating to `anna`.

## Mission
As usual, read the mission first:
```bash
alice@venus:~$ cat mission.txt 
################
# MISSION 0x14 #
################

## EN ##
The admin has left the password of the user anna as a comment in the file passwd. 
```

## Method of solving
Read the passwd file:
```bash
alice@venus:~$ cat /etc/passwd | grep "anna"
anna:x:1015:1015::/pwned/anna:/bin/bash
alice@venus:~$ cat /etc/passwd | grep "alice" 
alice:x:1014:1014:w8NvY27qkpdePox:/pwned/alice:/bin/bash
```
We can read the password with that command:
```bash
alice@venus:~$ cut -d: -f1,5 /etc/passwd | grep "alice"
alice:w8NvY27qkpdePox
```

## Key command
`cat /etc/passwd | grep "alice"`

`cut -d: -f1,5 /etc/passwd | grep "alice"`

***You are welcome!***
