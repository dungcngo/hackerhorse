# Bandit10

## Level Descrifption
The goal for this level was to find a password stored in a file named `data.txt` in one of the few human-readable strings, preceded by several '=' characters.

## Method of Solving
Upon logging in as `bandit9`, as usual we check what's the contents of the home directory with the:
```bash
bandit9@bandit:~$ ls -la
total 40
drwxr-xr-x   2 root     root     4096 Oct 14 09:25 .
drwxr-xr-x 150 root     root     4096 Oct 14 09:29 ..
-rw-r--r--   1 root     root      220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root     root     3851 Oct 14 09:19 .bashrc
-rw-r-----   1 bandit10 bandit9 19382 Oct 14 09:25 data.txt
-rw-r--r--   1 root     root      807 Mar 31  2024 .profile
```
It looks like there are files named `data.txt` here, so we want to know what kind of file type this is:
```bash
bandit9@bandit:~$ file data.txt 
data.txt: data
```
which returns a data type file. We just want to make sure how many lines are there on the file:
```bash
bandit9@bandit:~$ wc -l data.txt 
78 data.txt
```
Not so much only 78 lines, but we need to find some way to get the human-readable strings since there are some characters we can read. 

We are going to use the `strings` command and the `grep` command to get the specific `=` character. We type this command to retrieve the password:
```bash
bandit9@bandit:~$ strings data.txt |  grep ===
========== the
========== password
E========== is
5========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```
The password for the next level appeared!

## What we learned
- **Extracting Readable Strings with `strings`**: The `strings` command filters out human-readable text from binary or data files.
- **Finding Specific Patterns with `grep`**: Using `grep` allows searching for patterns, in this case, filtering lines that contain `=` to locate the password.
- **Combining Commands with Pipes (`|`)**: Piping strings into grep is an efficient way to refine output and extract relevant information.

## Key command
`strings data.txt | grep ===`

***You are welcome!***
