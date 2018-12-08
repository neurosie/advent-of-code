import sys

part = 2

with open(sys.argv[1], 'r') as f:
    # cloth = [[0 for _ in range(1000)] for _ in range(1000)]
    cloth = dict()
    ids = set()
    overlapped = set()
    count = 0
    for line in f:
        line = line.split(' ')
        id = int(line[0][1:])
        coords = line[2].split(',')
        x = int(coords[0])
        y = int(coords[1][:-1])
        size = line[3].split('x')
        w = int(size[0])
        h = int(size[1])
        for i in range(x, x+w):
            for j in range(y, y+h):
                if part == 1:
                    if (i, j) not in cloth:
                        cloth[(i, j)] = 1
                    else:
                        cloth[(i, j)] += 1
                        if cloth[(i, j)] == 2:
                            count += 1
                else:
                    if (i, j) not in cloth:
                        cloth[(i, j)] = id
                        if id not in overlapped:
                            ids.add(id)
                    else:
                        ids.discard(cloth[(i, j)])
                        ids.discard(id)
                        overlapped.add(cloth[(i, j)])
                        overlapped.add(id)
    if part == 1:
        print(count)
    else:
        print(repr(ids))
