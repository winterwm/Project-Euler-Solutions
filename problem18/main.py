# Project Euler Problem 18 - Maximum path sum I
# Problem Link: https://projecteuler.net/problem=18

import requests
from bs4 import BeautifulSoup
import numpy as np
import math

# NOTES:
# Scrapes the problem and builds a binary tree for the given problem.
# Recursivly finds the maximum path sum of a binary tree
# Assumes a balanced (pyramid) tree, but it would be fairly straight forward to generalize

# Node Class
class Node:
	# A node in the tree
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

     # Insert a row at the next available level
    def insert_row(self, data_array):
    	nodes = [self] # List of traversed nodes
    	node = self # Current node variable. Starts at root

    	# Initialize left and right node for placing new middle nodes
    	left_node = None 
    	right_node = None

    	# Legth of data array/how many new nodes we have to place
    	data_count = len(data_array)

    	# Traverse down to the last level
    	while node.leftChild != None: 
    		node  = node.leftChild
    		nodes.append(node) # Add nodes to traversed nodes as we go

    	# Add the left most node. Only connected to the previous level in one place
    	node.leftChild = Node(data_array[0])

    	# Loop for "middle" nodes that need to have two connections
    	for i in range(1, data_count-1, 1): # Start at 1 since 0 already added 
    		# First and last data added outside of this loop
    		left_node = node 
    		for j in range(i):
    			nodes.pop() # Pop i nodes off the nodes list / Take i steps back up
    			node = nodes[-1] # Make current node last node in traversed nodes
    		for j in range(i):
    			node = node.rightChild # Travese right i times
    			nodes.append(node) # Add nodes to list as we go

    		right_node = node 

    		# Link left and right node to the new node
    		left_node.rightChild = Node(data_array[i])
    		right_node.leftChild = left_node.rightChild

    	node.rightChild = Node(data_array[data_count-1]) # Last data in this row
    	# Only connected to the the right most node of the previous level

    	return



# Get the data from the web and shape it into a 2D array (matrix)
# Each row is one number with each digit being an entry in the arry
def get_data():
	URL = "https://projecteuler.net/problem=18"
	page = requests.get(URL) # Get the page

	soup = BeautifulSoup(page.content, "html.parser")
	results = soup.find(id="content") # Find the content

	data = results.find_all(class_="monospace center")
	triangle_data = data[1].text # Get the (second) displayed triangle and make it text


	return triangle_data

# Split the data and convert strings to ints so it is easy to add to the tree
def data_to_tree(triangle_data):
	triangle_data_split = triangle_data.split("\n") # Split on new lines
	data = []
	for row in triangle_data_split:
		row_split = row.split() # Split each row on spaces
		row_int = [int(i) for i in row_split] # Convert from strings to ints
		data.append(row_int) # Add the row to data
	return data

# Buid tree from data
def build_tree():
	triangle_data = get_data() # Get data from web
	data = data_to_tree(triangle_data) # Prepare data for adding to the tree
	root = Node(root_data) # Start by making the root
	data.remove(data[0]) # Remove the root from the data now that it is in the tree
	for row in data:
		root.insert_row(row) # Add the rows to the tree one by one
	return root # Return the root of the built tree

def find_max_path(root):
	max_sum = root.data # If we go through this node we have to add it's data to the sum
	if root.leftChild == None:
		return max_sum # If the root is an end node return the root's data
	else:
		# If not an end, compute the left and right max sum resursivly and return the maximum of the two
		left_sum = find_max_path(root.leftChild)
		right_sum = find_max_path(root.rightChild)
		max_sum = max_sum + max(left_sum, right_sum) # Add the larger of the left and right sum to max sum
		return max_sum




tree = build_tree() # Build tree
ans = find_max_path(tree) # Find the max path

# Print results
print("Answer:")
print(ans)






