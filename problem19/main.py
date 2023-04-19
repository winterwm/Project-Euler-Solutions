# Project Euler Problem 19 - Counting Sundays
# Problem Link: https://projecteuler.net/problem=19

import math

# NOTES: 
# Using Zeller's Congruence. This is an easy solution to code, but there may be more efficient ways to do this

# Using a variation of Zeller's Congruence formula to determine the day of the week based on the day/month/year
# h is day of the week. Saturday = 0, Sunday = 1, etc.
# m is month. 3 = March, 4 = April, ... 14 = February
# K is year mod 100
# J is zero based century floor(year/100)
def zeller_congruence(q, m, Y):
	h = (q + math.floor(13*(m+1)/5) + Y + math.floor(Y/4) - math.floor(Y/100) + math.floor(Y/400))% 7
	return h


# Count the days that are the first of the month and Sunday by Zeller's formula
def count_sundays():
	count = 0
	start = 1901
	stop = 2001 # Python's range function stops one short, so this will stop after year 2000 is done
	q = 1 # We are only concered with the first day of every month
	for Y in range(start, stop, 1): # Loop years
		for m in range(3, 15, 1): # Loop months. In Zeller's formula, January is the 13th month and February is the 14th month
			h = zeller_congruence(q, m, Y)
			if h == 1: # If the day is a Sunday, add to count
				count = count + 1
	return count

# Print Results
print("Answer:")
print(count_sundays())

