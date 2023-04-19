
import csv
import string

# Project Euler Problem 22 - Names score
# Problem Link: https://projecteuler.net/problem=22

# NOTES: 
# Pretty straight forward. Read in the data and clean it a little, then compute the 
# scores of each of the names and multiply by their position in the data set
# Remember to account for Python being 0 indexed

# Read the names data from names.txt
def read_data():
    file = open('names.txt', 'r')
    data = file.read().split(',')
    file.close()
    data = [eval(item) for item in data] # Eval away the extra quote marks
    return data

# Get the "score" of a word by summing up the alphabetical location of the letters
# A is 1, B is 2, C is 3, etc.
def get_word_value(name):
    S = 0
    for char in name:
        # Use string.ascii_uppercase.index(char) to convert an uppercase character to it's position in the alphabet
        S = S + string.ascii_uppercase.index(char) + 1 # Python 0 indexed so have to add 1 to every letter
    return S

# Compute the score of all the names in the data set and multiply by the names alphabetical 
# position in the data set
def tally_names(data):
    total = 0
    for index in range(len(data)):
        name_val = get_word_value(data[index])
        total = total + name_val*(index+1) # add 1 b/c 0 indexed
    return total

# Read in the data
data = read_data()
data.sort() # Sort the data
print("Answer:")
print(tally_names(data))