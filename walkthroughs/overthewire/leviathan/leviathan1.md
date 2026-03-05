# Leviathan01

## Level Description
There is no information for this level, intentionally.

## Method of Solving
After logging into the `leviathan0` server, we run `ls -la` to look for hidden files or directories in the home directory:
```bash
leviathan0@leviathan:~$ ls -la
total 24
drwxr-xr-x   3 root       root       4096 Oct 14 09:27 .
drwxr-xr-x 150 root       root       4096 Oct 14 09:29 ..
drwxr-x---   2 leviathan1 leviathan0 4096 Oct 14 09:27 .backup
-rw-r--r--   1 root       root        220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root       3851 Oct 14 09:19 .bashrc
-rw-r--r--   1 root       root        807 Mar 31  2024 .profile
```
There is a highlighted directory called `.backup`, we enter this directory and continue list hidden directories or file by using `ls`:
```bash
leviathan0@leviathan:~$ cd .backup/
leviathan0@leviathan:~/.backup$ ls -la
total 140
drwxr-x--- 2 leviathan1 leviathan0   4096 Oct 14 09:27 .
drwxr-xr-x 3 root       root         4096 Oct 14 09:27 ..
-rw-r----- 1 leviathan1 leviathan0 133259 Oct 14 09:27 bookmarks.html
```
Inside, there is one file `bookmarks.html`. We check the file typte:
```bash
leviathan0@leviathan:~/.backup$ file bookmarks.html 
bookmarks.html: HTML document, ASCII text, with very long lines (302)
```
We use `cat` and `grep` to search for anything that mentioned the nextlevel:
```bash
leviathan0@leviathan:~/.backup$ cat bookmarks.html | grep leviathan
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is 3QJ3TgzHDq" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```
New we can log in as `leviathan1` using this retrieved password.

## Key command
`ls -la`

`cat bookmarks.html | grep leviathan (or password)`

***You are welcome!***
