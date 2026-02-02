# 0x45
This write-up explains the steps taken to complete mission 0x45, starting from user `karla` and escalating to `denise`.

## Mission
As usual, read the mission first:
```bash
karla@venus:~$ cat mission.txt 
################
# MISSION 0x45 #
################

## EN ##
User denise has saved her password in the image.
```

## Method of solving
In the home directory, we found a JPEG image named `yuyu.jpg`.
```bash
karla@venus:~$ ls -la
total 68
drwxr-x--- 2 root  karla  4096 Apr  5  2024 .
drwxr-xr-x 1 root  root   4096 Apr  5  2024 ..
-rw-r--r-- 1 karla karla   220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 karla karla  3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 karla karla   807 Apr 23  2023 .profile
-rw-r----- 1 root  karla    31 Apr  5  2024 flagz.txt
-rw-r----- 1 root  karla   176 Apr  5  2024 mission.txt
-rw-r----- 1 root  karla 32946 Apr  5  2024 yuju.jpg
```
Since the password was reportedly "in the image", but not necessarily visible in the picture itself, we checked the file's **metadata**. Metadata contains hidden information about the file, such as the creator, the date if was taken, or custom comments, we used `exiftool` to inspect these hidden tags.
```bash
karla@venus:~$ exiftool yuju.jpg 
ExifTool Version Number         : 12.57
File Name                       : yuju.jpg
Directory                       : .
File Size                       : 33 kB
File Modification Date/Time     : 2024:04:05 06:28:46+00:00
File Access Date/Time           : 2024:04:05 06:28:46+00:00
File Inode Change Date/Time     : 2024:04:05 06:29:46+00:00
File Permissions                : -rw-r-----
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 96
Y Resolution                    : 96
Exif Byte Order                 : Big-endian (Motorola, MM)
Artist                          : sML
Date/Time Original              : 2021:11:01 10:34:51
Create Date                     : 2021:11:01 10:34:51
Sub Sec Time Original           : 95
Sub Sec Time Digitized          : 95
XP Author                       : sML
Padding                         : (Binary data 2060 bytes, use -b option to extract)
XMP Toolkit                     : Image::ExifTool 12.16
About                           : pFg92DpGucMWccA
Creator                         : sML
Image Width                     : 442
Image Height                    : 463
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 442x463
Megapixels                      : 0.205
Create Date                     : 2021:11:01 10:34:51.95
Date/Time Original              : 2021:11:01 10:34:51.95
```
The string found in the `About` field served as the password for the next user.
Using the identified password, we switch to user `denise` and get the flag.
```bash
karla@venus:~$ su - denise
Password: 
denise@venus:~$ id ; whoami
uid=1046(denise) gid=1046(denise) groups=1046(denise)
denise
```

## Key command
`exiftool yuju.jpg`
`About: password`

***You are welcome!***
