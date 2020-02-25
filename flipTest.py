def flip(pancakes, i):
	flippy = pancakes[-i:]
	flippy.reverse()
	end = len(pancakes) - i
	print(pancakes[:end] + flippy)

if __name__ == '__main__':
	pancakes = [i for i in range(1, 11)]

	#for j in range(1, len(pancakes)):
	#	flip(pancakes, j+1)
	#	print("-"*50)