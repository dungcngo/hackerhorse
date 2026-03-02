# Natas13

## Level Description
- **Username**: natas13
- **Password**: trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC
- **URL**: http://natas13.natas.labs.overthewire.org

## Method of Solving
![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas13/image-1.png)

Here is the source code for this challenge:

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas13/image-2.png)

This one is similar to the previous one, however this time the developer check if the file is an image file. We can try to bypass it by using the magic number of bitmap file, `GIF89a`, and prepend it to our PHP code (`natas13_file.php`):
```bash
GIF89a<?php echo file_get_contents('/etc/natas_webpass/natas14'); ?>
```

Then we use the same trick as before to modify the file extension in `Burp`. Upload file `natas13_file.php` on the page and use `Burpsuite` to intercept POST method, change filename.jpg to filename.php.

![image-3](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas13/image-3.png)

Then we can browser the link returned by the server.

![image-5](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas13/image-5.png)

And get the password for next level:

![image-4](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas13/image-4.png)

***You are welcome!***
