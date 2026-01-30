# 0x21
This write-up explains the steps taken to complete mission 0x21, starting from user `iris` and escalating to `eloise`.

## Mission
As usual, we read the objective first:
```bash
iris@venus:~$ cat mission.txt 
################
# MISSION 0x21 #
################

## EN ##
User eloise has saved her password in a particular way. 
```

## Method of solving
Look up what's the file in the home directory. We will find `eloise` file.
```bash
iris@venus:~$ cat eloise 
/9j/4AAQSkZJRgABAQEAYABgAAD/4RDSRXhpZgAATU0AKgAAAAgABAE7AAIAAAAEc01MAIdpAAQA
AAABAAAISpydAAEAAAAIAAAQwuocAAcAAAgMAAAAPgAAAAAc6gAAAAgAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA                 ....................................
oAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiig
AooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAP
/9k=
```
We try to decode it using `base64` and got:
```bash
iris@venus:~$ cat eloise | base64 -d
����JFIF``���ExifMM;sML�J���
                           >������85��85�
                                       �2021:11:10 10:18:032021:11:10 10:18:03sML��
.............
```
It looks like a JPG file or something. We can use `file` command to determine the file type.
```bash
iris@venus:~$ cat eloise | base64 -d | file -
/dev/stdin: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=4], baseline, precision 8, 394x102, components 3
```
Now, the challenge was to get that image off the server and onto our machine, where we can actually view it. We saved the decoded bytes into a temporary file.
```bash
iris@venus:~$ cat eloise | base64 -d > /tmp/image.jpg
```
Then, back on our local shell, we connected over the network. Using `scp` on port 5000, we pulled that mysterious file onto my local drive. 
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ scp -P 5000 iris@venus.hackmyvm.eu:/tmp/image.jpg .
                 ......
iris@venus.hackmyvm.eu's password: 
image.jpg                                     100%   13KB  21.3KB/s   00:00    
```
Now, just open that file by using `xdg-open` command.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ xdg-open image.jpg   
```
Loggin using that password and verify user `eloise`, go get the flag.
```bash
iris@venus:/tmp$ su - eloise
Password: 
eloise@venus:~$ id ; whoami
uid=1022(eloise) gid=1022(eloise) groups=1022(eloise)
eloise
```

## Key command
`cat eloise | base64 -d | file -`

`cat eloise | base64 -d > /tmp/image.jpg`

`xdg-open image.jpg`


***You are welcome!***
