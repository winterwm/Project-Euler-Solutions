# Project Euler Problem 10 - Summation of primes
# Link: https://projecteuler.net/problem=10

import math

# Helper Methods

# Mark all the multiples of p starting with p^2 in the indicator array
# 	We can start with p^2 since factors have pairs. If a number between p
#	and p^2 is divisible by p it has already been marked by one of the eariler
# 	markings.
def mark_multiples(indicator, p, n):
	for i in range(p**2, n, p):
		indicator[i] = 1;
	return indicator 

# Find the next prime. It is the next unmarked 
def find_next_prime(indicator, p, n):
	for i in range(p+1, n, 1):
		if indicator[i] == 0:
			return i
	else:
		return n+1

# Retrive all the prime numbers from 0 to n based on the indicator array
def scoop_primes(indicator, n):
	primes = []
	for i in range(n):
		if indicator[i] == 0:
			primes.append(i)

	return primes 

# Find all the prime numbers up to n
def find_primes(n):
	indicator = [0]*n 

	# Mark 0 and 1 as not prime 
	# I think the code is most clear if the index is the number
	indicator[0] = 1
	indicator[1] = 1

	p = 0 
	while p < n:
		# Find next p or terminate
		p = find_next_prime(indicator, p, n)
		# Mark multiples of p
		indicator = mark_multiples(indicator, p, n)

	primes = scoop_primes(indicator, n)
	return primes


# Sum all the entries in an array
def sumation(array):
	sum = 0
	for item in array:
		sum = sum+item
	return sum 

# Sum all the prime numbers up to n
def sum_primes(n):
	primes = find_primes(n)
	S = sumation(primes)
	return S;


# Sum all the prime numbers up to 2,000,000 and print the answer
print("Answer:")
print(sum_primes(2000000))





