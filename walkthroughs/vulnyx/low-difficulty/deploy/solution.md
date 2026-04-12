# VulNyx - Deploy

## Information
Deploy is vulnerable Linux virtual machine of low difficulty from the VulNyx platform, it was created by the `mow` user and works correctly on the VirtualBox and VMWare hypervisors.

## Solution
### Enumeration
```bash
┌──(dungcngo㉿kali)-[~]
└─$ nmap -n -Pn -sS -p- --min-rate 5000 192.168.100.150
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-10 11:19 +07
Nmap scan report for 192.168.100.150
Host is up (0.0033s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
8080/tcp open  http-proxy
MAC Address: 08:00:27:8E:59:08 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 142.64 seconds
```

```bash
┌──(dungcngo㉿kali)-[~]
└─$ nmap -sVC -p22,80,8080 192.168.100.150             
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-10 11:22 +07
Nmap scan report for deploy.lan (192.168.100.150)
Host is up (0.0013s latency).

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
80/tcp   open  http    Apache httpd 2.4.56 ((Debian))
|_http-server-header: Apache/2.4.56 (Debian)
|_http-title: Apache2 Debian Default Page: It works
8080/tcp open  http    Apache Tomcat
|_http-title: Apache Tomcat
|_http-open-proxy: Proxy might be redirecting requests
MAC Address: 08:00:27:8E:59:08 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.31 seconds
```

### Shell (tomcat)
![manager_webapp](/walkthroughs/vulnyx/low-difficulty/deploy/manager-webapp.png)

### Shell (sa)

### Shell (toor)

### Previlege Escalation




