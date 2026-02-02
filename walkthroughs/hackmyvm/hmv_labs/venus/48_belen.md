# 0x48
This write-up explains the steps taken to complete mission 0x48, starting from user `belen` and escalating to `leona`.

## Mission
As always, we read the objective:
```bash
belen@venus:~$ cat mission.txt 
################
# MISSION 0x48 #
################

## EN ##
It seems that belen has stolen the password of the user leona...
```

## Method of solving
We found a file named `stolen.txt` in the home directory. 
```bash
belen@venus:~$ ls -la 
total 36
drwxr-x--- 2 root  belen 4096 Apr  5  2024 .
drwxr-xr-x 1 root  root  4096 Apr  5  2024 ..
-rw-r--r-- 1 belen belen  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 belen belen 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 belen belen  807 Apr 23  2023 .profile
-rw-r----- 1 root  belen   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root  belen  197 Apr  5  2024 mission.txt
-rw-r----- 1 root  belen   32 Apr  5  2024 stolen.txt
```
Checking its content revealed a **Unix hash string** rather than a cleartext password.
```bash
belen@venus:~$ cat stolen.txt 
$1$leona$lhWp56YnWAMz6z32Bw53L0
```

Since password cracking tools like `john` or `hashcat` were not installed on the remote server. We had to exfiltrate the hash to my local attach machine.
1. We use `scp` from my local machine to download the file from the target machine.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ scp -P 5000 belen@venus.hackmyvm.eu:~/stolen.txt .
belen@venus.hackmyvm.eu's password: 
stolen.txt                                                   100%   32     0.1KB/s   00:00  
```
2. **Identify the Hash Type**: The $1$ prefix identifies this as MD5crypt (MD5-based Unix password hash). In hashcat, this corresponds to mode 500.
3. **Perform the Crack:** I ran hashcat using the famous `rockyou.txt` wordlist.
```bash
──(dungcngo㉿kali)-[/tmp]
└─$ hashcat -m 500 stolen.txt /usr/share/wordlists/rockyou.txt       
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
-------------------------------------------
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 6 secs

$1$leona$lhWp56YnWAMz6z32Bw53L0:freedom                   
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 500 (md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5))
Hash.Target......: $1$leona$lhWp56YnWAMz6z32Bw53L0
--------------------------------------------
Started: Mon Feb  2 04:05:45 2026
Stopped: Mon Feb  2 04:08:12 2026
```
Or 
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat stolen.txt > leona.hash    
                                                                                               
┌──(dungcngo㉿kali)-[/tmp]
└─$ john --format=md5crypt --wordlist=/usr/share/wordlists/rockyou.txt leona.hash
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 128/128 SSE2 4x3])
No password hashes left to crack (see FAQ)
                                                                                               
┌──(dungcngo㉿kali)-[/tmp]
└─$ john --show leona.hash                                                       
?:freedom

1 password hash cracked, 0 left
```
Using the retrieve password, we switch to user `leona` and get the flag.
```bash
belen@venus:~$ su - leona
Password: 
leona@venus:~$ id ; whoami
uid=1049(leona) gid=1049(leona) groups=1049(leona)
leona
```

## Key commands
`hashcat -m 500 stolen.txt /usr/share/wordlists/rockyou.txt`
`john --format=md5crypt --wordlist=/usr/share/wordlists/rockyou.txt leona.hash`


***You are welcome!***

***You are welcome!***
