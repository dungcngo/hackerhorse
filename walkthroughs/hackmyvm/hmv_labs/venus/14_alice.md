Mission
	The admin has left the password of the user anna as a comment in the
	file passwd. 
Method of solving
	Access the comments inside the /etc/passwd file
Key command
	cut -d: -f1,5 /etc/passwd | grep alice
