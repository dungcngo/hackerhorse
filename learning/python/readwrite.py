#!/bin/python3

months = open('months.txt')

for month in months:
	print(month.strip())

months.close()

days = open('days.txt', "a")

days.write("\nTuesday")

days.close()
