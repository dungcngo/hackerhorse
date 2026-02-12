# Bandit15

## Level Description
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost. 

## Method of Solving
We start by logging into the server with the credentials form the previous level.
```bash
┌──(root㉿kali)-[/home/…/Workspace/walkthroughs/overthewire/bandit]
└─# ssh bandit14@bandit.labs.overthewire.org -p 2220   
```
Running `ls` command in the home directory revealed no files. This meant the solution wasn't about reading a file but likely involved interacting with the system differently. Since the challenge description mentioned a port, we suspected this was a networking challenge.
```bash
bandit14@bandit:~$ ls
```

The instructions tell us we need to send the password for the current level to localhost port 30000. We can do so with the netcat program:
```bash
bandit14@bandit:~$ nc localhost 30000
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS         <--- This is password of `bandit14`
Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo         <--- This is password of `bandit15`
```
We can also do this as a one-liner if we use the echo and a pipe:
```bash
bandit14@bandit:~$ echo 'MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS' | nc localhost 30000
Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```
Alternatively, we can also use `telnet` to connect to port 30000 on localhost.
```bash
bandit14@bandit:~$ telnet localhost 30000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

Connection closed by foreign host.
```
**Understanding `nc` and `telnet`**:
- `nc` (netcat) is a flexiblle networking tool for sending and receiving raw data over TCP/UDP. It requires precise options and it often used for scripting or penetratrion testing.
- `telnet` is a simpler tool meant for interacting with text-based over a network. Unlike `nc`, it assumes the five number is the destination port, making it more user-friendly for this challenge.

## What we learned
- How to connect to a remote service using `telnet`, `nc`.
- The difference between `nc` and `telnet`.

## Key command
`nc localhost 30000`

`telnet localhosst 30000`

***You are welcome!***
