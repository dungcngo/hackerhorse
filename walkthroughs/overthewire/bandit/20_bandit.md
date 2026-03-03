# Bandit20

## Level Description
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## Method of Solving
We logged into the `bandit19` server using SSH. We list the contents of the home directory:
```bash
bandit19@bandit:~$ ls -la
total 36
drwxr-xr-x   2 root     root      4096 Oct 14 09:26 .
drwxr-xr-x 150 root     root      4096 Oct 14 09:29 ..
-rwsr-x---   1 bandit20 bandit19 14884 Oct 14 09:26 bandit20-do
-rw-r--r--   1 root     root       220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root     root      3851 Oct 14 09:19 .bashrc
-rw-r--r--   1 root     root       807 Mar 31  2024 .profile
```
This reveals a single file `bandit20-do`. The `s` in the permissions (`rws`) indicates that this is a `setuid binary`. This means the binary runs with the privileges of the file owner (`bandit20`), not the user executing it (`bandit19`).

We check the file type using the `file` command:
```bash
bandit19@bandit:~$ file bandit20-do 
bandit20-do: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=38f1351d0068ccbbace0e437f34859de85e63025, for GNU/Linux 3.2.0, not stripped
```
We use the `bandit20-do` binary to execute commands as the `bandit20` user. To retrieve the password for `bandit20`, we run:
```bash
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```
The output is the password.

## Key command
`./bandit20-do cat /etc/bandit_pass/bandit20`

***You are welcome!***
haha
