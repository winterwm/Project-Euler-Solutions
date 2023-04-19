# Project Euler Problem 8 - Largest product in a series
# Link: https://projecteuler.net/problem=8

# Deconstruct a number text file into an array
#	Each entry in the array will be a single digit
def deconstruct(string):
	array = []
	for letter in string:
		# Clean up any new lines characters
		if not(letter == '\n'):
			array.append(int(letter))
	return array

# Looks through array (an array of digits) and computes the product of every 
#	window_size adjacent entries.
# Returns the maximum product computed for any window
def find_max_prod(array, window_size):
	# Initialize the max_prod
	max_prod = 0
	number_length = len(array)
	for i in range(number_length-window_size):
		prod = 1 # Initialize as 1
		for j in range(window_size):
			prod = prod*array[i+j]
		if prod > max_prod:
			max_prod = prod
	return max_prod
 
# Read in the big number file and store it as a string
file =  open(r"big_number.txt")
string = str(file.read())
file.close()
array = deconstruct(string) # Convert the string to an array containing it's digits

window_size = 13 # Set window size
# This determines how many adjacent digits are used in the product.
# E.g. window_size = 13 means every group of 13 consecutive digits will be tested

print(find_max_prod(array, window_size))


