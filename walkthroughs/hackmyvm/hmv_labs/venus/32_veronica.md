# 0x32
This write-up explains the steps taken to complete mission 0x31, starting from user `veronica` and escalating to `lana`.

## Mission
```bash
veronica@venus:~$ cat mission.txt 
################
# MISSION 0x32 #
################

## EN ##
The user veronica uses a lot the password from lana, so she created an alias.
```

## Method of solving
The clue specifically about how the user interacts with the shell. An **alias** is a shortcut for a command or a string that a user can define in their session.

To find the shortcut `veronica` created, we used the `alias` command, which lists all active aliases for the current user.
```bash
veronica@venus:~$ alias
alias lanapass='UWbc0zNEVVops1v'
alias ls='ls --color=auto'
```
**Explanation:**
- **Bash Alias**: This is a way to create a custom command that maps to a longer command or a specific string. Users often put these in their `.bashrc` or `.profile` files.
- **alias**:Running this command without arguments displays all shortcuts currently set in the environment.
Using the password found in the `alias`, successfully switched to user `lana` and verify it get the flag.
```bash
veronica@venus:~$ su - lana
Password: 
lana@venus:~$ id ; whoami
uid=1033(lana) gid=1033(lana) groups=1033(lana)
lana
```

## Key command
`alias`

***You are welcome!***
