# 0x30
This write-up explains the steps taken to complete mission 0x30, starting from user `nina` and escalating to `kira`.

## Mission
As usual, we read the mission first:
```bash
nina@venus:~$ cat mission.txt 
################
# MISSION 0x30 #
################

## EN ##
The user kira is hidding something in http://localhost/method.php
```

## Method of solving
Checking the home directory and seeing the usual mission file. The hint explicitly points to a PHP file on the local web server, suggesting that we need to interact with it using different __HTTP Methods__.
```bash
nina@venus:~$ ls -la
total 32
drwxr-x--- 2 root nina 4096 Apr  5  2024 .
drwxr-xr-x 1 root root 4096 Apr  5  2024 ..
-rw-r--r-- 1 nina nina  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 nina nina 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 nina nina  807 Apr 23  2023 .profile
-rw-r----- 1 root nina   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root nina  197 Apr  5  2024 mission.txt
```
When we accessed the URL normally (GET) or used common methods like **POST**, the server responded with "I don't like this method!
```bash
nina@venus:~$ curl -X GET http://localhost/method.php

I dont like this method! 
```
This is a classic CTF hint to "fuzz" or ronate through other HTTP verbs like **PUT**, **PATCH**, or **DELETE**.

I used `curl` with the `-x` flag to manually specify the request method:
```bash
nina@venus:~$ curl -X PUT http://localhost/method.php

tPlqxSKuT4eP3yr 
```
**Explanation:**
- `HTTP Methods (Verbs)`: Most web traffic user **GET** (to read) or **POST** (to submit). However, developers can program a server to respond differently to other verbs like **PUT** (to replace) or **PATCH** (to modify).
- `curl -X [METHOD]`: This command forces `curl` to use a specific HTTP verb.
- The **PUT**  request revealed a string that looked like a password.

Using the password captured, logged in as `kira` and verify it, get the flag.
```bash
nina@venus:~$ su - kira
Password: 
kira@venus:~$ id ; whoami
uid=1031(kira) gid=1031(kira) groups=1031(kira)
kira
```

## Key command
`curl -X PUT -vv http://localhost/method.php`

***You are welcome!***
