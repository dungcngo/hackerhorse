Mission	
	The password of the clara user is found in a file modified on May 1,
	1968. 
Method of solving
	use the find command to locate a file modified in 1968
Key command
	find / -type f -mtime +18440 2>/dev/null
