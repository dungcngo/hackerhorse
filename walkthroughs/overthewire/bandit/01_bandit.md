# Bandit01: Just list

## Level Description
The task of this level was straighforward: we needed to find the password for the user `bandit1`. The hint said the password was stored in a file named `readme` located in the home directory. Once we found it, we had to use the password to log into the user `bandit1`, using SSH like always on port `2220`.

## Method of Solving
After successfully logging into the server as `bandit0`, we typed `ls` to list the files in the current directory, and sure enough, there was the `readme` file.
Next, we used the `cat` command to peek inside the file:
```bash
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
Congratulations on your first steps into the bandit game!!
Please make sure you have read the rules at https://overthewire.org/rules/
If you are following a course, workshop, walkthrough or other educational activity,
please inform the instructor about the rules as well and encourage them to
contribute to the OverTheWire community so we can keep these games free!

The password you are looking for is: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
```

## What we learned
- **File listing (`ls`)**: Always check your surroundings first! The `ls` command is your best friend for seeing what files are available.
- **Reading Files (`cat`)**: Simple yet powerful, `cat` allows you to quickly view the contents of a file.
- **Logging into Next Level**: Every password is used to log into the next level using SSH.

## Key command
`ls`

`cat readme`

***You are welcome!***
