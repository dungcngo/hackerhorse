# 0x34
This write-up explains the steps taken to complete mission 0x34, starting from user `noa` and escalating to `maia`.

## Mission 
As usual, read the objective first:
```bash
noa@venus:~$ cat mission.txt 
################
# MISSION 0x34 #
################

## EN ##
The password of maia is surrounded by trash 
```

## Method of solving
We checked the home directory and found a file named `trash`. This file is significantly larger than the others (3818 bytes) and contains binary data.
```bash
noa@venus:~$ ls -la
total 36
drwxr-x--- 2 root noa  4096 Apr  5  2024 .
drwxr-xr-x 1 root root 4096 Apr  5  2024 ..
-rw-r--r-- 1 noa  noa   220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 noa  noa  3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 noa  noa   807 Apr 23  2023 .profile
-rw-r----- 1 root noa    31 Apr  5  2024 flagz.txt
-rw-r----- 1 root noa   159 Apr  5  2024 mission.txt
-rw-r----- 1 root noa  3818 Apr  5  2024 trash
```
Running `file trash` confirmed it is identified as "data", meaning it's not a standard text file and contains many non-printable characters.
```bash
noa@venus:~$ file trash 
trash: data
```

To find the password "surrounded by trash", I used the `string` command. This tool ignores the binary "junk" and extracts sequences of printables characters.
```bash
noa@venus:~$ strings trash 
b;pK
*&dv
 |.-
wsG9
D55-
\|gu
1q#^
...
=I+"
xfFN
\nh1hnDPHpydEjoEN   <--- This is password captured
!	2L~8
JmN8
@%`j
...
```
**Explanation:**
- `strings`: This is the go-to tool when a password or flag is hidden inside a binary, executable, or corrupted file. It looks for sequences of 4 or more printable chacracter.
- __The Findings__: Amidst the random snippets of text, one specific alphanumeric string stood out as a likely candidate for a password. In this case, the string was `h1hnDPHpydEjoEN`.

Using the extracted string from the `trach` file, switching to user `maia` and get the flag.
```bash
noa@venus:~$ su - maia
Password: 
maia@venus:~$ id ; whoami
uid=1035(maia) gid=1035(maia) groups=1035(maia)
maia
```

## Key command
`strings -14 trash` (14 is length of password)

***You are welcome!***
