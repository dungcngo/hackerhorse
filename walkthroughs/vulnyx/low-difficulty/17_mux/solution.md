# VulNyx - Mux

## Information

## Solution
### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sCV -p- -T4 192.168.11.14  
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-06 08:07 +07
Nmap scan report for 192.168.11.14
Host is up (0.0019s latency).
Not shown: 65531 closed tcp ports (reset)
PORT    STATE SERVICE VERSION
80/tcp  open  http    Apache httpd 2.4.56 ((Debian))
|_http-server-header: Apache/2.4.56 (Debian)
|_http-title: Monna Lisa
512/tcp open  exec    netkit-rsh rexecd
513/tcp open  login
514/tcp open  shell   Netkit rshd
MAC Address: 08:00:27:C7:DD:4F (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.26 seconds
```
![web port 80](/walkthroughs/vulnyx/low-difficulty/mux/web-monnalisa.png)


### Shell

### Privilege Escalation


***You are welcome!***
