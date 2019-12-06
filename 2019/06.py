import sys
from collections import defaultdict

orbit_map = defaultdict(set)
adjacency = defaultdict(set)
with open(sys.argv[1]) as f:
	for line in f:
		src, dst = line.strip().split(')')
		orbit_map[src].add(dst)
		adjacency[src].add(dst)
		adjacency[dst].add(src)

def indirect_orbits(root, depth = 0):
	return depth + sum(indirect_orbits(sat, depth + 1) for sat in orbit_map[root])

def min_transfers(src, dst):
	queue = [(src, 0)]
	visited = set((src))
	while len(queue):
		v, dist = queue.pop(0)
		if v == dst:
			return dist - 2
		for w in adjacency[v]:
			if w not in visited:
				visited.add(w)
				queue.append((w, dist + 1))

if sys.argv[2] == '1':
	print(indirect_orbits('COM'))
else:
	print(min_transfers('YOU', 'SAN'))