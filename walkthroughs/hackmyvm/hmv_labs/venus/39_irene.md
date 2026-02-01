# 0x39
This write-up explains the steps taken to complete mission 0x39, starting from user `irene` and escalating to `adela`.

## Mission
As usual, we read the objective first:
```bash
irene@venus:~$ cat mission.txt 
################
# MISSION 0x39 #
################

## EN ##
The user adela has lent her password to irene.
```

## Method of solving
In the home directory, we find several files related to encryption and SSH: a private key (`id_rsa.pem`), a public key (`id_rsa.pub`), and an encrypted file named `pass.enc`.
```bash
irene@venus:~$ ls -la
total 44
drwxr-x--- 2 root  irene 4096 Apr  5  2024 .
drwxr-xr-x 1 root  root  4096 Apr  5  2024 ..
-rw-r--r-- 1 irene irene  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 irene irene 3526 Apr 23  2023 .bashrc
-rw-r--r-- 1 irene irene  807 Apr 23  2023 .profile
-rw-r----- 1 root  irene   31 Apr  5  2024 flagz.txt
-rw-r----- 1 root  irene 1704 Apr  5  2024 id_rsa.pem
-rw-r----- 1 root  irene  451 Apr  5  2024 id_rsa.pub
-rw-r----- 1 root  irene  178 Apr  5  2024 mission.txt
-rw-r----- 1 root  irene  256 Apr  5  2024 pass.enc
```
Running `file pass.enc` showed it was raw data, comfirming it was likely a binary blob resulting from encryption.

While we initially tried to use the keys to SSH in to `adela@localhost`, the host key verification failed, and the files were clearly intended for a different purpose: **Asymmetric Decryption**.
Since `id_rsa.pem` is a private key and `pass.enc` is an encrypted file, we used `openssl` to decrypt the data. 
```bash
irene@venus:~$ openssl pkeyutl -decrypt -inkey id_rsa.pem -in pass.enc
nbhlQyKuaXGojHx
```
**Explanation:**

**RSA Encryption**: This is an asymmetric cryptographic algorithm. Data encrypted with a **Public Key** can only be decrypted by the corresponding **Private Key**.
`openssl rsautl -decrypt`: This is and **OpenSSl** utility used to perform decryption operations with asymmetric keys (public/private keys).
`-inkey id_rsa.pem`: Specifies the private key used to "unlock" the data.
`-in pass.enc`: The encrypted file containing the secret.
**The Findings**: The decryption process translated the binary "trash" in pass.enc into a human-readable password string.

Using the password, we switch to user `adela` and get the flag.
```bash
irene@venus:~$ su - adela
Password: 
adela@venus:~$ id ; whoami
uid=1040(adela) gid=1040(adela) groups=1040(adela)
adela
```

## Key command
`openssl pkeyutl -decrypt -inkey id_rsa.pem -in pass.enc`

***You are welcome!***
