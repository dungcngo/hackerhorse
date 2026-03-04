# Bandit27

## Level Description
Good job getting a shell! Now hurry and grab the password for `bandit27`!

## Method of Solving
Because we already inside the `bandit26` and we've mentioned what have to do in the level description. Check what's inside the home director:
```bash
bandit26@bandit:~$ ls
bandit27-do  text.txt
```
Check the permissions of `bandit27-do`:
```bash
bandit26@bandit:~$ ls -l bandit27-do 
-rwsr-x--- 1 bandit27 bandit26 14884 Oct 14 09:26 bandit27-do
```
The `s` in `rws` shows that this is a SUID binary - it runs with the permissions of the file owner, which is `bandit27`. That's mean if we run it, it runs as if we're `bandit27`.

Run the binary file to print the password:
```bash
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
```

## Key command

***You are welcome!***
