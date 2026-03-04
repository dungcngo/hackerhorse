# Bandit32

## Level Description
There is a git repository at `ssh://bandit31-git@bandit.labs.overthewire.org/home/bandit31-git/repo` via the port 2220. The password for the user `bandit31-git` is the same as for the user `bandit31`.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

## Method of Solving
We need to git clone this level's repo as well:
```bash
┌──(dungcngo㉿kali)-[/]
└─$ mktemp -d
/tmp/tmp.YyYNK709OJ
                                                                            
┌──(dungcngo㉿kali)-[/]
└─$ cd /tmp/tmp.YyYNK709OJ
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.YyYNK709OJ]
└─$ git clone ssh://bandit31-git@bandit.labs.overthewire.org:2220/home/bandit31-git/repo
Cloning into 'repo'...
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

backend: gibson-1
bandit31-git@bandit.labs.overthewire.org's password: 
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.YyYNK709OJ]
└─$ cd repo               
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.YyYNK709OJ/repo]
└─$ ls
README.md
                                                                            
```
In this `README.md` file in the Git repo we see this message:
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.YyYNK709OJ/repo]
└─$ cat README.md
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master
```
The `README.md` file has the contents described in the `objective` portion of this document, which means we need to commit and push a file to the repo to get the flag.
```bash
┌──(dungcngo㉿kali)-[/tmp/tmp.YyYNK709OJ/repo]
└─$ echo 'May I come in?' > key.txt
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.YyYNK709OJ/repo]
└─$ git add key.txt -f
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.YyYNK709OJ/repo]
└─$ git commit -m "Add key.txt file"                  
[master 30a6503] Add key.txt file
 1 file changed, 1 insertion(+)
 create mode 100644 key.txt
                                                                            
┌──(dungcngo㉿kali)-[/tmp/tmp.YyYNK709OJ/repo]
└─$ git push origin master          
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

backend: gibson-1
bandit31-git@bandit.labs.overthewire.org's password: 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 330 bytes | 330.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: ### Attempting to validate files... ####
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
remote: Well done! Here is the password for the next level:
remote: 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K 
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
To ssh://bandit.labs.overthewire.org:2220/home/bandit31-git/repo
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'ssh://bandit.labs.overthewire.org:2220/home/bandit31-git/repo'
```
The retrieved password for `bandit32` is `3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K`.

## Key command

***You are welcome!***
