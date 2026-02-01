# 0x36
This write-up explains the steps taken to complete mission 0x36, starting from user `gloria` and escalating to `alora`.

## Mission 
As usual, read the objective first:
```bash
gloria@venus:~$ cat mission.txt 
################
# MISSION 0x36 #
################

## EN ##
User alora likes drawings, that's why she saved her password as ... 
```

## Method of solving
We checked the home directory and found a file named `image`. Unlike previous levels where images were binary file (like `.png`), this one was identified as text.
```bash
gloria@venus:~$ ls         
flagz.txt  image  mission.txt
gloria@venus:~$ file image 
image: ASCII text
```
When we displayed the content of the file using `cat`, it revealed a **QR Code** rendered entirely in **ASCII art** using `#` characters and spaces.
```bash
gloria@venus:~$ cat image 

##########################################################
##########################################################
##########################################################
##########################################################
########              ##########  ##              ########
########  ##########  ##    ##  ####  ##########  ########
########  ##      ##  ##  ##  ######  ##      ##  ########
########  ##      ##  ####  ########  ##      ##  ########
########  ##      ##  ##        ####  ##      ##  ########
########  ##########  ##        ####  ##########  ########
########              ##  ##  ##  ##              ########
########################  ####  ##########################
########    ##  ####    ####  ##  ##      ##    ##########
############    ######  ##    ##      ##          ########
########    ##    ##  ##  ##            ####  ##  ########
##############      ##  ##    ######  ##    ####  ########
############    ##      ##  ########    ##  ##  ##########
########################    ####    ##  ##  ####  ########
########              ##    ####            ##  ##########
########  ##########  ######  ##########  ####  ##########
########  ##      ##  ####  ##      ######        ########
########  ##      ##  ##    ##  ######  ##  ####  ########
########  ##      ##  ####          ##    ##  ##  ########
########  ##########  ##      ####  ##  ##################
########              ##  ##                    ##########
##########################################################
##########################################################
##########################################################
##########################################################
```
### The solution
**Using phone to scan**: Simply shrinking the terminal font size and scanning the screen with a smartphone QR reader.
**Explanation:**

- **ASCII Art QR Code:** A creative way to store data in a text-only environment. Each # represents a dark module and each space represents a light module.
- **Scanning:** Most modern QR scanners are robust enough to recognize the pattern even when represented by text characters instead of pixels.
- **The Findings:** Scanning the ASCII "drawing" successfully decoded the string hidden within the modules `mhrTFCoxGoqUxtw`

Switching to user `alora` and get the flag.
```bash
gloria@venus:~$ su - alora
Password: 
alora@venus:~$ id ; whoami
uid=1037(alora) gid=1037(alora) groups=1037(alora)
alora
```
 
## Key command
`cat image`

***You are welcome!***
