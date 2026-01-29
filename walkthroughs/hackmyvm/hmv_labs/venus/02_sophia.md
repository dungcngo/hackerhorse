# 0x02
This write-up walks through how mission 0x02 was completed, moving from user `sophia` to `angela`.

## Mission
In the home directory, read the `mission.txt`:
```bash
sophia@venus:~$ ls -la
total 36
drwxr-x--- 1 root   sophia 4096 Apr  5  2024 .
drwxr-xr-x 1 root   root   4096 Apr  5  2024 ..
-rw-r--r-- 1 sophia sophia  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 sophia sophia 3755 Jan 18 20:50 .bashrc
-rw-r--r-- 1 sophia sophia  807 Apr 23  2023 .profile
-rw-r----- 1 root   sophia   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root   sophia  359 Apr  5  2024 mission.txt
```
```bash
sophia@venus:~$ cat mission.txt 
################
# MISSION 0x02 #
################

## EN ##
The user angela has saved her password in a file but she does not remember where ... she only remembers that the file was called whereismypazz.txt
```
basically, our objective is to find a file called `whereismypazz.txt`.
	
## Method of solve
Since we don't know where the file is, using `find` command will be really helpful in this case.
```bash
sophia@venus:~$ find / -type f -name "whereismypazz.txt" 2>/dev/null
/usr/share/whereismypazz.txt
```
It starts seaching from `/` root directory, specifying the type and the exact name.

`2>/dev/null` is simply redirected standard error output to `/dev/null`. So, the screen stays clear from permission errors.

Just read that file:
```bash
sophia@venus:~$ cat /usr/share/whereismypazz.txt 
oh5p9gAABugHBje
```
Got the password for user `angela`, let's check if it works:
```bash
sophia@venus:~$ su - angela
Password: 
GOGETA SSJ1!
angela@venus:~$ id ; whoami
uid=1003(angela) gid=1003(angela) groups=1003(angela),1054(www3)
angela
```
We're now logged in as `angela`, print out the flag:
```bash
angela@venus:~$ cat flagz.txt 
8===SjMYBmMh4bk49TKq7PM8===D~~
```
	
## Key command
`find / -name whereismypazz.txt 2>/dev/null`

***You are welcome!***
