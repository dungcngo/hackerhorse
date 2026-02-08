# Bandit04

## Level Description
The goal for this level was to find the password for the next level, hidden in a file within the `inhere` directory. The file was hidden, so we need to use commands that could reveal it.

## Method of Solving
After logging in as `bandit3`, we started by listing the contents of the home directory:
```bash
bandit3@bandit:~$ ls
inhere
```
This revealed a single directory named `inhere`. Based on the goal, we knew hidden file was somewhere inside this directory, so we decided to investigate further.

To reveal hidden files, we used the `-a` flag with the `ls` command:
```bash
bandit3@bandit:~/inhere$ ls -al
total 12
drwxr-xr-x 2 root    root    4096 Oct 14 09:26 .
drwxr-xr-x 3 root    root    4096 Oct 14 09:26 ..
-rw-r----- 1 bandit4 bandit3   33 Oct 14 09:26 ...Hiding-From-You
```
This command listed all files in the `inhere` directory with long listing format, including the hidden ones. There was a file named `...Hiding-From-You`

We read the contents of the file using `cat`:
```bash
bandit3@bandit:~/inhere$ cat ./...Hiding-From-You 
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
```
The password for the next level appeared!

## What we learned
- **Hidden Files**: Files that begin with a `.` are considered hidden in Linux. To list them you need the `-a` (all) or `-al` (all with details long listing format) flag with `ls`.
- **File Permissions**: Observing file permissions in `ls -al` output helped confirm the file could be read by my user.
- **Exploration Skills**: This challenge reinforced the importance of checking for hidden files and directories when solving CTF puzzles.

## Key command
`ls -al ./inhere`

`cat inhere/...Hiding-From-You`
