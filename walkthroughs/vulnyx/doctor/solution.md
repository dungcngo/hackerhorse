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
