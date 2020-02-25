# Victor Arsenescu
# 2/20/20
# COMP 131 HW 2
import random

class Node(object):
	"""Each node has a pancake list and scores"""
	def __init__(self, pancakes, g):
		self.pancakes  = pancakes
		self.backwards = g
		self.forwards  = self.heuristic(pancakes) 
		self.total_score = self.backwards + self.forwards
	def heuristic(self, pancakes):
		h = 0
		for i in range(len(self.pancakes) - 1):
			h += 1 if abs(self.pancakes[i] - self.pancakes[i+1]) > 1 else 0
		return h

def flip(pancakes, i):
	if i == 0:
		pancakes.reverse()
		return pancakes
	flippy = pancakes[-i:]
	flippy.reverse()
	end = len(pancakes) - i
	return pancakes[:end] + flippy

def generate_successors(smallest):
	successors = set()
	for i in range(1, len(smallest.pancakes)): # can't flip zero pancakes
		successors.add(Node(flip(smallest.pancakes, i+1), smallest.backwards + i))
	return successors

def isGoal(node):
	return True if node.forwards == 0 else False


def A_star(initial_node, generate_successors, isGoal):
	i = 1
	path, expanded, frontier = {}, {}, {str(initial_node.pancakes) : initial_node}
	successors = set()
	while frontier: 
		key, smallest = min(frontier.items(), key=lambda pair: pair[1].total_score)
		print("Smallest: {} ({})".format(key, i))
		i += 1
		frontier.pop(key)
		if isGoal(smallest):
			if smallest.pancakes[0] < smallest.pancakes[-1]:
				return flip(smallest.pancakes, 0), path
			else:
				return smallest.pancakes, path
		path[str(smallest.pancakes)] = smallest
		expanded[str(smallest.pancakes)] = smallest
		successors = generate_successors(smallest)
		for successor in successors:
			if str(successor.pancakes) in frontier:
					frontier[str(successor.pancakes)] = min(successor, frontier[str(successor.pancakes)], key=lambda node: node.total_score )
			else:
				if not str(successor.pancakes) in expanded:
					frontier[str(successor.pancakes)] = successor
			expanded[str(successor.pancakes)] = successor
		print("."*50)
	return None

if __name__ == '__main__':
	pancakes = [i for i in range(1,6)]
	random.shuffle(pancakes)
	initial_node = Node(pancakes, 0)
	stack, path = A_star(initial_node, generate_successors, isGoal)
	for step in path:
		print("{} ---> ".format(step), end=" ")
	print(stack)
