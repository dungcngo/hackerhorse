# Bandit23

## Level Description
A program is running automatically at regular intervals from `cron`, the time-based job scheduler. Look in `/etc/cron.d/` for the configuration and see what command is being executed.

## Method of Solving
We log into the `bandit22` server, we list the contents of the home directory:
```bash
bandit22@bandit:~$ ls -la
total 20
drwxr-xr-x   2 root root 4096 Oct 14 09:25 .
drwxr-xr-x 150 root root 4096 Oct 14 09:29 ..
-rw-r--r--   1 root root  220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root root 3851 Oct 14 09:19 .bashrc
-rw-r--r--   1 root root  807 Mar 31  2024 .profile
```
The level description whispered of `cron job` running automatically. We investigate the `/etc/cron.d/` directory, where cron configurations are stored. We navigated there:
```bash
bandit22@bandit:~$ cd /etc/cron.d/
bandit22@bandit:/etc/cron.d$ ls 
behemoth4_cleanup  cronjob_bandit23  leviathan5_cleanup    sysstat
clean_tmp          cronjob_bandit24  manpage3_resetpw_job
cronjob_bandit22   e2scrub_all       otw-tmp-dir
```
The file `cronjob_bandit23` is the key to unlocking the next level. We open the `cronjob_bandit23` file to see what it was up to:
```
bandit22@bandit:/etc/cron.d$ cat cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
```
We inspect the script `/usr/bin/cronjob_bandit23.sh` to understand its purpose:
```bash
bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```
Here's what it did:
- It determined the current user (`whoami`)
- It generated an MD5 hash of the string `"I am user <username>"` and stored it in the variable `mytarget`.
- It copied the password for the current user (`/etc/bandit_pass/$myname`) to file in `/file/` named after the MD5 hash.

Since the cron job runs as the `bandit23` user, we need to figure out what the MD5 hash would be for `bandit23`. We run the following command to generate the hash:
```bash
bandit22@bandit:/etc/cron.d$ echo "I am user bandit23" | md5sum | cut -d '' -f 1
8ca319486bfbbc3663ea0fbe81326349 
```
The password for `bandit23` was stored in `/tmp/8ca319486bfbbc3663ea0fbe81326349`.

We check the contents for the file:
```bash
bandit22@bandit:/etc/cron.d$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
```
There is the password for user `bandit23`.

## Key command
`echo "I am user bandit23" | md5sum | cut -d ' ' -f 1`

***You are welcome!***
