# Project Euler Problem 12 - Highly divisible triangular numbers
# Problem Link: https://projecteuler.net/problem=12

import math

# NOTES
# By the sum of natural numbers formula Tn = n*(n+1)/2. Therefore, the factors 
# 	of Tn are the n/2 and n+1 or n+1/2 and n (depending on which one of n or n+1 is even)
# 	Each step we need to factor one additional number (n if n is odd or n/2 if even)

# Find Primes code from Problem 10
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

# Check if p is a divisor of num
def is_prime_divisors(num, p):
	return num % p == 0

# Find the power of p in the prime factorization of num
def find_prime_multiplicity(num, p):
	test = p
	power = 1
	while(num % test == 0):
		test = test*p 
		power = power+1
	return power-1

def find_prime_factorization(num, primes):
	factorization = [];
	for i in range(len(primes)):
		p = primes[i]
		if is_prime_divisors(num, p):
			factorization.append(find_prime_multiplicity(num, p))
		else:
			factorization.append(0)
	return factorization
	
# Find the multiplicity array for num/2
# Used for the even values of n
def prime_multiplicities_even(num, primes):
	return find_prime_factorization(int(num/2), primes)

# Find the multiplicity array for num
# Used for odd values of n
def prime_multiplicities_odd(num, primes):
	return find_prime_factorization(num, primes)

# combine the two multiplicity arrays
def combine_multiplicities(multiplicities1, multiplicities2):
	combined_multiplicities = []
	for i in range(len(multiplicities1)):
		combined_multiplicities.append(multiplicities1[i]+multiplicities2[i])

	return combined_multiplicities

# Count the divisors based on the powers prime factorization.
# Uses the formula (n1+1)*(n2+1)*...(nk+1) where n1, ..., nk 
# 	are the (nonzero) powers in the prime factorization.
def count_divisors(multiplicities):
	prod = 1
	for i in range(len(multiplicities)):
		if multiplicities[i] > 0:
			prod = prod*(multiplicities[i]+1)
	return prod



def find_target_triangle(target):
	primes = find_primes(100000)
	N = len(primes)
	n = 1 
	n_odd = False
	max_divisors = 1
	T = 1
	multiplicities1 = [0]*N
	multiplicities2 = [0]*N

	while max_divisors < target:
		n = n+1
		n_odd = (n_odd+1)%2
		multiplicities1 = multiplicities2
		if n_odd == 0:
			multiplicities2 = prime_multiplicities_odd(n, primes)
		else:
			multiplicities2 = prime_multiplicities_even(n, primes)
		combined_multiplicities = combine_multiplicities(multiplicities1, multiplicities2)
		divisor_count = count_divisors(combined_multiplicities)

		if divisor_count > max_divisors:
			max_divisors = divisor_count;
		T = (n-1)*(n)/2
		# print(T)
		# # print(combined_multiplicities)
		# print(divisor_count)



	return T

def testing():
	primes = find_primes(100)
	num = 10
	out1 = prime_multiplicities_odd(11, primes)
	out2 = prime_multiplicities_odd(10, primes)
	combined_multiplicities = update_combine_multiplicities(out1, out2)
	print(combined_multiplicities)
	print(count_divisors(combined_multiplicities))





print("Answer:")
# testing()
T = find_target_triangle(500)
print(T)
