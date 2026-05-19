# VulNyx - Build

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sn 192.168.11.0/24       
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-19 14:19 +07
Nmap scan report for 192.168.11.1
Host is up (0.0012s latency).
MAC Address: 0A:00:27:00:00:0B (Unknown)
Nmap scan report for 192.168.11.2
Host is up (0.00075s latency).
MAC Address: 08:00:27:28:99:92 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.11.26
Host is up (0.0043s latency).
MAC Address: 08:00:27:AC:63:E6 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.11.10
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 2.07 seconds

┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap 192.168.11.26             
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-19 14:17 +07
Nmap scan report for 192.168.11.26
Host is up (0.0042s latency).
Not shown: 995 closed tcp ports (reset)
PORT     STATE SERVICE
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
8080/tcp open  http-proxy
MAC Address: 08:00:27:AC:63:E6 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 2.34 seconds

┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p80,135,139,445,8080 192.168.11.26
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-19 14:21 +07
Nmap scan report for 192.168.11.26
Host is up (0.012s latency).

PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
8080/tcp open  http          Jetty 12.0.19
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Jetty(12.0.19)
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
MAC Address: 08:00:27:AC:63:E6 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: BUILD, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:ac:63:e6 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
|_clock-skew: 13h59m58s
| smb2-time: 
|   date: 2026-05-19T21:21:18
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.53 seconds
```

### Shell

### Privilege Escalation

***You are welcome!***
