# 0x37
This write-up explains the steps taken to complete mission 0x37, starting from user `alora` and escalating to `julie`.

## Mission 
As usual, read the mission first:
```bash
alora@venus:~$ cat mission.txt 
################
# MISSION 0x37 #
################

## EN ##
The user julie has created an iso with her password.
```

## Method of solving
In the home directory, we found a large file named `music.iso`. Verification with `file` command confirmed it was an ISO 9660 filesystem image.
```bash
alora@venus:~$ ls 
flagz.txt  mission.txt  music.iso
alora@venus:~$ file music.iso 
music.iso: ISO 9660 CD-ROM filesystem data 'CDROM'
```
Initially, we try to `mount` the image to view its contents, but since we lack `sudo` privileges and don't  have the `7z` tool installed to extract it, we need a way to read the data within the binary file directly.

Since an ISO is a raw image of a disk and the password was stored in a text file (`music.txt`) inside it, the text remained uncompressed and readable. We use the `strings` command to scan the binary file for printable character sequences.
```bash
alora@venus:~$ strings music.iso 
CD001
LINUX                           CDROM                           
                                                                                                                                                                                                                                                                                                                                                                                                GENISOIMAGE ISO 9660/HFS FILESYSTEM CREATOR (C) 1993 E.YOUNGDALE (C) 1997-2006 J.PEARSON/J.SCHILLING (C) 2006-2007 CDRKIT TEAM                                                                                                                 2024040506284600
2024040506284600
0000000000000000
2024040506284600
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
CD001
MUSIC.ZIP;1RR
music.zipPX$
RRIP_1991ATHE ROCK RIDGE INTERCHANGE PROTOCOL PROVIDES SUPPORT FOR POSIX FILE SYSTEM SEMANTICSPLEASE CONTACT DISC PUBLISHER FOR SPECIFICATION SOURCE.  SEE PUBLISHER IDENTIFIER IN PRIMARY VOLUME DESCRIPTOR FOR CONTACT INFORMATION.
pwned/alora/music.txtUT	
sjDf4i2MSNgSvOv           <----- This is the password
pwned/alora/music.txtUT
```
Successfully find the hidden password, switching to user `julie` and get the flag.
```bash
alora@venus:~$ su - julie
Password: 
julie@venus:~$ id ; whoami
uid=1038(julie) gid=1038(julie) groups=1038(julie)
julie
```

## Key command
`strings music.iso`
or 
`scp -P 5000 alora@venus.hackmyvm.eu:/pwned/alora/music.iso .`
`xdg-open music.iso`

***You are welcome***
