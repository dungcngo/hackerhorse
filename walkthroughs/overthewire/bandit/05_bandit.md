# Bandit05

## Level Description
The goal for this level to find the password stored in the only human-readable file inside the `inhere` directory. The trick was to identify which of the multiple files in the directory contained readable text and then extract the password.

## Method of Solving
After logging into the server as `bandit4`, we started by listing the contents of the home directory:
```bash
bandit4@bandit:~$ ls
inhere
```
We noticed a directory named `inhere`, so we checked its contents:
```bash
bandit4@bandit:~$ ls inhere/
-file00  -file02  -file04  -file06  -file08
-file01  -file03  -file05  -file07  -file09
```
Its contained multiple files named `-file00`, `-file01`, and so on. Since the goal was to find the *human-readable* file , we needed a way to determine the type of each file.

We decided to use the `file` command, which identifies the type of content within the files:
```bash
bandit4@bandit:~$ file ./inhere/*
./inhere/-file00: data
./inhere/-file01: data
./inhere/-file02: data
./inhere/-file03: data
./inhere/-file04: data
./inhere/-file05: data
./inhere/-file06: data
./inhere/-file07: ASCII text
./inhere/-file08: data
./inhere/-file09: data
```
This revealed the following:
- Most of the files contained data.
- One file, `-file07` was identified as ASCII text (human-readable).
Once we had the file name, we used the `cat` command to read its contents:
```bash
bandit4@bandit:~$ cat ./inhere/-file07
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
```
And there is the password for the next level!

## What we learned
- **Using the `file` Command**: The `file` command is an excellent tool for determining the type of data within files. It’s especially useful when dealing with files of unknown or mixed content.
- **Interpreting File Types**: Understanding that **ASCII text** indicates human-readable content allowed me to pinpoint the correct file quickly.
- **Efficient Searching**: With multiple files in a directory, it’s important to use tools that can help narrow the search. This strategy is crucial in CTF challenges.

## Key command
`file ./inhere/*`

`cat ./inhere/-file07`

***You are welcome!***
