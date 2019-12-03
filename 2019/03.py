import sys
from operator import add
from collections import Counter

with open(sys.argv[1]) as f:
	wires = [map(lambda x: (x[0], int(x[1:])), line.split(',')) for line in f]

direction_map = {
	"R": (1, 0),
	"L": (-1, 0),
	"U": (0, 1),
	"D": (0, -1),
}
def advance(coord, direction):
	return tuple(map(lambda x: add(*x), zip(coord, direction_map[direction])))

best = float('inf')
grid = Counter()
for i, wire in enumerate(wires):
	coord = (0, 0)
	steps = 0
	for direction, length in wire:
		for _ in range(length):
			coord = advance(coord, direction)
			if sys.argv[2] == '1':
				grid[coord] += 1
				if grid[coord] > 1:
					best = min(best, sum(map(abs, coord)))
			else:
				steps += 1
				if i == 0:
					grid[coord] = steps
				elif coord in grid:
					best = min(best, steps + grid[coord])

print(best)
