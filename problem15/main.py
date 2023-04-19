# Project Euler Problem 16 - Power digit sum
# Problem Link: https://projecteuler.net/problem=16

# NOTES
# I don't know of a good way to avoid explicitly computing 2^1000, 
#	but python handles it pretty well so I guess it's fine.

# Compute b^p and convert it to a string
def compute_power_string(b, p):
	return str(b**p)

# Sum the digits of a number string
def sum_digits(string):
	S = 0
	for char in string:
		S = S+ int(char)
	return S 

# Find the sum of the digits of the reult of b^p
def find_digit_sum(b, p):
	string = compute_power_string(b, p)
	return sum_digits(string)

# Print Results
print("Answer:")
print(find_digit_sum(2, 1000))