import sys, math

part = 1

points = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.split(",")
        points.append(((int(line[0].split("<")[1]),
                        int(line[1].split(">")[0])),
                       (int(line[1].split("<")[1]),
                        int(line[2].split(">")[0]))))

def advance(points, t):
    for i, ((x, y), (vx, vy)) in enumerate(points):
        points[i] = ((x + vx * t, y + vy * t), (vx, vy))

def grid_dims(points):
    min_x = min(points, key=lambda x: x[0][0])[0][0]
    max_x = max(points, key=lambda x: x[0][0])[0][0]
    min_y = min(points, key=lambda x: x[0][1])[0][1]
    max_y = max(points, key=lambda x: x[0][1])[0][1]
    return min_x, max_x, min_y, max_y

def print_grid(points):
    min_x, max_x, min_y, max_y = grid_dims(points)
    grid = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for ((x, y), _) in points:
        grid[y - min_y][x - min_x] = '#'
    for row in grid:
        print("".join(row))

def grid_size(dims):
    return abs(dims[1]-dims[0]) + abs(dims[3]-dims[2])

time = 0

for ((x, y), (vx, vy)) in points:
    if x < 0:
        advance(points, int(-x/vx))
        time += int(-x/vx)

for ((x, y), (vx, vy)) in points:
    if y < 0:
        advance(points, int(-y/vy))
        time += int(-y/vy)
dims = grid_dims(points)
size = grid_size(dims)

while True:
    advance(points, 1)
    time += 1
    new_dims = grid_dims(points)
    new_size = grid_size(new_dims)
    if new_size > size:
        advance(points, -1)
        time -= 1
        break
    size = new_size
# print(dims, size)
print_grid(points)
print(time)
