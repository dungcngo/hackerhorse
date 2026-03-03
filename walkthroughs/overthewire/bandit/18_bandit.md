# Bandit18

## Level Description
There are 2 files in the homedirectory: `passwords.old` and `passwords.new`. The password for the next level is in `passwords.new` and is the only line that has been changed between `passwords.old` and `passwords.new`.

## Method of Solving
Using the SSH private key from the previous level to log into user `bandit17`.
Once logged in, we check the contents of the home directory:
```bash
bandit17@bandit:~$ ls -la
total 36
drwxr-xr-x   3 root     root     4096 Oct 14 09:26 .
drwxr-xr-x 150 root     root     4096 Oct 14 09:29 ..
-rw-r-----   1 bandit17 bandit17   33 Oct 14 09:26 .bandit16.password
-rw-r--r--   1 root     root      220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root     root     3851 Oct 14 09:19 .bashrc
-rw-r-----   1 bandit18 bandit17 3300 Oct 14 09:26 passwords.new
-rw-r-----   1 bandit18 bandit17 3300 Oct 14 09:26 passwords.old
-rw-r--r--   1 root     root      807 Mar 31  2024 .profile
drwxr-xr-x   2 root     root     4096 Oct 14 09:26 .ssh
```
This reveal two files: `password.old` and `password.new`.

The goal is to find the password for `bandit18`, which is the only line that had changed between `password.old` and `password.new`. To do this, we need to compare the two file and identify the difference. 

We use to `diff` command to compare the two files:
```bash
bandit17@bandit:~$ diff passwords.old passwords.new 
42c42
< BMIOFKM7CRSLI97voLp3TD80NAq5exxk
---
> x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
```
This indicatd that line 42 in `password.old` was replaced with a new line `password.new`. The new line in `password.new` is the password for `bandit18`: `x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO`.

## Key command
`diff password.old password.new`

***You are welcome!***
