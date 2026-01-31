# 0x28
This write-up explains the steps taken to complete mission 0x28, starting from user `lola` and escalating to `celeste`.

## Mission 
As usual, read the objective first:
```bash
lola@venus:~$ cat mission.txt 
################
# MISSION 0x28 #
################

## EN ##
The user celeste has left a list of names of possible .html pages where to find her password. 
```
 
## Method of solving
Checking the home directory, we found a file named `pages.txt` containing a long list of potential filenames.
```bash
lola@venus:~$ ls -la
total 36
drwxr-x--- 2 root lola 4096 Apr  5  2024 .
drwxr-xr-x 1 root root 4096 Apr  5  2024 ..
-rw-r--r-- 1 lola lola  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 lola lola 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 lola lola  807 Apr 23  2023 .profile
-rw-r----- 1 root lola   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root lola  272 Apr  5  2024 mission.txt
-rw-r----- 1 root lola 1438 Apr  5  2024 pages.txt
```
Base on the mission, these pages are hosted on the local web server. We need to check each entry in `pages.txt` by appending `.html` and requesting it via `curl`. To automate this, we use a bash one-liner that loops through the list and stops only when it finds a page that actually exists.
```bash
lola@venus:~$ for page in $(cat pages.txt); do curl -s -f localhost/$page.html && echo -e "\nFound in: $page.html" && break; done
VLSNMTKwSV2o8Tn

Found in: cebolla.html
```
**Explanation:**
- `for page in $(cat pages.txt);`: Read every word from the dictionary file.
- `curl -s -f localhost/$page.html`: `-s` (silent) hides the progress meter and `-f` (fail) ensures the command returns an error if the page is missing (404), allowing the `&&` logic to work.
- `&& echo -e "\nFound in: $page.html" && break;`: If the request is successful, it prints the content, identifies the source file (`cebolla.html`), and exists the loop.

With this password captured, logged in as `celeste` and verify it, get the flag.
```bash
lola@venus:~$ su - celeste
Password: 
celeste@venus:~$ id ; whoami
uid=1029(celeste) gid=1029(celeste) groups=1029(celeste)
celeste
```

## Key command
`for page in $(cat pages.txt); do curl -s -f localhost/$page.html && echo -e "\nFound in: $page.html" && break; done`

***You are welcome!***
