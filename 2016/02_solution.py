import math

with open('02_input.txt') as f:
	data = f.read().strip()
	# data = ("ULL\n"
			# "RRDDD\n"
			# "LURDL\n"
			# "UUUUD")
	grid = [['X','X','1','X','X'],
			['X','2','3','4','X'],
			['5','6','7','8','9'],
			['X','A','B','C','X'],
			['X','X','D','X','X']]
	loc = [2,0]
	code = ""

	
	for line in data.split('\n'):
		for char in line:
			if char == 'U':
				if loc[0] != 0 and grid[loc[0]-1][loc[1]] != 'X':
					loc[0] -= 1
			elif char == 'D':
				if loc[0] != len(grid)-1 and grid[loc[0]+1][loc[1]] != 'X':
					loc[0] += 1
			elif char == 'L':
				if loc[1] != 0 and grid[loc[0]][loc[1]-1] != 'X':
					loc[1] -= 1
			elif loc[1] != len(grid)-1 and grid[loc[0]][loc[1]+1] != 'X':
				loc[1] += 1
		code += grid[loc[0]][loc[1]]
	print(code)

	# if char == 'U' and loc > 3:
				# loc -= 3
			# elif char == 'D' and loc < 7:
				# loc += 3
			# elif char == 'L' and loc % 3 != 1:
				# loc -= 1
			# elif char == 'R' and loc % 3 != 0:
				# loc += 1
		# code += str(loc)