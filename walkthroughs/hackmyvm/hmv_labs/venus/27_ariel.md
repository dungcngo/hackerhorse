Mission
	Seems that ariel dont save the password for lola, but there is a
	temporal file.
Method of solving
	Access a temporary file created by the VIM text editor, and extract
	a list of potential passwords, then brute force the login of the
	next user using that list of passwords
Key command
	hydra -s 5000 -l lola -P passwords.txt venus.hackmyvm.eu ssh
