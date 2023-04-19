# Project Euler Problem 14 - Longest Collatz sequence
# Problem Link: https://projecteuler.net/problem=14


# NOTES:
# Collatz's algorithm here is deterministic in the sense that a number N 
#	always takes S steps to get to 1. Once we know S, if we get to N while 
#	computing the sequence of another number, we can just add S and be done.
# Once we figure how many terms are in a numbers Collatz sequence, store it in 
#	a dictionary so we can use it when computing the sequence for future numbers

# Global Dictionary with some values to get us started
collatz_dictionary = {
		0:0,
		1:1,
		2:2
	}

# Performs one step of Collatz's iterative process
def perform_Collatz_step(n):
	if n%2 == 0:
		return int(n/2)
	else:
		return int(3*n+1)

# Check if i is a number in our Collatz Numbers dictionary
def check_unknown_Collatz(i):
	global collatz_dictionary
	if i in collatz_dictionary.keys():
		return False
	else:
		return True

# Populate the dictionary. 
# Figure out the length of the Collatz sequence for every number up to n
# Numbers greater than n will also be added to the dictionary if they are 
# 	reached while
def fill_Collatz_dictionary(n):
	global collatz_dictionary
	for i in range(2, n):
		if check_unknown_Collatz(i):
			compute_Collatz_chain(i)

# Progress through the Collatz sequence starting from i until we reach
# 	a number that has already been added to our dictionary. Add
#	all the numbers touched in this chanin to the dictionary.
def compute_Collatz_chain(i):
	global collatz_dictionary
	updates = [] # New numbers not yet in the dictionary
	num = i
	# Keep iterating through the Collatz sequence untill we reach a number in the dictionary
	while check_unknown_Collatz(num):
		updates.append(num)
		num = perform_Collatz_step(num) # Store the new numbers
	steps = len(updates) # How many steps it took us to get to the number in our dictionary
	for j in range(steps):
		# Add the numbers in updates to the dictionary based on the value of the number we found
		# 	in the dictionary and it's position in updates.
		collatz_dictionary.update({updates[j]:collatz_dictionary[num]+steps-j})



def find_maximum():
	global collatz_dictionary
	max_value = max(collatz_dictionary, key=collatz_dictionary.get)
	return max_value


	
fill_Collatz_dictionary(1000000)
print(find_maximum())
