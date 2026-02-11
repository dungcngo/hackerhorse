# Bandit14

## Level Description
The password for the next level is stored in `/etc/bandit_pass/bandit14` and can only be read by user `bandit14`. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Look at the commands that logged you into previous bandit levels, and find out how to use the key for this level.

## Method of Solving
As always, logging into the Bandit server as `bandit13`. Check what's available in the home directory:
```bash
bandit13@bandit:~$ ls -la
total 24
drwxr-xr-x   2 root     root     4096 Oct 14 09:26 .
drwxr-xr-x 150 root     root     4096 Oct 14 09:29 ..
-rw-r--r--   1 root     root      220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root     root     3851 Oct 14 09:19 .bashrc
-rw-r--r--   1 root     root      807 Mar 31  2024 .profile
-rw-r-----   1 bandit14 bandit13 1679 Oct 14 09:26 sshkey.private
```
The output reveals a file named `sshkey.private`.

Use the SSH key to log in as `bandit14`:
```bash
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost -p 2220
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit13/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit13/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

!!! You are trying to log into this SSH server with a password on port 2220 from localhost.
!!! Connecting from localhost is blocked to conserve resources.
!!! Please log out and log in again.

backend: gibson-0
Received disconnect from 127.0.0.1 port 2220:2: no authentication methods enabled
Disconnected from 127.0.0.1 port 2220
```
Because SSH requires the private key file to be readable and writable only by its owner, otherwise it will raise a security error when you use `ssh -i sshkey.private`. Since the `bandit13` server does not allow `chmod`.
```bash
bandit13@bandit:~$ chmod 600 sshkey.private 
chmod: changing permissions of 'sshkey.private': Operation not permitted
```
We will use `scp` to copy the `sshkey.private` file to the local machine.
```bash
┌──(root㉿kali)-[~]
└─# scp -P 2220 bandit13@bandit.labs.overthewire.org:/home/bandit13/sshkey.private .
...
backend: gibson-0
bandit13@bandit.labs.overthewire.org's password: 
sshkey.private                                100% 1679     4.0KB/s   00:00 
```
Use the `chmod` command to set the proper permissions for the private key when using SSH.
```bash
┌──(root㉿kali)-[~]
└─# chmod 600 sshkey.private    
```
Use the SSH key to log in as `bandit14`.
```bash
┌──(root㉿kali)-[~]
└─# ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220 
...

  Enjoy your stay!

bandit14@bandit:~$ 
```
Retrieve the password:
```bash
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```
The password for the next level appeared!

## What we learned
- **Using an SSH private key for authentication**: Instead of a password, private keys provide a secure way to log in.
- **How `cat` helps read protected files**: The `/etc/bandit_pass/` directory contains passwords, but access is only allowed to the correct user.
- **Why private keys should be kept secure**: Since the SSH key allowed authentication without a password, it highlights the importance of keeping private keys protected.

## Key command
`ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220`

`chmod 600 sshkey.private`

`cat /etc/bandit_pass/bandit14`

***You are welcome!***
