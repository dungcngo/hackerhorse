# Bandit19

## Level Description
The password for the next level is stored in a file `readme` in the homedirectory. Unfortunately, someone has modified `.bashrc` to log you out when you log in with `SSH`.

## Method of Solving
When we attempt to log into `bandit18` using SSH, we are immediately logged out. This behaviour is caused by a modification to the `.bashrc` file, which runs automatically upon login. To bypass this, we need to execute commands without triggering the `.bashrc` file.

Instead of logging into a shell, we use SSH to execute commands directly. This bypasses the `.bashrc` file and allows me to interact with the server.

We use SSH to read the contents of `readme` file:
```bash
┌──(root㉿kali)-[~]
└─# ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

backend: gibson-0
bandit18@bandit.labs.overthewire.org's password: 
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
```
The output reveals the password for `bandit19`.

## Key command

***You are welcome!***
