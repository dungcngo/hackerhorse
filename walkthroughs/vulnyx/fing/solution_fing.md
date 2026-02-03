# FING - VulNyx

## Information
**Fing** is a low-difficulty vulnerable Linux virtual machine from the VulNyx platfrom, created by the user **d4t4s3c**, and it runs properly on both VirtualBox and VMware.

## Solution 
### Enumeration
**Nmap**/TCP
Use Nmap to scan the ports on the Fing's IP address (192.168.100.230).
```bash
┌──(dungcngo㉿kali)-[~]
└─$ nmap -n -Pn -sS -p- --min-rate 5000 192.168.100.230
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-03 01:32 EST
Nmap scan report for 192.168.100.230
Host is up (0.045s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
79/tcp open  finger
80/tcp open  http
MAC Address: 08:00:27:6E:57:FA (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 128.43 seconds
```
The host at 192.168.100.230 is up, with three services listening: SSH, Finger, and HTTP. All other ports are closed.

```bash
┌──(dungcngo㉿kali)-[~]
└─$ nmap -sVC -p22,79,80 192.168.100.230               
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-03 01:35 EST
Nmap scan report for fing.lan (192.168.100.230)
Host is up (0.0014s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
79/tcp open  finger  Linux fingerd
|_finger: No one logged on.\x0D
80/tcp open  http    Apache httpd 2.4.56 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.56 (Debian)
MAC Address: 08:00:27:6E:57:FA (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.65 seconds
```
The victim host at 192.168.1.43 is running:
- SSH for remote administration.
- Finger (an old, rarely used service that my leak information).
- An Apache HTTP server with the default page, indicating that the web server is active but no specific application has been deployed yet.

### Shell 
#### 79/TCP (FINGER)
**Use Brute-Force**




