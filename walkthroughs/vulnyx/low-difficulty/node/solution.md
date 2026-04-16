# VulNyx - Node

## Information
**Node** is a low difficulty vulnerable Linux virtual machine from the VulNyx platform, it was created by user d4t4s3c and works correctly on VirtualBox and VMware hypervisors.

## Solution
### Enumeration
Using `nmap` command to scan server `192.168.100.185`:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sCV -p- -vv -T4 192.168.100.185
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-16 15:03 +07
NSE: Loaded 157 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 15:03
Completed NSE at 15:03, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 15:03
Completed NSE at 15:03, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 15:03
Completed NSE at 15:03, 0.00s elapsed
Initiating ARP Ping Scan at 15:03
Scanning 192.168.100.185 [1 port]
Completed ARP Ping Scan at 15:03, 0.11s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 15:03
Completed Parallel DNS resolution of 1 host. at 15:03, 0.01s elapsed
Initiating SYN Stealth Scan at 15:03
Scanning node.lan (192.168.100.185) [65535 ports]
Discovered open port 80/tcp on 192.168.100.185
Discovered open port 22/tcp on 192.168.100.185
Discovered open port 1880/tcp on 192.168.100.185
Completed SYN Stealth Scan at 15:04, 33.40s elapsed (65535 total ports)
Initiating Service scan at 15:04
Scanning 3 services on node.lan (192.168.100.185)
Completed Service scan at 15:04, 11.62s elapsed (3 services on 1 host)
NSE: Script scanning 192.168.100.185.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 15:04
Completed NSE at 15:04, 0.84s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 15:04
Completed NSE at 15:04, 0.05s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 15:04
Completed NSE at 15:04, 0.01s elapsed
Nmap scan report for node.lan (192.168.100.185)
Host is up, received arp-response (0.0019s latency).
Scanned at 2026-04-16 15:03:28 +07 for 46s
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE REASON         VERSION
22/tcp   open  ssh     syn-ack ttl 64 OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDP4OvUJ0xKoulS7xOYz1485bm/ZBVN/86xLQvh7Gqa1DmEWz/eHP2C3MJQnqTFPOEh18FULOzj9fiehyzhd6CM7+qBZ/4B9b5RkOx7AL+S3aRIey4qQj7/k72PqMBkyfD2krjNOg7ZZe8z9o0A4VyeDljG6ukVFeN6PEtWWtdmmnVJztgzX0wPWPaO9GM5hITyvpIB/Y/IqueYR+ft2n5ROLLUfjFLezB+zSa6xkDPGiY9qMZBMXA/6oaaD3TV1x6jfTtZi+Aca0scDfOTJUVlSwZYaHrJQSNlKFJhniucqq/zxOnMIHjs/v1YXYCh0jlYDsb5J/NqTzEPMKkbtwn97T5/FQvsWDGJFTtxvCCrInmnUHB+cG8dSRYQZ763QoPxF/feDSNbrKjTv8D1K2EPhf1rBGQGIObgatVHNFclVWfuq7sn4x9olNnbsEogIQ5mbEq0mBlgOW5vowFxUkI60Ond4Dl7H4fkCeiPfngWFrT+6cQoNgA3HRKf6NtQeYs=
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNDNbes4gKOy7nXoXxW1kPwOX/vuxNkae5WSrIFu+ZD8OUIX5OK8e6o7IZDJAxn/ACAJL9Mm+tA44syyemA6C40=
|   256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINItrDSHbBfPB1CJosqklAQXN4/Mt++ocUqbiG861ZSG
80/tcp   open  http    syn-ack ttl 64 Apache httpd 2.4.56 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.56 (Debian)
1880/tcp open  http    syn-ack ttl 64 Node.js Express framework
|_http-cors: GET POST PUT DELETE
|_http-favicon: Unknown favicon MD5: 818DD6AFD0D0F9433B21774F89665EEA
|_http-title: Node-RED
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
MAC Address: 08:00:27:D2:8A:34 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 15:04
Completed NSE at 15:04, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 15:04
Completed NSE at 15:04, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 15:04
Completed NSE at 15:04, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.69 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```


### Shell (dev)

### Privilege Escalation

anh
