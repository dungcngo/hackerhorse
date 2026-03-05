# Leviathan02

## Level Description
There is no information for this level, intentionally.

## Method of Solving
After logging into the `leviathan1` server, we run `ls -la` to look for hidden files or directories in the home directory:
```bash
leviathan1@leviathan:~$ ls -la
total 36
drwxr-xr-x   2 root       root        4096 Oct 14 09:27 .
drwxr-xr-x 150 root       root        4096 Oct 14 09:29 ..
-rw-r--r--   1 root       root         220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root        3851 Oct 14 09:19 .bashrc
-r-sr-x---   1 leviathan2 leviathan1 15084 Oct 14 09:27 check
-rw-r--r--   1 root       root         807 Mar 31  2024 .profile
```
There is a `check` SUID binary in the home directory owned by our target user, `leviathan2`.

When we run the `check` binary, it asks us for a password, but we don't know it.
```bash
leviathan1@leviathan:~$ ./check
password: 
```
We use the `ltrace` command to check which dynamic library calls and system calls are used when it is run:
```bash
leviathan1@leviathan:~$ ltrace ./check
__libc_start_main(0x80490ed, 1, 0xffffd474, 0 <unfinished ...>
printf("password: ")                             = 10
getchar(0, 0, 0x786573, 0x646f67password: 
)                = 10
getchar(0, 10, 0x786573, 0x646f67
)               = 10
getchar(0, 2570, 0x786573, 0x646f67
)             = 10
strcmp("\n\n\n", "sex")                          = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)             = 29
+++ exited (status 0) +++
```
We see that the binary is doing a `strcmp` function that checks the user input against the `sex` value. So, the correct password is `sex` and we run:
```bash
leviathan1@leviathan:~$ ./check 
password: sex
$ 
```
And get a shell prompt with `sh` shell and verifying which user we are:
```bash
$ whoami
leviathan2
$ 
```
Now, as the `leviathan2` user, we access the next level's password:
```bash
$ cat /etc/leviathan_pass/leviathan2
NsN1HwFoyN
```
## Key command
`ltrace ./check`

***You are welcome!***
