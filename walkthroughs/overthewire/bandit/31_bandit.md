# Bandit31

## Level Description
There is a git repository at `ssh://bandit30-git@bandit.labs.overthewire.org/home/bandit30-git/repo` via the port 2220. The password for the user `bandit30-git` is the same as for the user `bandit30`.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

## Method of Solving
We need to git clone this repo as well, like all the rest:
```bash
┌──(dungcngo㉿kali)-[/]
└─$ mktemp -d
/tmp/tmp.PwZDwiNVNL
                                                                            
┌──(dungcngo㉿kali)-[/]
└─$ cd /tmp/tmp.PwZDwiNVNL
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.PwZDwiNVNL]
└─$ git clone ssh://bandit30-git@bandit.labs.overthewire.org:2220/home/bandit30-git/repo
Cloning into 'repo'...
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

backend: gibson-1
bandit30-git@bandit.labs.overthewire.org's password: 
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.PwZDwiNVNL]
└─$ cd repo               
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.PwZDwiNVNL/repo]
└─$ ls
README.md
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.PwZDwiNVNL/repo]
└─$ cat README.md
just an epmty file... muahaha
```
There is nothing in git logs and nothing in the git branches:
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.PwZDwiNVNL/repo]
└─$ git log -p
commit d604df2303c973b8e0565c60e4c29d3801445299 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 14 09:26:28 2025 +0000

    initial commit of README.md

diff --git a/README.md b/README.md
new file mode 100644
index 0000000..029ba42
--- /dev/null
+++ b/README.md
@@ -0,0 +1 @@
+just an epmty file... muahaha
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.PwZDwiNVNL/repo]
└─$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
```
But there's a weird looking tag:
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.PwZDwiNVNL/repo]
└─$ git show-ref --tags
84368f3a7ee06ac993ed579e34b8bd144afad351 refs/tags/secret
```
We can look at the secret tag by using this command:
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.PwZDwiNVNL/repo]
└─$ git show secret     
fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy
```
This is the retrieved password of user `bandit31`.

## Key command
`git show-ref --tags`

`git show secret`

***You are welcome!***
