# Victor Arsenescu
# 2/20/20
# COMP 131 HW 2

class Node(object):
	"""Each node has a pancake list and scores"""
	def __init__(self, pancakes, g):
		self.pancakes  = pancakes
		self.backwards = g
		self.forwards  = heuristic(pancakes) 
		self.total_score = self.backwards + self.forwards
	def heuristic(self, pancakes):
		h = 0
		for i in range(len(self.pancakes) - 1):
			h += 1 if abs(self.pancakes[i] - self.pancakes[i+1]) > 1 else 0
		return h

def flip(pancakes, i):
    flippy = arr[-i:]
    flippy.reverse()
    end = len(arr) - i
    return arr[:end] + flippy

def generate_successors(smallest):
	successors = []
	for i in range(1, len(smallest.pancakes)): # can't flip zero pancakes
		successors.append(Node(flip(smallest.pancakes, i), smallest.backwards + 1))
	return successors

def isGoal(node):
	return True if node.pancakes == [7,6,5,4,3,2,1] else False

def A_star(initial_state, generate_successors, isGoal):
	'''
	Arguments: 
	- state_space is some list-like structure of length k.
	- successor is a function that returns a new state - aka modifies P.
	- path and heuristics are functions that return the relevant values.
	- isGoal is a function which performs a goal check and returns T/F.
	'''
	expanded, frontier = [], [initial_state]
	while frontier: 
		smallest = min(frontier, key=lambda node: node.total_score) 
		frontier.remove(smallest)
		if isGoal(smallest):
			return smallest.pancakes
		for successor in generate_successors(smallest):
			if successor in expanded:
				continue
			if successor in frontier:
				frontier[frontier.index(successor)] = min(successor, frontier[frontier.index(successor)], key=lambda node: node.total_score)
			elif successor in expanded:
				expanded[expanded.index(successor)] = min(successor, expanded[expanded.index(successor)], key=lambda node: node.total_score)
			else:
				frontier.append(successor)
	return None

if __name__ == '__main__':
	pancakes = [3,2,5,1,6,4,7]
	initial = Node(pancakes, 0)
	A_star(initial, generate_successors, isGoal)
