# Bandit11

## Level Description
The password for this next level was stored in the file named `data.txt`, which contains `base64` encoded data.

## Method of Solving
Upon logging in as `bandit10`, us usual check what's the contents of home directory and it's file type if there it is:
```bash
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ file data.txt 
data.txt: ASCII text
```
To determine how long the line of text would be, we ran this command:
```bash
bandit10@bandit:~$ wc -l data.txt 
1 data.txt
```
Let's view the contents of this file:
```bash
bandit10@bandit:~$ cat data.txt 
VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==
```
It returns a string with `base64` encoded data. We could use the `base64` command to encode or decode.

We could use `-d` option with the file naem as an argument to solve this challenge.
```bash
bandit10@bandit:~$ base64 -d data.txt 
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```
The password for the next level appeared!

## What we learned 
- **Understanding Bae64 Encoding**: Recognized that the file’s contents were Base64-encoded text.
- **Decoding Base64 with `base64 -d`** - Used the `base64 -d` command to decode the text and reveal the password.

## Key command
`base64 -d data.txt`

***You are welcome!***
