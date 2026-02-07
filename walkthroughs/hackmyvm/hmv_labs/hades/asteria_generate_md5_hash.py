#!/bin/python3

import hashlib

def find_magic_hash(limit=1000000000):
	for i in range(limit):
		s = str(i).encode()
		h = hashlib.md5(s).hexdigest()
		if h.startswith("0e") and h[2:].isdigit():
			print(f"Found: {i} -> {h}")
	print("Not found within limit")

if __name__ == "__main__":
	find_magic_hash()
