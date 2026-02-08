# Bandit00: Log Into Remote Server

## Level Description
This was the starting point of the bandit wargame. The goal seemed straighforward: log into a remote server using SSH. The host was `bandit.labs.overthewire.org`, port `2220`. They even gave me the username and password - both were `bandit0`.

## The Process
We need to use SSH, but there was one small twist—port 2220. SSH, by default, connects on port 22, so we know we have to explicitly specify the port this time.

We fire up our terminal, type the command:
```bash
┌──(root㉿kali)-[/home/dungcngo]
└─# ssh bandit0@bandit.labs.overthewire.org -p 2220
```
When prompted for the password, we entered `bandit0`.

## What we learned
- **Using SSH**: we got hands-on experience connecting to a remote server.
- **Specifying Ports**: By default, SSH uses port 22, but for this challenge, we learned how to connect to a custom port with the `-p` flag.
- **Basic Authentication**: It's always good to know how to log in with just a username and password.

***You are welcome!***
