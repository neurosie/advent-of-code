with open('03_input.txt') as f:
	data = f.read().strip().split('\n')
	
	count = 0
	
	for i in range(len(data)):
		sides = [int(data[i/3*3+x].split()[i%3]) for x in range(3)]
		possible = True
		for j in range(3):
			if sides[j] >= sides[(j+1)%3] + sides[(j+2)%3]:
				possible = False
				break
		if possible:
			count += 1
	print(count)