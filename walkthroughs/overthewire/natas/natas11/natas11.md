# Natas11

## Level Description
- **Username**: natas11
- **Password**: UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk
- **URL**: http://natas11.natas.labs.overthewire.org

## Method of Solving
![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas11/image-1.png)

In this level, we got the following PHP code:

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas11/image-2.png)

In this challenge, the code seems to add the color of the background into our cookie. Also, the cookie contains the field _showpassword_ set to `no`. If we modify the value to `yes` we will get the value of the password. However, we don't have the key for the `xor_encrypt()` function.

As the algorithm used is XOR and we know the plaintext and ciphertext values of the cookie, we can recover the key. This is due to the face that `ciphertext XOR plaintext = key`, it's called know plaintext attack. Run the PHP script (`natas11_xor_encrypt.php`) to get the secret key.
```bash
<?php
function xor_encrypt($in) {
    $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
$cookie = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D";
echo xor_encrypt(base64_decode($cookie));
?>
```
Result:
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/overthewire/natas/natas11]
└─$ php natas11_xor_encrypt.php
eDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeL      
```
Now we need to encode the new cookie with yes as value for `showpassword` by running PHP script (`natas11_xor_encrypt1.php`):
```bash
<?php
function xor_encrypt($in) {
    $key = "eDWo";
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
echo base64_encode(xor_encrypt(json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"))))
?>
```
Result:
```bash
┌──(dungcngo㉿kali)-[~/…/walkthroughs/overthewire/natas/natas11]
└─$ php natas11_xor_encrypt1.php
HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc5   
```

Now we just need to edit our cookie by `curl`:
```bash
┌──(dungcngo㉿kali)-[/tmp]
└─$ curl -H "Cookie: data=HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc5" -u natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk http://natas11.natas.labs.overthewire.org/
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas11", "pass": "UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk" };</script></head>

<h1>natas11</h1>
<div id="content">
<body style="background: #ffffff;">
Cookies are protected with XOR encryption<br/><br/>

The password for natas12 is yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB<br>
<form>
Background color: <input name=bgcolor value="#ffffff">
<input type=submit value="Set color">
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

***You are welcome!***
