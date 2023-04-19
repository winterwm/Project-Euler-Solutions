# Project Euler Problem 7 - 10001st prime
# Link: https://projecteuler.net/problem=7
import math

# NOTES
# I don't know a more efficient method than brute force.
# 	We'll keep trying numbers until we have found 10,001 prime numbers

# Check if num is prime
def is_prime(num):
	for i in range(2, math.floor(num/2)+1):
		if num%i == 0:
			return False
	else:
		return True

# Find the target-th prime number
def find_target_prime(target):
	count  = 0
	num = 1
	while count < target:
		num = num+1
		if is_prime(num):
			count = count+1

	return num

# Find the 10,001st prime
print("Answer:")
print(find_target_prime(10001))