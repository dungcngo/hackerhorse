Mission
	The user isabel has left her password in a file in the /etc/xdg
	folder but she does not remember the name, however she has dict.txt
	that can help her to remember.
Method of solving
	We need to brute force readable files in a directory where we have
	no read permissions
Key command
	cat dict.txt | xargs -I {} sh -c 'if [ -r /etc/xdg/{} ]; then echo
	"Readable file found: /etc/xdg/{}"; exit 0; fi' || echo "No readable
	file found in /etc/xdg directory."
