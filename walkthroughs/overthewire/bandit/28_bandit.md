# Bandit28

## Level Description
There is a git repository at `ssh://bandit27-git@bandit.labs.overthewire.org/home/bandit27-git/repo` via the port 2220. The password for the user `bandit27-git` is the same as for the user `bandit27`.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs `git` installed locally on your machine.

## Method of Solving
We connect to the `bandit25` server using SSH. We use `mktemp` to create a temporary directory and move into it:
```bash
┌──(dungcngo㉿kali)-[~]
└─$ mktemp -d                         
/tmp/tmp.a3GJLC5eUQ
                                                                           
┌──(dungcngo㉿kali)-[~]
└─$ cd /tmp/tmp.a3GJLC5eUQ 
```
We use this command to access github repo:
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.a3GJLC5eUQ]
└─$ git clone ssh://bandit27-git@bandit.labs.overthewire.org:2220/home/bandit27-git/repo
Cloning into 'repo'...
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

backend: gibson-1
bandit27-git@bandit.labs.overthewire.org's password: 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
```
When the cloning finished, we navigated into new repo directory:
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.a3GJLC5eUQ]
└─$ ls                                
repo
                                                                           
┌──(dungcngo㉿kali)-[/tmp/tmp.a3GJLC5eUQ]
└─$ cd repo               
                                                                           
┌──(dungcngo㉿kali)-[/tmp/tmp.a3GJLC5eUQ/repo]
└─$ ls
README
                                                                           
┌──(dungcngo㉿kali)-[/tmp/tmp.a3GJLC5eUQ/repo]
└─$ cat README                        
The password to the next level is: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN
```

## Key command
`mktemp -d`

`git clone ssh://bandit27-git@bandit.labs.overthewire.org:2220/home/bandit27-git/repo`

***You are welcome!***
