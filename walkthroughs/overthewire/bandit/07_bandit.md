# Bandit07

## Level Description
The goal for this level was to find the password storted in a file somewhere on the server, which must meet the following criteria:
- Owned by user `bandit07`
- Owned by group `bandit06`
- Exactly 33 bytes in size.

## Method of solving
After logging into the server as user `bandit06`, we started by listing the contents of the current directory with `ls -la`, but we didn't find anything useful.
```bash
bandit6@bandit:~$ ls -la
total 20
drwxr-xr-x   2 root root 4096 Oct 14 09:25 .
drwxr-xr-x 150 root root 4096 Oct 14 09:29 ..
-rw-r--r--   1 root root  220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root root 3851 Oct 14 09:19 .bashrc
-rw-r--r--   1 root root  807 Mar 31  2024 .profile
```
Since the password file could be located anywhere on the system, we used the `find` command to search for files that met the specified criteria. We ran the following command:
```bash
bandit6@bandit:~$ find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null
/var/lib/dpkg/info/bandit7.password
```
It returned the file `/var/lib/dpkg/infor/bandit7.password`

We used to the `cat` command to read the contents of the file:
```bash
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password 
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
```
The password for the next level appeared!

## What we learned
- **Using find with Multiple Criteria**: The `find` commands is highly flexible, allowing me to combine multiple filters like file size, ownership, and permissions to find exactly what I needed.
- **Handling Permission Denied Errors**: When searching in directories without access, it’s important to suppress errors using `2>/dev/null` to keep the output clean.

## Key command
`find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null`

***You are welcome!***
