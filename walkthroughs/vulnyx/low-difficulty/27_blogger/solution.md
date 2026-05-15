# VulNyx - Blogger

## Information

## Solution
### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.8    
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-15 16:51 +07
Nmap scan report for 10.11.5.8
Host is up (0.0014s latency).
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
MAC Address: 08:00:27:C8:C8:33 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.51 seconds
```
#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.8/ -w /usr/share/seclists/Discovery/Web-Content/common.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.8/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 274]
/.htaccess            (Status: 403) [Size: 274]
/.htpasswd            (Status: 403) [Size: 274]
/index.html           (Status: 200) [Size: 10701]
/server-status        (Status: 403) [Size: 274]
/wordpress            (Status: 301) [Size: 310] [--> http://10.11.5.8/wordpress/]
Progress: 4750 / 4750 (100.00%)
===============================================================
Finished
===============================================================
```

#### Wordpress
![web wordpress](/walkthroughs/vulnyx/low-difficulty/27_blogger/web-wordpress.png)

We check version of WordPress by seeing in source code: `WordPress 6.3`.

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wpscan --url http://10.11.5.8/wordpress/ --enumerate vp,vt,u
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.28
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://10.11.5.8/wordpress/ [10.11.5.8]
[+] Started: Fri May 15 17:00:18 2026

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.56 (Debian)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://10.11.5.8/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://10.11.5.8/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://10.11.5.8/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 6.3 identified (Insecure, released on 2023-08-08).
 | Found By: Emoji Settings (Passive Detection)
 |  - http://10.11.5.8/wordpress/, Match: 'wp-includes\/js\/wp-emoji-release.min.js?ver=6.3'
 | Confirmed By: Meta Generator (Passive Detection)
 |  - http://10.11.5.8/wordpress/, Match: 'WordPress 6.3'

[i] The main theme could not be detected.

[+] Enumerating Vulnerable Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Vulnerable Themes (via Passive and Aggressive Methods)
 Checking Known Locations - Time: 00:00:01 <====> (652 / 652) 100.00% Time: 00:00:01

[i] No themes Found.

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:01 <======> (10 / 10) 100.00% Time: 00:00:01

[i] User(s) Identified:

[+] peter
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Fri May 15 17:01:15 2026
[+] Requests Done: 699
[+] Cached Requests: 4
[+] Data Sent: 192.759 KB
[+] Data Received: 211.391 KB
[+] Memory used: 264.234 MB
[+] Elapsed time: 00:00:56
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.8/wordpress/ -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.8/wordpress/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 274]
/.htpasswd            (Status: 403) [Size: 274]
/.hta                 (Status: 403) [Size: 274]
/index.php            (Status: 301) [Size: 0] [--> http://10.11.5.8/wordpress/]
/wp-admin             (Status: 301) [Size: 319] [--> http://10.11.5.8/wordpress/wp-admin/]                                                                              
/wp-content           (Status: 301) [Size: 321] [--> http://10.11.5.8/wordpress/wp-content/]                                                                            
/wp-includes          (Status: 301) [Size: 322] [--> http://10.11.5.8/wordpress/wp-includes/]                                                                           
/xmlrpc.php           (Status: 405) [Size: 42]
Progress: 4613 / 4613 (100.00%)
===============================================================
Finished
===============================================================
```

![web source code](/walkthroughs/vulnyx/low-difficulty/27_blogger/web-source-code.png)



### Shell

### Privilege Escalation

***You are welcome!***
