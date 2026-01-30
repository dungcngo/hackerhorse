# 0x10
This write-up explains the steps taken to complete mission 0x10, starting from user `isla` and escalating to `violet`.

## Mission
As always, read the objective first:
```bash
isla@venus:~$ cat mission.txt 
################
# MISSION 0x10 #
################

## EN ##
The password of the user violet is in the line that begins with a9HFX (these 5 characters are not part of her password.). 
```

## Method of solving
In the home directory, there is a file named `passy`, when we look into it:
```bash
isla@venus:~$ cat passy 
gRfsUwzARHdRSUOrXbvc
vTLXwbzOnYzjPRRzshdN
lZUtoGkBCVcfSzRpbAFA
WnmzolwEtyoWYPprSvHf
kOAxfgMrNHMTdrlyrMVu
     .....
JHbLHzEGnwOEffvUazwF
ndocUrxRYCPIEftpaxHD
nRcIAFUAMkaAjYHBIRNv
NyJUCiEupUYOOMyIprOf
```
There are so many lines inside, it's not efficient to look at it line after line.
The hint mentioned the password is in the line that begins with `a9HFX` but these 5 characters are not part of the password.
Use grep command to get the line:
```bash
isla@venus:~$ grep "a9HFX" passy
WKINVzNQLKLDVAca9HFX
dWeFra9HFXzNQLKLDVAc
kfRgNa9HFXzNQLKLDVAc
zNQa9HFXfEtrgLKLDVAc
WKINVzNQLa9HFXDwErfc
WKINVa9HFXzDcceWeTfd
a9HFXWKINVzNQLKLDVAc
```
Or, we can use `sed` so that only lines starting with `a9HFX` are processed, the string is removed, and the resulting line is printed.
```bash
isla@venus:~$ sed -n 's/^a9HFX//p' passy
WKINVzNQLKLDVAc
```

## Key command
`sed -n 's/^a9HFX//p' passy`

`grep "a9HFX" passy`

***You are welcome!***

