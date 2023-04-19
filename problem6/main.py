# Project Euler Problem 6 - Sum square difference
import math

# NOTES
# I don't see anyway around having to square all the numbers for the sum of the squares
# 	But the square of the sum can be computed effciently with the sum of natural numbers formula

# Sum of natural numbers 1, 2, ..., n
def sum_of_naturals(n):
	return n*(n+1)/2

# Sum of the squares of the first n natural numbers
# 	1^2 + 2^2 + 3^2 + ... + n^2
def sum_of_squared(n):
	sum = 0;
	# Loop 1 to n 
	for i in range(1, n+1):
		sum = sum+i**2 # Add the square of i
	return sum

# Computes the difference between the square of the sum 
# 	and the sum of the squares of the natural numbers 1, 2, 3, ..., n
def difference(n):
	S2 = sum_of_squared(n)
	S1 = sum_of_naturals(n)**2
	return S1 - S2

# Print results
print("Answer:")
print(int(difference(100)))