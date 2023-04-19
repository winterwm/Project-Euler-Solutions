# Project Euler Problem 20 - Factorial digit sum
# Problem Link: https://projecteuler.net/problem=20

import math

# NOTES
# Needs big number support, but computing the 100! and looping through the digits works.
# You could save some computation by dividing by factors of 10 you get in the factorial. 
# i.e. dont multiply by 10, multply by 2 instead of 20 since the 10s will just add traling 0s
# I don't know of a way that they avoids computing a really big intiger and looping through the digits though

# Sum the digits of a number
def counter(num):
	string = str(num) # Convert to string
	total = 0
	for char in string: # Loop through the gigits
		total = total + int(char) # Convert the digits back to ints and add them to total
	return total

num = math.factorial(100) # Compute 100! 
# Python handles big numbers well enough to do this. Neat!

# Print Results
print("Answer")
print(counter(num))