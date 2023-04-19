import numpy as np
import math
import time

# I think this will work for max_n = 9, it will just take 5 hours or so with the current method
# Thinking about ways to make this more effiecient
# There may be divisibility restrictions on p, a, b that would help eliminate cases


tic = time.perf_counter()

# For n = 1, 2, ..., max_n
max_n = 6;
solutions = []


# Helper Functions
def compute_candidate_b(a, p, n):
	B = float(p/10**n - 1/a)
	return float(1/B) 

def check_is_int(num):
	eps = float(np.finfo(float).eps) # Machine percision
	return abs(num - round(num)) < 0.00000005

def index_1_range(num):
	return range(1, num+1)

# i takes role of n, j takes role of p
for i in index_1_range(max_n):
	# For the current n, loop over all values from 1 to 2*10^n
	for j in index_1_range(2*10**i):
		
		# Right Hand Side for current n, p
		rhs = float(j/10**i)
		
		# Start a at 1 or 1/rhs
		a = max(1, math.floor(float(1/rhs)))
		
		# If 2/a >= rhs, there could exist b such that 1/a + 1/b = rhs
		while float(2/a) >= rhs:
			if float(1/a) < rhs:
				# Compute b for fixed current a, p, n
				b_candidate = compute_candidate_b(a, j, i)
				# If the computed b is an integer, add the tupple [a, b, p, n] to the list of solutions
				if check_is_int(b_candidate):
					solutions.append([a, b_candidate, j, i])
			a=a+1;
print("Number of solutions:")
print(len(solutions))

toc = time.perf_counter()
print(f"This program took {toc - tic:0.4f} seconds")