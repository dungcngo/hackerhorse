# Natas06

## Level Description
- **Username**: natas6
- **Password**: 0RoJwHdSKWFTYR5WuiAewauSuNaBXned
- **URL**: http://natas6.natas.labs.overthewire.org

## Method of Solving
In this level, we need to enter a _secret_ to get the solution. If we check the source, we obtain the following PHP code:

![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas06/image-1.png)

By reading the code we can see that there is an included file (`includes/secret.inc`):

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas06/image-2.png)

Let's try to access it:

![image-3](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas06/image-3.png)

Now, if we enter the secret, we'll be able to get the password for the following level:

![image-4](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas06/image-4.png)

***You are welcome!***
