# Bandit09

## Level Description
The goal for this level is to find the password stored in the file named `data.txt` which is the only line of the text that occurs only once. 

## Method of Solving
After logging in as `bandit7`, like usual:
```bash
bandit8@bandit:~$ ls -la
total 56
drwxr-xr-x   2 root    root     4096 Oct 14 09:26 .
drwxr-xr-x 150 root    root     4096 Oct 14 09:29 ..
-rw-r--r--   1 root    root      220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root    root     3851 Oct 14 09:19 .bashrc
-rw-r-----   1 bandit9 bandit8 33033 Oct 14 09:26 data.txt
-rw-r--r--   1 root    root      807 Mar 31  2024 .profile
```
This return file is named `data.txt` and is in the home directory.

We used a command `file` to determine its type:
```bash
bandit8@bandit:~$ file data.txt 
data.txt: ASCII text
```
We were curious how many lines are there on that file, we have been checking it and it contains 1001 lines.
```bash
bandit8@bandit:~$ wc -l data.txt 
1001 data.txt
```
With that amount of lines, we knew we were not going to check it manually line-by-line.

We are going to sort the file with the `sort` command and then send the output as input using `|` (pipeline) to the `uniq` command with `-u` as a flag because our goal is to find the lines that occur only once.
```bash
bandit8@bandit:~$ sort data.txt | uniq -u
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
```
The password for the next level appeared!

## What we learned
- **Sorting text with `sort`**: Ensures duplicate lines are grouped together, making it easier to filter unique lines.
- **Filtering unique lines with `uniq -u`**: Extract only lines that appear once, which was key to finding the password.
- **Using pipes `|` for command chaining**: Allows combining multiple commands efficiently for streamlined data processing.

## Key command
`sort data.txt | uniq -u`

***You are welcome!***
