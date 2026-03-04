# Bandit26

## Level Description
Logging in to `bandit26` from `bandit25` should be fairly easy… The shell for user `bandit26` is not `/bin/bash`, but something else. Find out what it is, how it works and how to break out of it.

## Method of Solving
We connect to the `bandit25` server using SSH. In the home directory, we find a ssh key with named `bandit26.sshkey`.
```bash
bandit25@bandit:~$ ls
bandit26.sshkey
```

Since we get the ssh key, we're going to use the `-i` option with the provided sshkey file.
```bash
bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost -p 2220
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit25/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit25/.ssh/known_hosts).
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

backend: gibson-1
Received disconnect from 127.0.0.1 port 2220:2: no authentication methods enabled
Disconnected from 127.0.0.1 port 2220
```
At first we think this going to be easy but it turns the server immediately closed after we connected. 

Because the `bandit26` user doesn't use a standard shell, we can lookup what shell they use with the following command:
```bash
bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
```
We can find out what kind of file we're dealing with:
```bash
bandit25@bandit:~$ file /usr/bin/showtext
/usr/bin/showtext: POSIX shell script, ASCII text executable
```
It's a shell script file. Let's inspect it:
```bash
bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

exec more ~/text.txt
exit 0
```
This script uses the `more` command to read a file. We could potentially break out of the `more` command if whatever we're reading is larger than what can fit on the screen. 

We're given an SSH key to login as `bandit26`, so we copy the key content to our desktop and create the key. Then we make the terminal text _really_ big and  use the following command to login.
```bash
ssh -i bandit26.key bandit26@bandit.labs.overthewire.org -p 2220
```

If we're in the middle of the `more` command, we can use the `v` key to switch into the VIM text editor. From there, we could use the `:shell` command to open an interactive shell, but the shell is set to the `showtext` file. We can set a new shell for the session like this:
```bash
:set shell=/bin/bash
```
Then open the shell:
```bash
:shell
```
From here we can read the password for `bandit26`:
```bash
:shell
<:~$ cat /etc/bandit_pass/bandit26
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
```

## Key command
`cat /etc/passwd | grep bandit26`

`:set shell=/bin/bash`

***You are welcome!***
