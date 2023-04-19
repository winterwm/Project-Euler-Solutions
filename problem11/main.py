# Project Euler Problem 10 - Largest product in a grid
# Link: https://projecteuler.net/problem=11

import pandas as pd
import numpy 

# NOTES
# We only need to compute products in the down, right and three diagonal directions
#	since the products are commutative. 

# Computes the product of four adjacent entries in the array
# Starting with entry (i, j) and counting to the right
# If this would take us beyond the end of the array, returns 0
def right_prod(array, window, i, j, dim):
	if j + window > dim:
		return 0
	else:
		prod = 1
		for k in range(window):
			prod = prod*array[i][j+k]
		return prod

# Computes the product of four adjacent entries in the array
# Starting with entry (i, j) and counting to downwards
# If this would take us beyond the end of the array, returns 0
def down_prod(array, window, i, j, dim):
	if i + window > dim:
		return 0
	else:
		prod = 1
		for k in range(window):
			prod = prod*array[i+k][j]
		return prod

# Computes the product of four diagonal entries in the array
# Starting with entry (i, j) and counting to the right-downward direction
# If this would take us beyond the end of the array, returns 0
def diag_prod(array, window, i, j, dim):
	if j + window > dim or i+window > dim:
		return 0
	else:
		prod = 1
		for k in range(window):
			prod = prod*array[i+k][j+k]
		return prod

# Computes the product of four diagonal entries in the array
# Starting with entry (i, j) and counting to the left-downward
# If this would take us beyond the end of the array, returns 0
def diag_counter_prod(array, window, i, j, dim):
	if j - window < 0 or i+window > dim:
		return 0
	else:
		prod = 1
		for k in range(window):
			prod = prod*array[i+k][j-k]
		return prod

# Computes the product of four diagonal entries in the array
# Starting with entry (i, j) and counting to the right-upward
# If this would take us beyond the end of the array, returns 0
def diag_up_prod(array, window, i, j, dim):
	if j + window > dim or i-window < 0:
		return 0
	else:
		prod = 1
		for k in range(window):
			prod = prod*array[i-k][j+k]
		return prod

def find_prod(dim, window):
	max_prod = 0
	for i in range(dim):
		for j in range(dim):
			S = right_prod(array, window, i, j, dim)
			if S > max_prod:
				max_prod = S 
			S = down_prod(array, window, i, j, dim)
			if S > max_prod:
				max_prod = S
			S = diag_prod(array, window, i, j, dim)
			if S > max_prod:
				max_prod = S  
			S = diag_counter_prod(array, window, i, j, dim)
			if S > max_prod:
				max_prod = S
			S = diag_up_prod(array, window, i, j, dim)
			if S > max_prod:
				max_prod = S    
	return max_prod 



# Read in text fime and convert to a 2d array
df = pd.read_csv("number_grid.txt", delim_whitespace = True, header = None)
array = df.to_numpy()

# Tell the product finder the dimensions of the data and how many adjacent
# 	values to compute the products with.
#	Assuming a 20x20 2d array and computing products with 4 adjacent/diagonal entries 
#	because that is what is given in the problem, but this code is generalizable.
dim = 20;
window = 4;
max_prod = find_prod(dim, window)


# Print results
print("Answer:")
print(max_prod)






