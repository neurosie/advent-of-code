import sys

part = 2

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

coords = []
with open(sys.argv[1]) as f:
    for line in f:
        coords.append([int(x) for x in line.rstrip().split(', ')])

upleft = [min(coords, key=lambda x: x[i])[i] for i in range(2)]
downright = [max(coords, key=lambda x: x[i])[i] for i in range(2)]

coords = [[c[i] - upleft[i] for i in range(2)] for c in coords]
downright = [downright[i] - upleft[i] for i in range(2)]

if part == 1:
    areas = [0 for _ in range(len(coords))]
    infinite = set()
    for i in range(downright[0] + 1):
        for j in range(downright[1] + 1):
            dists = [distance([i, j], c) for c in coords]
            argmin = min(range(len(dists)), key=lambda x: dists[x])
            if dists.count(dists[argmin]) > 1:
                continue
            areas[argmin] += 1
            if (i == 0 or i == downright[0] or
                j == 0 or j == downright[1]):
                infinite.add(argmin)

    max = 0
    for i, area in enumerate(areas):
        if area > max and i not in infinite:
            max = area
    print(max)
else:
    area = 0
    for i in range(downright[0] + 1):
        for j in range(downright[1] + 1):
            if sum(distance([i, j], c) for c in coords) < 10000:
                area += 1
    print(area)
