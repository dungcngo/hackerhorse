# 0x09
This write-up explains the steps taken to complete mission 0x09, starting from user `victoria` and escalating to `isla`.

## Mission
As usual, read the objective:
```bash
victoria@venus:~$ cat mission.txt 
################
# MISSION 0x09 #
################

## EN ##
The user isla has left her password in a zip file.
```

## Method of solving
In the home directory, there is a zip file like what the hint said about. However, because we don't have permision to create something in the home directory, we can't extract the file.
Then, we create a temporary directory under `/tmp` and copy that file into it:
```bash
victoria@venus:~$ mkdir /tmp/123456 
victoria@venus:~$ cp ./passw0rd.zip /tmp/123456
```
Move to `/tmp/123456` and extract the zip file here:
```bash
victoria@venus:~$ cd /tmp/123456
victoria@venus:/tmp/123456$ unzip passw0rd.zip 
Archive:  passw0rd.zip
 extracting: pwned/victoria/passw0rd.txt  
```
Print the password:
```bash
victoria@venus:/tmp/123456$ cat pwned/victoria/passw0rd.txt 
D3XTob0FUImsoBb
```
Verify it by switching to user `isla` and read the flag:
```bash
victoria@venus:/tmp/123456$ su - isla
Password: 
GOGETA SSJ6 
tornillo --->
isla@venus:~$ id ; whoami
uid=1010(isla) gid=1010(isla) groups=1010(isla)
isla
```

## Key command
`unzip passw0rd.zip`

***You are welcome!***
