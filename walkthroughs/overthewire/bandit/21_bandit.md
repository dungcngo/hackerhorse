# Bandit21

## Level Description
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (`bandit20`). If the password is correct, it will transmit the password for the next level (`bandit21`).

## Method of Solving
We log into the `bandit20` server using SSH. We list the contents of the home directory:
```bash
bandit20@bandit:~$ ls -la
total 36
drwxr-xr-x   2 root     root      4096 Oct 14 09:26 .
drwxr-xr-x 150 root     root      4096 Oct 14 09:29 ..
-rw-r--r--   1 root     root       220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root     root      3851 Oct 14 09:19 .bashrc
-rw-r--r--   1 root     root       807 Mar 31  2024 .profile
-rwsr-x---   1 bandit21 bandit20 15608 Oct 14 09:26 suconnect
```
This revealed a single file `suconnect`. The `s` in the permissions (`rws`) indicates that this is a `setuid binary`. This means the binary runs with the privileges of the file owner (`bandit21`), not the user executing it (`bandit20`).

We run the `suconnect` binary to understand its usage:
```bash
bandit20@bandit:~$ ./suconnect 
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.
```
To interact with the `suconnect` binary, we need to set up a listener on a specific port. We use `nc` to listen on port `1234` and send the `bandit20` password.
```bash
bandit20@bandit:~$ echo "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -lnvp 1234 &
[1] 18
bandit20@bandit:~$ Listening on 0.0.0.0 1234
```
This command runs `nc` in the background, listening on port `1234` and sending the password when a connection is made.

While the listener was running, we execute the `suconnect` binary to connect to same port:
```bash
bandit20@bandit:~$ ./suconnect 1234
Read: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
Password matches, sending next password
```
The output confirmed that the password was correct.
```bash
bandit20@bandit:~$ Listening on 0.0.0.0 1234
Connection received on 127.0.0.1 40166
EeoULMCra2q0dSkYj561DX7s1CpBuOBt     <---- This is the password of bandit21
```

## Key command
`echo "password_bandit20" | nc -nlvp 1234 &`

`./suconnect 1234`

***You are welcome!***
