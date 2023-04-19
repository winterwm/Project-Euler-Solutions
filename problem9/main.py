# Project Euler Problem 9 - Special Pythagorean triplet
# Link: https://projecteuler.net/problem=9
import math

# Helper Methods
def check_triple(a, b, c):
	return a**2 + b**2 - c**2 == 0


# Finds a Pythagorean triple with the added restriction a + b + c = target
# 	Only finds one triple then stops working.
def find_restricted_triple(target):
	for c in range(target-2, 3, -1):
		for b in range(c-1, 1, -1):
			# Once a is driven negative, break and skip to the next c value
			if target-c-b > 0:
				a = target-c-b # Find what a must be given target, b, c
				# If it is a Pythagorean triple, return it
				if check_triple(a, b, c):
					return [a, b, c]
			else:
				break
	else: # Throw an error if no tripple is found
		print("Error: No such triple found")

# Compute the product a*b*c of the Pythagorean triple (a, b, c)
def compute_prod(triple):
	return triple[0]*triple[1]*triple[2]


trip = find_restricted_triple(1000)
ans = compute_prod(trip)

# Print results
print("Answer:")
print(trip)

