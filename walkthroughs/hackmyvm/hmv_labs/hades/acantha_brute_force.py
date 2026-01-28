#!/bin/python3

import subprocess

#Path to the binary
binary_path = "./guess"

#Loop through all 6-digit PINs
for pin in range(1000000):
	pin_str = str(pin).zfill(6)
	print(f"Trying PIN: {pin_str}")

	process = subprocess.Popen([binary_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	output, error = process.communicate(input=(pin_str + '\n').encode())

	output_decoded = output.decode()

	# Check if the binary's output contains the failure message
	if "NO" not in output_decoded:
		print(f"Correct PIN found: {pin_str}")
		break
