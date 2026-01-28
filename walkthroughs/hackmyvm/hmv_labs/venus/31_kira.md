Mission
	The user veronica visits a lot http://localhost/waiting.php
Method of solving
	We need to send a specific user-agent HTTP header to the endpoint
Key command
	curl -A "PARADISE" http://localhost/waiting.php
	curl -H "User-Agent: PARADISE" http://localhost/waiting.php
	
