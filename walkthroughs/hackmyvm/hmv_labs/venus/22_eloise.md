# 0x22
This write-up explains the steps taken to complete mission 0x22, starting from user `eloise` and escalating to `lucia`.

## Mission
As usual, read the mission first:
```bash
eloise@venus:~$ cat mission.txt 
################
# MISSION 0x22 #
################

## EN ##
User lucia has been creative in saving her password.
```

## Method of solving
Checking the files in the home directory, we can see a file named `hi`.
```bash
eloise@venus:~$ ls 
flagz.txt  hi  mission.txt
```
When viewing the content of `hi`, it appears to be a Hexdump.
```bash
eloise@venus:~$ cat hi
00000000: 7576 4d77 4644 5172 5157 504d 6547 500a
```
To read the actual password, we need to revert the hex dump into plain text (ASCII). We use `xxd` with the `-r` (revert) flag and the `-p` (plain hexdump) flag.
```bash
eloise@venus:~$ cat hi | xxd -r -p
uvMwFDQrQWPMeGP
```
With the password, switch to the user `lucia`. Verify it and get the flag.
```bash
eloise@venus:~$ su - lucia
Password: 
lucia@venus:~$ id ; whoami
uid=1023(lucia) gid=1023(lucia) groups=1023(lucia)
lucia
```

## Key command
`cat hi | xxd -r -p`

***You are welcome!***
