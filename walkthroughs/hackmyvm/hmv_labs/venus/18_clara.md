# 0x18
This write-up explains the steps taken to complete mission 0x18, starting from user `clara` and escalating to `frida`.

## Mission
As always, read the mission first:
```bash
clara@venus:~$ cat mission.txt 
################
# MISSION 0x18 #
################

## EN ##
The password of user frida is in the password-protected zip (rockyou.txt can help you) 
```

## Method of solving
The target machine lacks `john` or `zip2john`. The `protected.zip` file must be transferred to our local attack machine.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ scp -P 5000 clara@venus.hackmyvm.eu:~/protected.zip .  
clara@venus.hackmyvm.eu's password: 
protected.zip                                 100%  244     0.6KB/s   00:00   
```
Once on our local machine, we use `zip2john` to extract the password hash.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ zip2john protected.zip > clara.hash
ver 1.0 efh 5455 efh 7875 protected.zip/pwned/clara/protected.txt PKZIP Encr: 2b chk, TS_chk, cmplen=28, decmplen=16, crc=239F7473 ts=3383 cs=3383 type=0
```
Using john and the recommanded `rockyou.txt` wordlist, we crack the hash.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt clara.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
No password hashes left to crack (see FAQ)
```
We reveal the cracked ZIP password using `john --show` and password is `pass123`:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ john --show clara.hash                                     
protected.zip/pwned/clara/protected.txt:pass123:pwned/clara/protected.txt:protected.zip::protected.zip

1 password hash cracked, 0 left
```
Now, we unzip the file to get the contents, which will contain `frida`'s password.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ unzip protected.zip
Archive:  protected.zip
[protected.zip] pwned/clara/protected.txt password: 
 extracting: pwned/clara/protected.txt  
```
Reading the file reveals the password for user `frida`.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ cat pwned/clara/protected.txt  
Ed4ErEUJEaMcXli
```
Using the password from the text file, we switch back to the venus machine and `su` to `frida`.
```bash
clara@venus:~$ su - frida
Password: 
frida@venus:~$ id ; whoami
uid=1019(frida) gid=1019(frida) groups=1019(frida)
frida
```
Finally, we read the flag.

## Key command
`scp -P 5000 clara@venus.hackmyvm.eu:~/protected.zip .`
`zip2john protected.zip > clara.hash`
`john --wordlist=/usr/share/wordlists/rockyou.txt clara.hash`
`john --show clara.hash`
`unzip protected.zip`

***You are welcome!***
