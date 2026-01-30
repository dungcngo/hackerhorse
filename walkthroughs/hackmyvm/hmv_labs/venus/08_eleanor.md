# 0x08
This write-up explains the steps taken to complete mission 0x07, starting from user `eleanor` and escalating to `victoria`.

## Mission
As always, read the objective first:
```bash
eleanor@venus:~$ cat mission.txt 
################
# MISSION 0x08 #
################

## EN ##
The user victoria has left her password in a file in which the owner is the user violin. 
```

## Method of solving
From the desription victoria's password is in a file owned by violin.
Locate that file using `find` command:
```bash
eleanor@venus:~$ find / -type f -user violin 2>/dev/null
/usr/local/games/yo
```
Basically, we are specified the thing we searching for like it's type a file (`-type f`) and it's owner (`-user violin`) from root (`/`) directory as well as suppressing all error output messages (`2>/dev/null`).
Read that file:
```bash
eleanor@venus:~$ cat /usr/local/games/yo
pz8OqvJBFxH0cSj
```
Verify it by switching to `victoria` user:
```bash
eleanor@venus:~$ su - victoria
Password: 
victoria@venus:~$ id ; whoami
uid=1009(victoria) gid=1009(victoria) groups=1009(victoria)
victoria
```
Successfully logged in as `victoria`, get the flag.

## Key command
`find / -type f -user violin 2>/dev/null`


***You are welcome!***
