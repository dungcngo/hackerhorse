# 0x26
This write-up explains the steps taken to complete mission 0x26, starting from user `alexa` and escalating to `ariel`.

## Mission
As usual, read the mission:
```bash
alexa@venus:~$ cat mission.txt 
################
# MISSION 0x26 #
################

## EN ##
The password of the user ariel is online! (HTTP)
```

## Method of solving
The hint indicates that the password is being hosted on a local web server. To retrieve the password from the internel  web server, we can use the `curl` command. Since no port was specified, we assumed the default HTTP port (80).
```bash
alexa@venus:~$ curl localhost
33EtHoz9a0w2Yqo
```
With the password obatained, switching user to `ariel` and get the flag.
```bash
alexa@venus:~$ su - ariel
Password: 
ariel@venus:~$ id ; whoami
uid=1027(ariel) gid=1027(ariel) groups=1027(ariel)
ariel
```

## Key command
`curl localhost`
	
***You are welcome!***
