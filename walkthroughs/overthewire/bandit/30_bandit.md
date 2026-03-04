# Bandit30

## Level Description
There is a git repository at `ssh://bandit29-git@bandit.labs.overthewire.org/home/bandit29-git/repo` via the port 2220. The password for the user `bandit29-git` is the same as for the user `bandit29`.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

## Method of Solving
We need to git clone this repo as well, like all the rest:
```bash
┌──(dungcngo㉿kali)-[~]
└─$ mktemp -d    
/tmp/tmp.Xbk7dhH9CV
                                                                            
┌──(dungcngo㉿kali)-[~]
└─$ cd /tmp/tmp.Xbk7dhH9CV
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.Xbk7dhH9CV]
└─$ git clone ssh://bandit29-git@bandit.labs.overthewire.org:2220/home/bandit29-git/repo
Cloning into 'repo'...
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

backend: gibson-1
bandit29-git@bandit.labs.overthewire.org's password: 
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 16 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (16/16), 1.44 KiB | 98.00 KiB/s, done.
Resolving deltas: 100% (2/2), done.
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.Xbk7dhH9CV]
└─$ ls
repo
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.Xbk7dhH9CV]
└─$ cd repo                
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.Xbk7dhH9CV/repo]
└─$ ls
README.md

┌──(dungcngo㉿kali)-[/tmp/tmp.Xbk7dhH9CV/repo]
└─$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

```
To take a look at the history for the `README.md` file, we use this command:
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.Xbk7dhH9CV/repo]
└─$ git log -p
commit 8ff4dfab0a869265c3cd59719c5101098e2279ed (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 14 09:26:26 2025 +0000

    fix username

diff --git a/README.md b/README.md
index 2da2f39..1af21d3 100644
--- a/README.md
+++ b/README.md
@@ -3,6 +3,6 @@ Some notes for bandit30 of bandit.
 
 ## credentials
 
-- username: bandit29
+- username: bandit30
 - password: <no passwords in production!>
 

commit 09300a1ee84da9a017084bc0723c2e0de4a12584
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 14 09:26:26 2025 +0000
:
```
We look at the git logs for the master branch, and they indicate that the `README.md` file was redacted. We need to take a look at the different branches  for the repo:
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.Xbk7dhH9CV/repo]
└─$ git branch -a     
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
```
This output indicates there more than one branch that we can look at. We want to checkout the dev branch. We can switch branches in Git with the following command:
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.Xbk7dhH9CV/repo]
└─$ git checkout dev
branch 'dev' set up to track 'origin/dev'.
Switched to a new branch 'dev'
```
We can now take a look at the logs for this branch:
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.Xbk7dhH9CV/repo]
└─$ git log -p
commit e50e6cc6be6bc718f834b1584971b1039e4e87db (HEAD -> dev, origin/dev)
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 14 09:26:26 2025 +0000

    add data needed for development

diff --git a/README.md b/README.md
index 1af21d3..bc6ad3d 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for bandit30 of bandit.
 ## credentials
 
 - username: bandit30
-- password: <no passwords in production!>
+- password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL
 

commit a3b6378aa0d0088c60b8854d0d20f46aabd466bc
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 14 09:26:26 2025 +0000

    add gif2ascii
:
```

## Key command
`git branch -a`

`git checkout dev`

***You are welcome!***
