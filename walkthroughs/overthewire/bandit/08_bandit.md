# Bandit08

## Level Description
The goal of this level is to locate a password hidden inside a file named `data.txt`. The password is positioned next to the word `millionth`.

However, the challenge is that `data.txt` is a massive file with nearly 100,000 lines, making manual inspection impractical. This requires an efficient way to extract the required information.

## Method of Solving
When logging into as `bandit7`, we ran:
```bash
bandit7@bandit:~$ ls -la
total 4108
drwxr-xr-x   2 root    root       4096 Oct 14 09:26 .
drwxr-xr-x 150 root    root       4096 Oct 14 09:29 ..
-rw-r--r--   1 root    root        220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root    root       3851 Oct 14 09:19 .bashrc
-rw-r-----   1 bandit8 bandit7 4184396 Oct 14 09:26 data.txt
-rw-r--r--   1 root    root        807 Mar 31  2024 .profile
```
This command lists all files, including hidden ones in a long listing format. The output revealed a `data.txt`.

To understand the file format, we userd the `file` command:
```bash
bandit7@bandit:~$ file data.txt 
data.txt: Unicode text, UTF-8 text
```
This tells us that the file contains **text data** and is encoded in **UTF-8 format**.

To get a sense of how large this file is, we counted the number of lines:
```bash
bandit7@bandit:~$ wc -l data.txt 
98567 data.txt
```
With 98,567 lines, manually scanning through the file is out of the question.

Since we know the password is next to the word `millionth`, we can use `grep` to extract the relevant line:
```bash
bandit7@bandit:~$ cat data.txt | grep millionth
millionth	dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```
The password for the next level appeared!

## What we learned
- Using file to check file types and encodings.
- Using wc -l to count the number of lines in a file
- Using grep to search for specific text inside large files.

## Key command
`wc -l data.txt`

`cat data.txt | grep millionth`

***You are welcome!***
