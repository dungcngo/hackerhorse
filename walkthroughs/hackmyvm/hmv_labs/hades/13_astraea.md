# 0x13
This write-up explains the steps taken to complete mission 0x13 on hades@hackmyvm.eu, starting from user `astraea` and escalating to `atalanta`.

## Mission
This mission clue for this level was found within retrieved from the FTP server:
```bash
asteria@hades:/tmp/ftpp$ cat mission.txt 
################
# MISSION 0x13 #
################

## EN ##
The user atalanta has done something with our account. 
```

## Method of solving
After discovering the password for `astraea` in the previous challenge, we encountered a block when trying to log in via SSH. The system allowed the password but immediately terminated the connection.

### Step 1: SSH Attempt (Connection closed)
Standard shell access was restricted for this user, likely through a configuration like `/usr/sbin/nologin`.
```bash
asteria@hades:~$ ssh astraea@localhost
...
astraea@localhost's password: 
^KssHQIAFsxUamecyXIUk^
Connection to localhost closed.
```

### Step 2: Preparing a Writable Worksapce.
When using FTP to download files with `mget`, the FTP client tries to save the file into our current local directory. Because the current directory(`/pwned/asteria`) was not writable, we had to create a temporary workspace in `/tmp`.
```bash
asteria@hades:~$ mkdir /tmp/ftpp
asteria@hades:~$ cd /tmp/ftpp
```

### Step 3: FTP Login and File Retrieval
From the new writable directory, we connected to the local FTP server.
```bash
asteria@hades:/tmp/ftpp$ ftp astraea@localhost
Trying [::1]:21 ...
Connected to localhost.
220 (vsFTPd 3.0.3)
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> 
```
We use `mget *` to download the targer user's password file, this mission details, and the flag.
```bash
ftp> ls
229 Entering Extended Passive Mode (|||34622|)
150 Here comes the directory listing.
-rw-r-----    1 0        2004           21 Apr 05  2024 atalanta.txt
-rw-r-----    1 0        2004           22 Apr 05  2024 flagz.txt
-rw-r-----    1 0        2004          181 Apr 05  2024 mission.txt
226 Directory send OK.
ftp> mget *
mget atalanta.txt [anpqy?]? yes
229 Entering Extended Passive Mode (|||22649|)
150 Opening BINARY mode data connection for atalanta.txt (21 bytes).
100% |***********************************|    21       81.05 KiB/s    00:00 ETA
226 Transfer complete.
21 bytes received in 00:00 (19.75 KiB/s)
mget flagz.txt [anpqy?]? yes
229 Entering Extended Passive Mode (|||8695|)
150 Opening BINARY mode data connection for flagz.txt (22 bytes).
100% |***********************************|    22      111.89 KiB/s    00:00 ETA
226 Transfer complete.
22 bytes received in 00:00 (23.00 KiB/s)
mget mission.txt [anpqy?]? yes
229 Entering Extended Passive Mode (|||11281|)
150 Opening BINARY mode data connection for mission.txt (181 bytes).
100% |***********************************|   181      782.11 KiB/s    00:00 ETA
226 Transfer complete.
181 bytes received in 00:00 (223.46 KiB/s)
ftp> exit
221 Goodbye.
```

Once the transfer was complete, we exited FTP and read the password  for the next level.
```bash
asteria@hades:/tmp/ftpp$ cat atalanta.txt 
mUcSNQlaXtwSvGcgeTYZ
```
Using this retrieved password, we successfully established a full SSH sesssion as `atalanta`.
```bash
asteria@hades:/tmp/ftpp$ ssh atalanta@localhost
...
atalanta@hades:~$ id; hostname
uid=2005(atalanta) gid=2005(atalanta) groups=2005(atalanta)
hades
```
### Explanation
- **Restricted Shells**: Users can be barred from SSH but still granted access to other services like FTP for file management.
- **FTP Local Permissions**: A common mistake when using the `ftp` command is forgetting that you must have write permissions in the directory where you launched the FTP client. Without a writable local path, `get` or `mget` command will fail.

## Key command
`mkdir /tmp/ftpp`

`ftp astraea@localhost`

`wget *`

***You are welcome!***
