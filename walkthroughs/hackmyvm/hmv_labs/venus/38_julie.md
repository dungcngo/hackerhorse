# 0x38
This write-up explains the steps taken to complete mission 0x36, starting from user `julie` and escalating to `irene`.

## Mission 
The mission for this stage provided a cryptic clue:
```bash
julie@venus:~$ cat mission.txt 
################
# MISSION 0x38 #
################

## EN ##
The user irene believes that the beauty is in the difference.
```

## Method of solving
In the home directory, we find two text files, `1.txt` and `2.txt`, both excatly 4802 bytes in size. This suggested that the files are nearly identical, but contained a specific discrepancy that held the password.
```bash
julie@venus:~$ ls -la
total 48
drwxr-x--- 2 root  julie 4096 Apr  5  2024 .
drwxr-xr-x 1 root  root  4096 Apr  5  2024 ..
-rw-r--r-- 1 julie julie  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 julie julie 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 julie julie  807 Apr 23  2023 .profile
-rw-r----- 1 root  julie 4802 Apr  5  2024 1.txt
-rw-r----- 1 root  julie 4802 Apr  5  2024 2.txt
-rw-r----- 1 root  julie   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root  julie  192 Apr  5  2024 mission.txt
```
To find "beauty in the difference", we use the `diff` command. This tool compares two files line by line and outputs the specific lines where they do not match.
```bash
julie@venus:~$ diff 1.txt 2.txt 
174c174
< 8VeRLEFkBpe2DSD   <---- This is the password captured
---
> aNHRdohjOiNizlU
```
**Explanation:**

`diff`: A fundamental utility used to find differences between two files. In CTFs, this is commonly used when two large files are provided and you need to find the one unique string hidden inside.

`174c174`: This indicates that a change exists on line 174 of both files.
`< 8VeRLEFkBpe2DSD`: This shows the content present in the first file (1.txt).
`> aNHRdohjOiNizlU`: This shows the content present in the second file (2.txt).

**The Finding**: Between the two unique strings, the one from the first file proved to be the valid password for the next user.


Using this password, we switch to user `irene` and get the flag.
```bash
julie@venus:~$ su - irene
Password: 
irene@venus:~$ id ; whoami
uid=1039(irene) gid=1039(irene) groups=1039(irene)
irene
```

## Key command
`diff 1.txt 2.txt`
	
***You are welcome!***
