# Problem 3 - Largest Prime Factor
import numpy as np 
import math

# This script works in the general case and num could be made an input,
# 	but we'll keep it hard coded for the number asked for in Problem 3 of Project Euler
num = 600851475143

# Helper method to find the smallest factor of a given number num (besides 1)
def find_smallest_factor(num):
	for i in range(2, math.floor(num/2)+1):
		if num%i == 0:
			return i
	else:
		# If num not divisible by any numbers from 2 to num/2, 
		#	it is prime and so is it's own smallest factor (besides 1)
		return num


# Check if a number is prime
def is_prime(num, small):
	return small == num

def find_largest_prime_factor(num):
	# List of the factors of num that we will add to as we find them
	factors = []

	# Find smallest factor
	small = find_smallest_factor(num)
	big = num/small

	# Add smallest factor n and compliment factor num/n to factors
	factors.append(small)
	factors.append(big)

	# Search factors for largest element and check if it is prime
	largest = max(factors)
	largest_loc = factors.index(max(factors))
	# Check if num's smallest factor is itself, if it is, then num is prime
	prime_bool = is_prime(small, num)

	# If prime, done
	# If not prime, repeat the process on the largest factor
	while not(prime_bool):
		del factors[largest_loc]
		num = largest 
		small = find_smallest_factor(num)
		big = num/small
		# Add smallest factor n and compliment factor num/n to factors
		factors.append(small)
		factors.append(big)
		# Search factors for largest element and check if it is prime
		largest = max(factors)
		largest_loc = factors.index(max(factors))
		prime_bool = is_prime(small, num)
		# Once the largest factor in the list of factors is prime, we are finished
	return int(largest)

# Find the largest prime factor of num. 
print("Answer: ")
print(find_largest_prime_factor(num))