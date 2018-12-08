import math

with open('01_input.txt') as f:
	turns = f.read().strip().split(', ')
	# turns = 'R8, R4, R4, R8'.split(', ')
	loc = [0, 0]
	dir = [0, 1]
	
	locs = {tuple(loc)}
	found = False
	
	for t in turns:
		angle = math.atan2(dir[1],dir[0]) + (math.pi / 2 if t[0] == 'L' else  -math.pi / 2)
		dir[0] = int(math.cos(angle))
		dir[1] = int(math.sin(angle))
		for i in range(int(t[1:])):
			loc[0] += dir[0]
			loc[1] += dir[1]
			# print(loc)
			if loc[0] == 75 and loc[1] == -4:
				print(tuple(loc) in locs)
			
			if tuple(loc) in locs:
				found = True
				break
			locs.add(tuple(loc))
		if found:
			break
		
	print(loc)
	print(abs(loc[0]) + abs(loc[1]))