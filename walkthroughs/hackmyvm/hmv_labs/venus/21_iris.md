Mission
	User eloise has saved her password in a particular way. 
Method of solving
	we need to convert the base64 encoded string back into a binary
	file. The binary file is a jpg file which has the password in its
	contents
Key command
	base64 -d eloise.b64 > eloise.jpg
