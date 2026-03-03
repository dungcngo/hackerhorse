# Bandit22

## Level Description
A program is running automatically at regular intervals from `cron`, the time-based job scheduler. Look in `/etc/cron.d/` for the configuration and see what command is being executed.

## Method of Solving
We log into `bandit21` server. We list the contents of the home directory:
```bash
bandit21@bandit:~$ ls -la
total 24
drwxr-xr-x   2 root     root     4096 Oct 14 09:26 .
drwxr-xr-x 150 root     root     4096 Oct 14 09:29 ..
-rw-r--r--   1 root     root      220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root     root     3851 Oct 14 09:19 .bashrc
-r--------   1 bandit21 bandit21   33 Oct 14 09:26 .prevpass
-rw-r--r--   1 root     root      807 Mar 31  2024 .profile
```
The level description mentioned `cron`, the time-based job scheduler. My first move is to investigate the `/etc/cron.d` directory, where cron jobs are often configured.

We navigated there:
```bash
bandit21@bandit:~$ cd /etc/cron.d/
bandit21@bandit:/etc/cron.d$ ls
behemoth4_cleanup  cronjob_bandit23  leviathan5_cleanup    sysstat
clean_tmp          cronjob_bandit24  manpage3_resetpw_job
cronjob_bandit22   e2scrub_all       otw-tmp-dir
```
The file `cronjob_bandit22` caught my eye. It had to be the key.

We open the `cronjob_bandit22` file to see what it was up to:
```bash
bandit21@bandit:/etc/cron.d$ cat cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```
This important that a script, `/usr/bin/cronjob_bandit22.sh`, was running every minute as the `bandit22` user. The `&> /dev/null` part ensured that any output was discarded, making it harder to detect. We inspect the script to understand its  purpose:
```bash
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```
Here's what it did:
- It changed the permissions of a file in `/tmp/` to `644`, making it readable by everyone.
- It wrote the password for `bandit22` (`/etc/bandit_pass/bandit22`) into this file.

The cron job was essentially leaking the password into a temporary file, but only for a brief moment. Since the cron job ran as the `bandit22` user, it had the necessary permissions to write the password to the temporary file. All we had to do was read the file before it was overwritten or deleted.

We check the contents of the file:
```bash
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
```
There is the password for `bandit22`.

## Key commnad
`cd /etc/cron.d/`

`cat cronjob_bandit22`

`cat /usr/bin/cronjob_bandit22.sh`

***You are welcome!***
