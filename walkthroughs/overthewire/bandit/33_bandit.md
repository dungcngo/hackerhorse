# Bandit33

## Level Description
After all this `git` stuff, it’s time for another escape. Good luck!

## Method of Solving
After log into `bandit32`, we are now welcomed by a big ASCII banner, but this one is different, it says:
```bash
WELCOME TO THE UPPERCASE SHELL
>> 
```
This is a shell escape scenario.

We are not allowed to use any commands which use lowercase characters.
```bash
>> ls
sh: 1: LS: Permission denied
>> pwd
sh: 1: PWD: Permission denied
>> whoami
sh: 1: WHOAMI: Permission denied
```
But spcecial characters are unaffected. We use the only available shell trick: the current shell process.
```bash
>> $0
$ 
```
What is `$0`?
- `$0` in shell scripting represents the name of the shell or script being executed. 
- In this case, running `$0` will re-execute the shell.
```bash
$ whoami
bandit33
```
Now that we are operating as `bandit33`, just read the password file:
```bash
$ cat /etc/bandit_pass/bandit33
tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0
```

## Key command
`$0`

***You are welcome!***
