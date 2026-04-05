## Identity Host IP (Attacker Machine)
In Kali Linux, we use `ifconfig` command:
```bash
┌──(dungcngo㉿kali)-[~]
└─$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        ether 08:00:27:76:d1:ed  txqueuelen 1000  (Ethernet)
        RX packets 31247  bytes 38261100 (36.4 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 8294  bytes 1646289 (1.5 MiB)
        TX errors 0  dropped 8 overruns 0  carrier 0  collisions 0

eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.11.3  netmask 255.255.255.0  broadcast 192.168.11.255
        inet6 fe80::6ea2:321d:d0ba:1685  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:b5:57:1b  txqueuelen 1000  (Ethernet)
        RX packets 69020  bytes 4825687 (4.6 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 69905  bytes 4301200 (4.1 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        ether 08:00:27:1b:39:31  txqueuelen 1000  (Ethernet)
        RX packets 69  bytes 5596 (5.4 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 119  bytes 14412 (14.0 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 78  bytes 5892 (5.7 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 78  bytes 5892 (5.7 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

## Discover Metasploitable2 IP
```bash
┌──(dungcngo㉿kali)-[~]
└─$ nmap -sn 192.168.11.0/24
```
```bash
┌──(dungcngo㉿kali)-[~]
└─$ nmap -sn 192.168.11.0/24 
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-05 09:12 +07
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 192.168.11.1
Host is up (0.00053s latency).
MAC Address: 0A:00:27:00:00:0B (Unknown)
Nmap scan report for 192.168.11.2
Host is up (0.00034s latency).
MAC Address: 08:00:27:6C:2B:E8 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.11.5   <--- This target IP
Host is up (0.0012s latency).
MAC Address: 08:00:27:A9:B8:5A (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.11.3
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 2.30 seconds
```

## Service Enumeration & Scripted Scan
```bash
nmap -sV -sC 192.168.11.5 -oN nmap_scan.txt  
```

- `-sV`: Version detection
- `-sC`: Default NSE script
- `-oN`: Save output to file
