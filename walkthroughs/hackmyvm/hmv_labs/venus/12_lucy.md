Mission
	The password of the user elena is between the characters fu and ck 
Method of solving
	we need to isolate a string in a file between some specific 
	characters
Key command
	sed -n 's/.*fu\(.*\)ck.*/\1/p' file.yo 
