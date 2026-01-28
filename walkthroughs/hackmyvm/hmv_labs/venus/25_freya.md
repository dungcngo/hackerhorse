Mission
	User alexa puts her password in a .txt file in /free every minute
	and then deletes it. 
Method of solving
	Write a loop which constantly reads an empty directory, but read all
	the file contents when a file exists there
Key command
	while true; do ls /free/* 2>/dev/null | xargs -r cat; sleep 1; done
	while true; do [ -f /free/* ] && cat /free/*; sleep 1; done	
	while true; do cat /free/*.txt 2>/dev/null; sleep 1; done
