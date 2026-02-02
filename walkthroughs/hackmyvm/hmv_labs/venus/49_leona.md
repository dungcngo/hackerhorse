# 0x49
This write-up explains the steps taken to complete mission 0x49, starting from user `leona` and escalating to `ava`.

## Mission
As usual, read the mission first:
```bash
leona@venus:~$ cat mission.txt 
################
# MISSION 0x49 #
################

## EN ##
User ava plays a lot with the DNS of venus.hmv lately... 
```

## Method of solving
We initially tried to query the local DNS server using standard tools like `nslookup` and `dig` against `localhost`. However, the server returned `SERVFAIL`, suggesting it was either misconfigured or restricted.
```bash
leona@venus:~$ nslookup -type=txt venus.hmv localhost
;; Got SERVFAIL reply from 127.0.0.1, trying next server
Server:		localhost
Address:	127.0.0.1#53

** server can't find venus.hmv: SERVFAIL
```

Since I couldn't get the information via a network query, we looked for the DNS configuration files directly on the system. On Linux, the **BIND** (Berkely Internet Name Domain) service stores its zone data in `/etc/bind/`.

By navigating to that directory, we found the zone file the `venus.hmv` domain.
```bash
leona@venus:~$ cd /etc/bind
leona@venus:/etc/bind$ cat db.venus.hmv

;
; BIND data file for local loopback interface
;
    604800
@       IN      SOA     ns1.venus.hmv. root.venus.hmv. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL

;@      IN      NS      localhost.
;@      IN      A       127.0.0.1
;@      IN      AAAA    ::1
@       IN      NS      ns1.venus.hmv.

;IP address of Name Server

ns1     IN      A       127.0.0.1
ava IN      TXT     oCXBeeEeYFX34NU
```
Using the password, we switch to user `ava` and get the flag.
```bash
leona@venus:/etc/bind$ su - ava
Password: 
ava@venus:~$ id ; whoami
uid=1050(ava) gid=1050(ava) groups=1050(ava)
ava
```

## Key command
`cat /etc/bind/db.venus.hmv`

***You are welcome!***
