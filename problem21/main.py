# Project Euler Problem 21 - Amicable numbers
# Problem Link: https://projecteuler.net/problem=21

import math

# NOTES:
# There are methods that generate amicable numbers, but not exhaustivley. So we'll try every number up to 10,000
# It would be more efficient to work from the prime factorizations rather than computing the divisors for every number
# 



# Find the proper divisors of num
def find_proper_divisors(num):
	divisors = []
	for i in range(1, math.floor(num/2)+1):
		if num/i == math.floor(num/i):
			divisors.append(i)
	return divisors

# Sum a list of divisors
def sum_divisors(divisors):
	return sum(divisors)

# Find the amicable numbers up to cap
def find_amicable_numbers(cap):
	divisor_sums = [0]*(cap+1) # Prepare array
	# For all the numbers up to cap, compute the sum of the divisors
	for i in range(0, cap+1, 1):
		divisors = find_proper_divisors(i)
		divisor_sums[i] = sum_divisors(divisors)

	# Add the amicable numbers to an array
	amicable_numbers = []
	for i in range(0, cap+1, 1):
		# Technically we should be wary of pair of amicable numbers where one is above cap but the other is below cap
		# Thankfully, through testing we've found no such pair exists for cap = 10,000
		if divisor_sums[i] < cap:
			# divisor_sums basically works like d(n) from the problem statement
			if divisor_sums[divisor_sums[i]] == i and divisor_sums[i] != i:
				# Note perfect numbers (numbers for which d(n) = n) are excluded from being amicable numbers per the prompt
				amicable_numbers.append(i)

	return amicable_numbers

# Print Results
print("Answer:")
print(sum(find_amicable_numbers(10000)))
