# Project Euler Problem 5 - Smallest multiple
import math

# NOTES
# This is a little extra, but I didn't want to do it the brute force way.
# This method constructs the smallest number divisible by 1, 2, 3, ..., and 20
# by looking at the prime factors of 1, 2, ..., 20.
# That is, it computes prod = p1^n1 * p2^n2 * ... *pk^nk where
# 	p1, ... , pk are all the prime numbers smaller than 20
#	n1, ..., nk are the highest multiplicities that those primes appear
#		in the prime factorization of any of the numbers 1, 2, 3, ..., n

# Helper functions
# Check if num is prime
def is_prime(num):
	for i in range(2, math.floor(num/2)+1):
		composite = num%i == 0
		if composite:
			return False
	else:
		return True

# Find a pair of factors of num
# This finds the largest/smallest pair (ignoring 1 and num)
def find_factor(num):
	for i in range(2, math.floor(num/2)+1):
		composite = num%i == 0
		if composite:
			return [i, num/i]
	else:
		return [num]

# Check if a list of numbers is prime
def check_if_prime_list(factors):
	for i in range(len(factors)):
		if not(is_prime(factors[i])):
			return False
	else:
		return True

# Perform one factorization step
# i.e. take the list of factors and split any non prime entries into a pair of it's factors
def step_factorize(factors):
	new_factors = factors
	l = len(factors) # Number of factors
	# For every item in factors...
	for i in range(l):
		# Store the current factor
		factor = factors[i]
		# If it is not prime...
		if not(is_prime(factor)):
			new_factors.remove(factor)
			adds = find_factor(factor) # Find it's largest and smallest (non 1) factors
			# Add two of its factors
			for j in range(len(adds)):
				new_factors.append(adds[j])
	return new_factors

# Factorize until the whole list is primes
def prime_factorize(factors):
	while not(check_if_prime_list(factors)):
		factors = step_factorize(factors)
	return factors

# List all the prime numbers up to n
def list_primes(n):
	primes = []
	for i in range(2, n):
		if is_prime(i):
			primes.append(i)
	return primes


def counter(lst, target):
    count = 0
    for ele in lst:
        if int(ele) == target:
            count = count + 1
    return count

# General method to find the first number devisible by every natural number
# 	from 1 to n.
# 	Constructs prod by figuring out the powers needed of all prime factors from 2 to n
def find_prod(n):
	# First twenty prime factors.
	# 	We are going to figure out how many powers of each of these we need 
	#	in order for our result to be divisible by all the numbers 1 to 20
	prime_factors = list_primes(n)

	num_of_prime_factors = len(prime_factors)

	# Start the counts for all the primes at one
	count = [1]*num_of_prime_factors

	# For each number from 1 to 20...
	for i in range(2, 20):
		i_counts = [0]*num_of_prime_factors
		factorization = prime_factorize([i]) # Compute the prime factorization
		# For each factor
		for j in range(num_of_prime_factors):
			# Compute how many instnces of that prime factor there are for this number
			i_counts[j] = counter(factorization, prime_factors[j])
			# If the power of the prime factor is greater than the power in count,
			# 	replace the number in count
			if i_counts[j] > count[j]:
				count[j] = i_counts[j]

	prod = 1;
	# Take the prime factors and raise them to the powers in count
	# 	Compute the product
	for i in range(num_of_prime_factors):
		prod = prod*prime_factors[i]**count[i]
	return prod 

# Print results
print("The first number divisible by 1, 2, 3, ..., and 20 is:")
print(find_prod(20))




