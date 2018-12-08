with open('04_input.txt') as f:
	data = f.read().strip().split('\n')
	# data = ("aaaaa-bbb-z-y-x-123[abxyz]\n"
			# "a-b-c-d-e-f-g-h-987[abcde]\n"
			# "not-a-real-room-404[oarel]\n"
			# "totally-real-room-200[decoy]").split('\n')
	
	for line in data:
		chars = ''.join(line.split('-')[:-1])
		uniques = list(set(list(chars)))
		counts = {x: chars.count(x) for x in uniques}
		uniques.sort()
		uniques.sort(key=lambda x: counts[x], reverse=True)
		checksum = ''.join(uniques[0:5])
		if checksum == line.split('[')[1].split(']')[0]:
			id = int(line.split('[')[0].split('-')[-1])
			
			decoded = ""
			for c in '-'.join(line.split('-')[:-1]):
				if c == '-':
					decoded += ' '
				else:
					decoded += chr((ord(c) - 97 + id) % 26 + 97)
			if "north" in decoded:
				print(str(id) + ": " + decoded)