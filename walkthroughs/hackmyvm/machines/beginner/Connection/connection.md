# Connection

## Summary

## Reconnaissance
### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sn 192.168.11.0/24          
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-03 15:41 +07
Nmap scan report for 192.168.11.1
Host is up (0.010s latency).
MAC Address: 0A:00:27:00:00:0B (Unknown)
Nmap scan report for 192.168.11.2
Host is up (0.010s latency).
MAC Address: 08:00:27:C2:00:F1 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.11.11
Host is up (0.00093s latency).
MAC Address: 08:00:27:71:CD:2C (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.11.10
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 2.30 seconds
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 192.168.11.11  
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-03 15:41 +07
Nmap scan report for 192.168.11.11
Host is up (0.00079s latency).
Not shown: 65531 closed tcp ports (reset)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 b7:e6:01:b5:f9:06:a1:ea:40:04:29:44:f4:df:22:a1 (RSA)
|   256 fb:16:94:df:93:89:c7:56:85:84:22:9e:a0:be:7c:95 (ECDSA)
|_  256 45:2e:fb:87:04:eb:d1:8b:92:6f:6a:ea:5a:a2:a1:1c (ED25519)
80/tcp  open  http        Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Apache2 Debian Default Page: It works
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.9.5-Debian (workgroup: WORKGROUP)
MAC Address: 08:00:27:71:CD:2C (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: Host: CONNECTION; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -1d19h50m23s, deviation: 2h18m34s, median: -1d21h10m23s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-05-01T11:32:06
|_  start_date: N/A
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.9.5-Debian)
|   Computer name: connection
|   NetBIOS computer name: CONNECTION\x00
|   Domain name: \x00
|   FQDN: connection
|_  System time: 2026-05-01T07:32:07-04:00
|_nbstat: NetBIOS name: CONNECTION, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.24 seconds
```
## Initial Access

## Privilege Esacalation
