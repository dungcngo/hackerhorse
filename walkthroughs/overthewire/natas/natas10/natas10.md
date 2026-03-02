# Natas10

## Level Description
- **Username**: natas10
- **Password**: t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu
- **URL**: http://natas10.natas.labs.overthewire.org

## Method of Solving
In this level, we need to enter _words_ to get the password for next level.

![image-1](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas10/image-1.png)

If we check the sourcecode, we get the following PHP code:

![image-2](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas10/image-2.png)

This one is quiet similar to the previous one however, we got some restriction on the characters. But, we could try to read all the file of a directory using following input `.* /etc/natas_webpass/natas11`.
- `.*`: This is a regular expression (regex) that means "matches every string". It is often used to bypass or match all data in search field.
- `/etc/natas_webpass/natas11`: This is the path to a file containing the password for the next level.

![image-3](https://github.com/dungcngo/hackerhorse/blob/main/walkthroughs/overthewire/natas/natas10/image-3.png)
***You are welcome!***
