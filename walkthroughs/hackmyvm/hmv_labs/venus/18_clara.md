Mission
	The password of user frida is in the password-protected zip
	(rockyou.txt can help you) 
Method of solve
	download the zip file and then crack the password using some
	password cracking software
Key command
	step1: in clara vm : cat protected.zip | base64 - chuyen noi dung file zip thanh chuoi base64
	step2: copy noi dung sang tmp cua may chu local, thuc hien tao file protected.b64 sau do chuyen sang file zip: cat protected.b64 | base64 -d > protected.zip
	step3: chuyen file zip thanh hash: zip2john protected.zip > clara.hash
	step4: run: john clara.hash --wordlist=/usr/share/wordlists/rockyou.txt de xem pass cua file zip
	step5: unzip protected.zip 
	step6: cat pwned/clara/protected.txt 
