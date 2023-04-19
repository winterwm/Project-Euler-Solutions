# Project Euler Problem 17 - Number letter counts
# Problem Link: https://projecteuler.net/problem=17

# NOTES:
# There are too many finiky language rules that I can't quite figure out how to 
# 	code up, so I'm just going to tally how many times each word appears
# This one sucks I'm skipping it for now.


# Count characters in a string
def count_char(str):
	return len(str)

# Small numbers
smalls = ["one", "two", "three", "four", "five",
				"six", "seven", "eight", "nine", "ten",
				"eleven", "twelve", "thirteen", "fourteen",
				"fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
smalls_apps = [192, 109, 109, 109, 109, 109, 109, 109, 109,
				10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
tens = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
tens_apps = [100, 100, 100, 100, 100, 100, 100, 100]

hundred = count_char("hundred")
hundred_apps = 100*9
thousand = count_char("thousand")
thousand_apps = 1

and_apps = 99*9
and_len = 3

# Tally up the total characters in the lists
smalls_count = [count_char(small) for small in smalls]
tens_count = [count_char(ten) for ten in tens]
smalls_weighted = [smalls_count[i]*smalls_apps[i] for i in range(len(smalls_count))]
tens_weighted = [tens_count[i]*tens_apps[i] for i in range(len(tens_count))]

ans = sum(smalls_weighted)+sum(tens_weighted)
ans = ans+ hundred*hundred_apps
ans = ans + thousand*thousand_apps
ans = ans + and_len*and_apps

print(ans)

