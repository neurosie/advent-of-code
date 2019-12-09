import sys

width = 25
height = 6
with open(sys.argv[1]) as f:
	data = f.read().strip()
	layers = len(data) // width // height
	if layers * width * height != len(data):
		sys.exit()
	image = [[[int(data[i * height * width + j * width + k]) for k in range(width)] 
				for j in range(height)] for i in range(layers)]

if sys.argv[2] == '1':
	the_layer = min((sum(1 for row in layer for x in row if x == 0), i) 
						   for i, layer in enumerate(image))[1]
	print(sum(1 for row in image[the_layer] for x in row if x == 1) * 
		  sum(1 for row in image[the_layer] for x in row if x == 2))
else:
	# we don't support transparency here
	decoded = [[next(image[k][i][j] for k in range(layers) if image[k][i][j] != 2) 
				for j in range(width)] for i in range(height)]
	for row in decoded:
		print(''.join(' ' if x == 0 else 'X' for x in row))
