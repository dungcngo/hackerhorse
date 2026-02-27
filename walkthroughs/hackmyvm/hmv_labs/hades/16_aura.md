# 0x16
This write-up explains the steps taken to complete mission 0x16 on hades@hackmyvm.eu, starting from user `aura` and escalating to `aegle`.

## Mission
As always, we read the mission first:
```bash
aura@hades:~$ cat mission.txt 
################
# MISSION 0x16 #
################

## EN ##
User aegle has a good memory for numbers.
```
The mission for this stage pointed to a memory challenge involving user `aegle`.
## Method of Solving
In the home directory, there was an executable named `numbers` that required specific input to proceed.
```bash
aura@hades:~$ ls -la
total 52
drwxr-x--- 2 root aura  4096 Apr  5  2024 .
drwxr-xr-x 1 root root  4096 Apr  5  2024 ..
-rw-r--r-- 1 aura aura   220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 aura aura  3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 aura aura   807 Apr 23  2023 .profile
-rw-r-x--- 1 root aura   160 Apr  5  2024 auri.sh
-rw-r----- 1 root aura    22 Apr  5  2024 flagz.txt
-rw-r----- 1 root aura   168 Apr  5  2024 mission.txt
-rw---x--- 1 root aura 16064 Apr  5  2024 numbers
```

## Key command

***You are welcome!***
