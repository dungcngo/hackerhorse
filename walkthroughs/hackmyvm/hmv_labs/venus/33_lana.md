# 0x33
This write-up explains the steps taken to complete mission 0x33, starting from user `lana` and escalating to `noa`.

## Mission
As always, read the objective first:
```bash
lana@venus:~$ cat mission.txt 
################
# MISSION 0x33 #
################

## EN ##
The user noa loves to compress her things.
```

## Method of solving
We checked the home directory and found it failed. We then used the `file` command to determine the actual file type, which revealed it was a **POSIX tar archive**, not a gzip or zip file.
```bash
lana@venus:~$ file zip.gz 
zip.gz: POSIX tar archive (GNU)
```

Since we didn't have write permissions in the current folder, we created a temporary workspace in `/tmp/`, copied the archive there, and extract it using `tar`.
```bash
lana@venus:~$ mkdir /tmp/lana1/
lana@venus:~$ cp zip.gz /tmp/lana1/
lana@venus:~$ cd /tmp/lana1/
lana@venus:/tmp/lana1$ tar -xf zip.gz
```
Inside the extracted folder structure, we found the password:
```bash
lana@venus:/tmp/lana1$ ls
pwned  zip.gz
lana@venus:/tmp/lana1$ cd pwned/
lana@venus:/tmp/lana1/pwned$ ls
lana
lana@venus:/tmp/lana1/pwned$ cd lana/
lana@venus:/tmp/lana1/pwned/lana$ ls
zip
lana@venus:/tmp/lana1/pwned/lana$ cat zip
9WWOPoeJrq6ncvJ
```
Using the password, switching to user `noa` and verify it get the flag.
```bash
lana@venus:/tmp/lana1/pwned/lana$ su - noa
Password: 
noa@venus:~$ id ; whoami
uid=1034(noa) gid=1034(noa) groups=1034(noa)
noa
```

## Key command
`tar -xvf zip.gz`

***You are welcome!***

