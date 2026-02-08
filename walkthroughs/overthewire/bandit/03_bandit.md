# Bandit03

## Level Description
The goal for this level was to retrieved the password stored in a file named `--space in the filename--` located in the home directory. The challenge here was dealing with spaces in the file name, which required special handling when using commands.

## Method of Solving
After logging into the server as `bandit2`, we listed the contents of home directory:
```bash
bandit2@bandit:~$ ls -la
total 24
drwxr-xr-x   2 root    root    4096 Oct 14 09:26 .
drwxr-xr-x 150 root    root    4096 Oct 14 09:29 ..
-rw-r--r--   1 root    root     220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root    root    3851 Oct 14 09:19 .bashrc
-rw-r--r--   1 root    root     807 Mar 31  2024 .profile
-rw-r-----   1 bandit3 bandit2   33 Oct 14 09:26 --spaces in this filename--
```
There was a file named `--space in this file name--`. We knew that filenames containning spaces can't just be typed directly into commands without either quoting them or escaping the spaces.
To read the file, we use escaping the spaces with backslashes:
```bash
bandit2@bandit:~$ cat ./--spaces\ in\ this\ filename-- 
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
```
There was the password for the next level.

## What we learned
- **Handling Filenames with Spaces**: When dealing with filenames that include spaces, quoting the filenames (e.g., 'filename with spaces') or escaping the spaces (e.g., `filename\ with\ spaces`)is essential.
- **File Operations**: This challenge reinforced the importance of understanding how to handle unconventional file names in Linux.

## Key command
`cat ./--spaces\ in\ this\ filename--`

***You are welcome!***
