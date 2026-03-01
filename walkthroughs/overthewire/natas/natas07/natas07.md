# Natas07

## Level Description
- **Username**: natas7
- **Password**: bmg8SvU1LizuWjx3y7xkNERkHxGre0GS
- **URL**: http://natas7.natas.labs.overthewire.org

## Method of Solving
In this level, we get 2 links random pages. If you check the URL, we can see that the `index.php` takes the page name as variable.

![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas07/image-1.png)

We know that the password for `natas8` should be in `etc/natas_webpass/natas8`, so we could try a path traversal to find the password:

`http://natas7.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8`

And here we go!

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas07/image-2.png)

***You are welcome!***
