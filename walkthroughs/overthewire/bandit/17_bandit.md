# Bandit17	

## Level Description
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range `31000 to 32000`. First find out which of these ports have a server listening on them. 

Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

## Method of Solving
We started by connecting to the `bandit16` server using SSH. After entering the password from the previous level, we were in.

The challenge hinted that the password was hidden behind one of the ports in the range 31000-32000. We used `nmap` to scan these ports.
```bash
bandit16@bandit:~$ nmap -p31000-32000 -vv -sV localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-03-03 07:23 UTC
NSE: Loaded 46 scripts for scanning.
Initiating Ping Scan at 07:23
Scanning localhost (127.0.0.1) [2 ports]
Completed Ping Scan at 07:23, 0.00s elapsed (1 total hosts)
Initiating Connect Scan at 07:23
Scanning localhost (127.0.0.1) [1001 ports]
Discovered open port 31960/tcp on 127.0.0.1
Discovered open port 31518/tcp on 127.0.0.1
Discovered open port 31790/tcp on 127.0.0.1
Discovered open port 31691/tcp on 127.0.0.1
Discovered open port 31046/tcp on 127.0.0.1
Completed Connect Scan at 07:23, 0.02s elapsed (1001 total ports)
Initiating Service scan at 07:23
Scanning 5 services on localhost (127.0.0.1)
Service scan Timing: About 20.00% done; ETC: 07:27 (0:02:40 remaining)
Completed Service scan at 07:26, 159.87s elapsed (5 services on 1 host)
NSE: Script scanning 127.0.0.1.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 07:26
Completed NSE at 07:26, 0.02s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 07:26
Completed NSE at 07:26, 0.03s elapsed
Nmap scan report for localhost (127.0.0.1)
Host is up, received conn-refused (0.00011s latency).
Scanned at 2026-03-03 07:23:47 UTC for 160s
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE     REASON  VERSION
31046/tcp open  echo        syn-ack
31518/tcp open  ssl/echo    syn-ack
31691/tcp open  echo        syn-ack
31790/tcp open  ssl/unknown syn-ack
31960/tcp open  echo        syn-ack
```
One of the ports is sevring SSL that ports is 31518 and 31790, so we send that port the password.
```bash
bandit16@bandit:~$ echo 'kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx' | openssl s_client -quiet -connect localhost:31790
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```
We receive a SSH private key as the response, so we'll need to create a private  key for the next level.

## Key command
`nmap -p31000-32000 -sV localhost`

`echo 'password_bandit16' | openssl s_client -quiet -connect localhost:31790`

***You are welcome!***
