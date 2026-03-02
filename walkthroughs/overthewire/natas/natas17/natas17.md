# Natas17	

## Level Description
- **Username**: natas17
- **Password**: EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC
- **URL**: http://natas17.natas.labs.overthewire.org

## Method of Solving
![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas17/image-1.png)

Here is the PHP code for this challenge:

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas17/image-2.png)

From the source code, we know a few things:
- the name of the table: "users"
- the columns in the table: "username", and "password"

We have to construct a payload that causes the app to sleep, because the app doesn't give us any text feedback. We also need to construct a UNION-based payload and determine the number of columns returned. This payload will get us started.
```bash
" UNION SELECT 1,sleep(5) FROM users where username like 'a%';-- - 
```
We can shortcut this process by guessing that the username we're looking for is natas18. That means we can start leaking the user's password with this payload.
```bash
" UNION SELECT 1,sleep(5) FROM users where username = 'natas18' and password like "a%";-- - 
```
We can run the script to solve it (`natas17_brute_force.py`)

***You are welcome!***
