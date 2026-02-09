# Bandit12

## Level Description
In this level, the password we are looking for is stored in the file `data.txt`, where all lowercase (a-z) and uppercase(A-Z) letters have been rotated by 13 positions.

## Method of Solving
Upon logging in as `bandit11`, we always check contents of home directory and it's file type if there it is.
```bash
bandit11@bandit:~$ ls -la
total 24
drwxr-xr-x   2 root     root     4096 Oct 14 09:25 .
drwxr-xr-x 150 root     root     4096 Oct 14 09:29 ..
-rw-r--r--   1 root     root      220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root     root     3851 Oct 14 09:19 .bashrc
-rw-r-----   1 bandit12 bandit11   49 Oct 14 09:25 data.txt
-rw-r--r--   1 root     root      807 Mar 31  2024 .profile
bandit11@bandit:~$ file data.txt 
data.txt: ASCII text
```
Let's view the contents of this file:
```bash
bandit11@bandit:~$ cat data.txt 
Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4
```
A common encoding method in CTF challenges is ROT13. ROT13 is a simple cipher the shifts each letter by 13 positions, and we can use `rot13` to decode it.

We use `scp` to copy the `data.txt` file back to the local machine so that we can run `rot13` on it.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ scp -P 2220 bandit11@bandit.labs.overthewire.org:~/data.txt . 
...
backend: gibson-0
bandit11@bandit.labs.overthewire.org's password: 
data.txt                                      100%   49     0.1KB/s   00:00   
```
We type this command to retrieve the password on the local machine:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat data.txt | rot13    
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```
The password for the next level appeared!

## What we learned
- **`scp` command**: `scp` works similarly to `cp` (copy), but instead of copying  within the same system, it can tranfer files over the network. The data being sent is encrypted using SSH.
- **ROT13 Encoding**: A simpel substitution cipher that shifts letters by 13 places.

## Key command
`cat data.txt | rot13`

***You are welcome!***
