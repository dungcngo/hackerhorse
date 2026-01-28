Mission 
	The user celeste has left a list of names of possible .html pages
	where to find her password. 
Method of solving
	We needed to fuzz the localhost website for a valid page based on a
	list of potential endpoint names
Key command
	sed 's/$/.html/' pages.txt > url.txt
	
	cat url.txt | xargs -I {} sh -c 'code=$(curl -s -o /dev/null -w "
	{http_code}" http://localhost/{}); [ "$code" -eq 200 ] && echo
	"http://localhost/{}"'
	
	curl -vv http://localhost/cebolla.html
