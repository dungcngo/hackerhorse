# Natas09

## Level Description
- **Username**: natas9
- **Password**: ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t
- **URL**: http://natas9.natas.labs.overthewire.org

## Method of Solving
In this level, we need to enter _words_ to get the solution. 

![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas09/image-1.png)

If we check the view sourcode, we got the following PHP code:

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas09/image-2.png)

By reading the code, we can tell that there is a potential command injection.

So if we can enter `; cat /etc/natas_webpass/natas10 #` in the search field, we will get the password. That's due to the fact that `;` token separates commands in a shell.

![image](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas09/image-3.png)

***You are welcome!***
