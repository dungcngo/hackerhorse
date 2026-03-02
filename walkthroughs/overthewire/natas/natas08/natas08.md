# Natas08

## Level Description
- **Username**: natas8
- **Password**: xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q
- **URL**: http://natas8.natas.labs.overthewire.org

## Method of Solving
In this level, we have the following PHP code:

![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas08/image-1.png)

Here, our input should be equal to `3d3d516343746d4d6d6c315669563362`, but it is modified by `encodeSecret()` function.

We just need to reverse it to obtain the right secret. Here is the PHP script:
```bash
<?php

$secret = "3d3d516343746d4d6d6c315669563362";

function decodeSecret($secret) {
	return base64_decode(strrev(hex2bin($secret)));
}

print(decodeSecret($secret));
?>
```
The result  when running the above script is:
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/overthewire/natas/natas08]
└─$ php natas8_decode.php
oubWYf2kBq                   
```

Now, if we enter the secret we should get the password for the next level:

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas08/image-2.png)

***You are welcome!***
