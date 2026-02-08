# Bandit02

## Level Description
The goal for this level was to find the password for the next level, which was hidden in a file named `-` in the home directory. The tricky part was dealing with the filename, `-` can confuse commands into thinking it's an option or flag. Once we had the password, we needed to log into `bandit2` using SSH on port `2220`.

## Method of Solving
After logging into the servers as `bandit1`, we immediately listed the contents of the home directory.
```bash
bandit1@bandit:~$ ls -la
total 24
-rw-r-----   1 bandit2 bandit1   33 Oct 14 09:26 -
drwxr-xr-x   2 root    root    4096 Oct 14 09:26 .
drwxr-xr-x 150 root    root    4096 Oct 14 09:29 ..
-rw-r--r--   1 root    root     220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root    root    3851 Oct 14 09:19 .bashrc
-rw-r--r--   1 root    root     807 Mar 31  2024 .profile
```
There was a single file named `-`. At first glance, it seemed straightforward to use `cat` to read the file, so we tried:
```bash
bandit1@bandit:~$ cat -

```
But instead of showing the file contents, the command seeme to think we were passing a flag.

The solution was to specify the file path explicitly, so we used `./` to refer to the current directory:
```bash
bandit1@bandit:~$ cat ./-
263JGJPfgU6LtdEvgfWU1XP5yac29mFx
```
There was the password for the next level.

## What we learned
- **Handling Special Filenames**: Files named with special characters like `-` can confuse commands. Prefixing the file name with `./` tells the command explicitly, “This is a file in the current directory.”
- **Clearing Command Usage Confusion**: When a command doesn’t behave as expected, look closely at the error or usage messages—they can point you toward the solution.
- **Reinforcing File Operations**: Commands like cat can have quirks, and understanding how to handle them is key for CTF challenges.

## Key command
`ls -la`

`cat ./-`

***You are welcome!***
