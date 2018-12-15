serial = 9798
size = 300
grid = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):
	for j in range(size):
		rack = i + 11
		grid[i][j] = ((rack * (j + 1) + serial) * rack) // 100 % 10 - 5

best = (None, 0)
partial = [[[0 for _ in range(size-i)] for _ in range(size-i)] for i in range(size)]

partial[0] = grid

for s in range(1,size):
	print(s+1)
	for i in range(size - s):
		for j in range(size - s):
			if s % 2 == 0:
				partial[s][i][j] = partial[s//2][i][j]
				partial[s][i][j] += partial[s//2-1][i+s//2+1][j]
				partial[s][i][j] += partial[s//2-1][i+s//2+1][j+s//2]
				partial[s][i][j] += partial[s//2-1][i][j+s//2+1]
				partial[s][i][j] += partial[s//2-1][i+s//2][j+s//2+1]
				if s > 2:
					partial[s][i][j] -= partial[s//2-2][i+s//2+1][j+s//2+1]
				partial[s][i][j] += partial[0][i+s][j+s]
			else:
				partial[s][i][j] = (partial[s//2][i][j] +
									partial[s//2][i][j+s//2+1] +
								    partial[s//2][i+s//2+1][j] +
								    partial[s//2][i+s//2+1][j+s//2+1])

			p = partial[s][i][j]
			if p > best[1]:
				best = ((i+1, j+1, s+1), p)
print(best)
