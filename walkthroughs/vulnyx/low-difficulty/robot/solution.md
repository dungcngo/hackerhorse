# VulNyx - Robot

## Information

## Solution
### Enummeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 192.168.100.178 
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-28 14:11 +07
Stats: 0:00:28 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 50.00% done; ETC: 14:12 (0:00:06 remaining)
Nmap scan report for robot.lan (192.168.100.178)
Host is up (0.0023s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
80/tcp open  http    Apache httpd 2.4.56 ((Debian))
|_http-title: Hello Friend
|_http-server-header: Apache/2.4.56 (Debian)
MAC Address: 08:00:27:5D:66:EE (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 29.20 seconds
```

### Shell (elliot)
![web](/walkthroughs/vulnyx/low-difficulty/robot/web.png)

We download and analyze the image using `exiftool` and get the path `/B4ckUp_3LLi0t`

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -sX GET "http://192.168.100.178/" | grep "img src"
    <img src="image.jpg" alt="image" />
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ wget -q "http://192.168.100.178/image.jpg"                                 
                                                                                                                                                                       
┌──(dungcngo㉿kali)-[/tmp]
└─$ exiftool image.jpg 
ExifTool Version Number         : 13.36
File Name                       : image.jpg
Directory                       : .
File Size                       : 682 kB
File Modification Date/Time     : 2023:10:06 19:50:53+07:00
File Access Date/Time           : 2026:04:28 14:32:40+07:00
File Inode Change Date/Time     : 2026:04:28 14:32:40+07:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Comment                         : B4ckUp_3LLi0t/
Image Width                     : 1920
Image Height                    : 1080
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 1920x1080
Megapixels                      : 2.1
```

![backup-elliot](/walkthroughs/vulnyx/low-difficulty/robot/backup-web.png)

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://192.168.100.178/B4ckUp_3LLi0t -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -x bak, zip, rar, sql, old 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.100.178/B4ckUp_3LLi0t
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              ,bak
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta.bak             (Status: 403) [Size: 280]
/.hta                 (Status: 403) [Size: 280]
/.hta.                (Status: 403) [Size: 280]
/.htaccess.bak        (Status: 403) [Size: 280]
/.htpasswd.bak        (Status: 403) [Size: 280]
/.htpasswd            (Status: 403) [Size: 280]
/.htaccess            (Status: 403) [Size: 280]
/.htaccess.           (Status: 403) [Size: 280]
/.htpasswd.           (Status: 403) [Size: 280]
/connect.bak          (Status: 200) [Size: 266]
/index.html           (Status: 200) [Size: 481]
Progress: 14250 / 14250 (100.00%)
===============================================================
Finished
===============================================================
```

```
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl http://192.168.100.178//B4ckUp_3LLi0t/connect.bak
<?php

$client = new MongoDB\Client(
    'mongodb://127.0.0.1:27017'
    [
        'username' => 'mongo',
        'password' => 'm0ng0P4zz',
        'ssl' => true,
        'replicaSet' => 'myReplicaSet',
        'authSource' => 'admin',
        'db' => 'elliot',
    ],
);
```


### Privilege Escalation

***You are welcome!***
