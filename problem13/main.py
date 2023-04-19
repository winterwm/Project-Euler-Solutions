# Project Euler Problem 13 - Large sum
# Problem Link: https://projecteuler.net/problem=13

import requests
from bs4 import BeautifulSoup
import numpy as np
import math

# 	We read in the data storing each number as an entry in a matrix and 
# 	then we do addition by "hand" to find the sum (summing columns and manually carrying the regroups along)
#	You do have to do at least some of it by "hand" since 50 digits is beyond what a double can store


# Get the data from the web and shape it into a 2D array (matrix)
# Each row is one number with each digit being an entry in the arry
def get_data():
	URL = "https://projecteuler.net/problem=13"
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, "html.parser")
	results = soup.find(id="content")

	data = results.find_all("div", class_="monospace center")

	i = 0
	j = -1
	array = []
	# Just keep the numbers
	for char in data[0].text:
		if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			array.append(int(char))
			i = i+1
	# Shape the data into a 100x50 matrix
	matrix = np.reshape(array, (100, 50))
	return matrix

# Sum a column of matrix
def sum_column(matrix, column, n):
	S = 0
	for i in range(n):
		S = S + matrix[i][column]
	return S

# Computes the 
def compute_places(matrix):
	n = len(matrix) # Number of rows of matrix
	m = len(matrix[0]) # Number of columns of matrix
	regroup = 0
	partial_sum = ""
	for place in range(m):
		regroup_digit = regroup%10
		regroup = regroup - regroup_digit
		
		# Always divisible by 10 since we subtracted off the last digit
		regroup = int(regroup/10)

		# Start computing the current digit
		S = regroup_digit
		
		# Sum columns right to left and keep track of regrouping
		S = S + sum_column(matrix, m-place-1, n)

		digit = int(S%10) # Last digit of the sum (after regroupig)
		rest_of_sum = S - digit
		regroup = regroup + int(rest_of_sum/10) # Always divisible by 10
		# Put fill in digits right to left
		partial_sum = str(digit)+partial_sum

		# Move on to next digit

	# Tack the rest of the regrouping on the left of the result
	partial_sum = str(regroup)+partial_sum
	return partial_sum


# Find answer
matrix = get_data()
ans = compute_places(matrix)

# Print results
print("Answer:")
print(ans)













