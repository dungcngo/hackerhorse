# Bandit29

## Level Description
There is a git repository at `ssh://bandit28-git@bandit.labs.overthewire.org/home/bandit28-git/repo` via the port 2220. The password for the user `bandit28-git` is the same as for the user `bandit28`.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

## Method of Solving
We need to clone the repository like we did in the previous level:
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.a3GJLC5eUQ]
└─$ mktemp -d
/tmp/tmp.SzQz1G4Ti8
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.a3GJLC5eUQ]
└─$ cd /tmp/tmp.SzQz1G4Ti8
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.SzQz1G4Ti8]
└─$ git clone ssh://bandit28-git@bandit.labs.overthewire.org:2220/home/bandit28-git/repo
Cloning into 'repo'...
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

backend: gibson-1
bandit28-git@bandit.labs.overthewire.org's password: 
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.SzQz1G4Ti8]
└─$ ls
repo
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.SzQz1G4Ti8]
└─$ cd repo               
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.SzQz1G4Ti8/repo]
└─$ ls
README.md
```
From here, we take a look at the `README.md` file, and it looks like the password was redacted.
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.SzQz1G4Ti8/repo]
└─$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
```
To take a look at the history for the `README.md` file, we use this command:
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.SzQz1G4Ti8/repo]
└─$ git log -p
commit b5ed4b5a3499533c2611217c8780e8ead48609f6 (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 14 09:26:24 2025 +0000

    fix info leak

diff --git a/README.md b/README.md
index d4e3b74..5c6457b 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
+- password: xxxxxxxxxx
 

commit 8b7c651b37ce7a94633b7b7b7c980ded19a16e4f
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 14 09:26:24 2025 +0000
```
The retrieved password for `bandit29` is 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7.

## Key command
`git log -p`

***You are welcome!***
