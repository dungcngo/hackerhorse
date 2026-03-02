# Natas12

## Level Description
- **Username**: natas12
- **Password**: yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB
- **URL**: http://natas12.natas.labs.overthewire.org

## Method of Solving
![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas12/image-1.png)

In this level, we got the following PHP code:

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas12/image-2.png)

Here, it is a simple file upload vulnerability. If we upload a simple PHP file like `natas12_file.php`:
```bash
<?php echo file_get_contents('/etc/natas_webpass/natas13'); ?>
```
We should be able to get the password for the next level. However, if you take a look at the HTML code:

![image-3](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas12/image-3.png)

The extension of the file if modified on the client side. If we want to keep the `.php` extension, we need to intercept the upload request and modify the extension to `.php`, it can be done using a proxy like `Burp`.

Upload file `natas12_file.php` on the page. Use `Burpsuite` to intercept POST method  and change filename.jpg to filename.php.

![image-4]((https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas12/image-4.png)

Then, we can browser the link return by the server:

![image-5]((https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas12/image-5.png)

And get the password for next level:

![image-6]((https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas12/image-6.png)
***You are welcome!***
