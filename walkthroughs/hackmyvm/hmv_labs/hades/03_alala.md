# 0x03
This write-up explains the steps taken to complete mission 0x03 on hades@hackmyvm.eu, starting from user `alala` and escalating to `althea`.

## Mission
As usual, we read the objective first:
```bash
alala@hades:~$ cat mission.txt 
################
# MISSION 0x03 #
################

## EN ##
User althea loves reading Linux help.
```
The mission for this stage provided a clear hint about user preferences.

## Method of solving
In the home directory, we found a binary named `read` and a file named `althea_pass.txt` that we initially could not access due to permission restrictions.
```bash
alala@hades:~$ ls -la
total 52
drwxr-x--- 2 root   alala   4096 Apr  5  2024 .
drwxr-xr-x 1 root   root    4096 Apr  5  2024 ..
-rw-r--r-- 1 alala  alala    220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 alala  alala   3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 alala  alala    807 Apr 23  2023 .profile
-r--r----- 1 althea althea    21 Apr  5  2024 althea_pass.txt
-rw-r----- 1 root   alala     22 Apr  5  2024 flagz.txt
-rw-r----- 1 root   alala    164 Apr  5  2024 mission.txt
-rwS--s--- 1 root   alala  16056 Apr  5  2024 read
```

The binary `read` has **SUID** (Set User ID) and **SGID** (Set Group ID) bits set. When executed, it displayed the effective user ID as `althea`. This indicated that the binary was designed to run with `althea`'s privileges.
```bash
MAN(1)                         Manual pager utils                         MAN(1)

NAME
       man - an interface to the system reference manuals

SYNOPSIS
       man [man options] [[section] page ...] ...
       man -k [apropos options] regexp ...
       man -K [man options] [section] term ...
       man -f [whatis options] page ...
       man -l [man options] file ...
       man -w|-W [man options] page ...

DESCRIPTION
       man  is  the  system's  manual pager.  Each page argument given to man is
       normally the name of a program, utility or function.  The manual page as-
       sociated  with  each  of  these arguments is then found and displayed.  A
       section, if provided, will direct man to look only in that section of the
       manual.  The default action is to search in all of the available sections
       following a pre-defined order (see DEFAULTS), and to show only the  first
       page found, even if page exists in several sections.

       The  table  below shows the section numbers of the manual followed by the
 Manual page man(1) line 1 (press h for help or q to quit) (Type :e)
 
Examine: cat althea_pass.txt (Press Enter)
~
~
~
~
Manual page man(1) line 1/1 (END) (press h for help or q to quit)
```
**Explanation:**
- **SUID (Set User ID):** The S in the owner's permission field (-rwS--s---) means this program runs with the authority of the file's owner (root) or a designated user .
- **SGID (Set Group ID):** The s in the group's permission field allows the program to run with the privileges of the group alala.
- **Privilege Escalation:** In this specific challenge, the read binary was likely configured to read the althea_pass.txt file which was otherwise inaccessible to the alala user. By executing the binary, it used its elevated permissions to display the contents of the password file directly to the terminal.
## Key command
`./read`

`:e`

`cat althea_pass.txt`
	
***You are welcome!***
