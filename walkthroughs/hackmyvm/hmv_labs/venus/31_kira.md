# 0x31
This write-up explains the steps taken to complete mission 0x31, starting from user `kira` and escalating to `veronica`.

## Mission
As usual, we read the objective first:
```bash
kira@venus:~$ cat mission.txt 
################
# MISSION 31 #
################

## EN ##
The user veronica visits a lot http://localhost/waiting.php
```

## Method of solving
We checked the home directory and identified the next target URL. Based on the previous levels, we knew we needed to interact with the local web server again.
```bash
kira@venus:~$ ls -la
total 32
drwxr-x--- 2 root kira 4096 Apr  5  2024 .
drwxr-xr-x 1 root root 4096 Apr  5  2024 ..
-rw-r--r-- 1 kira kira  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 kira kira 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 kira kira  807 Apr 23  2023 .profile
-rw-r----- 1 root kira   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root kira  191 Apr  5  2024 mission.txt
```
When we first accessed the page with a standard `curl` request, the server gave me a specific requirement: `Im waiting for the user-agent PARADISE`.
```bash
kira@venus:~$ curl http://localhost/waiting.php

Im waiting for the user-agent PARADISE. 
```
To solve this, I needed to modify the **User-Agent** header in my HTTP request. The **User-Agent** string tells the server what kinh of browser or tool is visiting the site.

We attempted to use `-H`:
```bash
kira@venus:~$ curl -H "User-Agent: PARADISE" http://localhost/waiting.php

QTOel6BodTx2cwX 
```
With the password captured, logged in as `veronica` and verify it, get the flag.
```bash
kira@venus:~$ su - veronica
Password: 
veronica@venus:~$ id ; whoami
uid=1032(veronica) gid=1032(veronica) groups=1032(veronica)
veronica
```

## Key command
`curl -A "PARADISE" http://localhost/waiting.php`

`curl -H "User-Agent: PARADISE" http://localhost/waiting.php`
	
***You are welcome!***
