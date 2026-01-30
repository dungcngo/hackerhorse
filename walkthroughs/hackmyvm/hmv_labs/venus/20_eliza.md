# 0x20
This write-up explains the steps taken to complete mission 0x20, starting from user `eliza` and escalating to `iris`.

## Mission
As always, read the objective first:
```bash
eliza@venus:~$ cat mission.txt 
################
# MISSION 0x20 #
################

## EN ##
The user iris has left me her key.
```

## Method of solving
We could easily logging in as `iris` using `ssh` with `-i` option and then typed `yes`:
```bash
eliza@venus:~$ ssh -i .iris_key iris@localhost
The authenticity of host 'localhost (::1)' can't be established.
ED25519 key fingerprint is SHA256:JQMeqhRR4E5l3ltY/S1hK0srs1Q3KaXzC6Qga/MvPqM.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
..........................................................
Last login: Fri Jan 30 17:21:11 2026 from 172.66.0.1
iris@venus:~$ 
```
Verify it by switching user to `iris` and sucessfully, get the flag.
```bash
iris@venus:~$ id ; whoami
uid=1021(iris) gid=1021(iris) groups=1021(iris)
iris
```

## Key command	
`ssh -i iris_key iris@venus.hackmyvm.eu -p 5000`

***You are welcome!***
	
