import sys

part = 2

with open(sys.argv[1]) as f:
    map = [list(l) for l in f.read().split('\n')[:-1]]

carts = []
locs = set()

for y, row in enumerate(map):
    for x, c in enumerate(row):
        if c in ['>', '<', '^', 'v']:
            carts.append([y, x, c, 0])
            locs.add((y, x))
            if c == '>' or c == '<':
                map[y][x] = '-'
            else:
                map[y][x] = '|'

delta = {
    '>' : (1, 0), '<' : (-1, 0), 'v' : (0, 1), '^' : (0, -1)
}
compass = ['^', '>', 'v', '<']
turn = {
    '/' : {
        '^' : '>', '>' : '^', 'v' : '<', '<' : 'v'
    },
    '\\' : {
        '^' : '<', '<' : '^', 'v' : '>', '>' : 'v'
    }
}

while True:
    carts.sort(key=lambda x: (x[0], x[1]))
    to_remove = []
    for i, [y, x, dir, turns] in enumerate(carts):
        if i in to_remove:
            continue
        locs.remove((y, x))
        x += delta[dir][0]
        y += delta[dir][1]
        if (y, x) in locs:
            if part == 1:
                print(x, y)
                sys.exit()
            else:
                locs.remove((y, x))
                to_remove.append(i)
                to_remove.append(next(j for j in range(len(carts))
                        if j != i and carts[j][0] == y and carts[j][1] == x))
                continue
        locs.add((y, x))
        if map[y][x] in turn:
            dir = turn[map[y][x]][dir]
        elif map[y][x] == '+':
            if turns % 3 == 0:
                dir = compass[(compass.index(dir) - 1) % 4]
            elif turns % 3 == 2:
                dir = compass[(compass.index(dir) + 1) % 4]
            turns += 1
        carts[i] = [y, x, dir, turns]
    if len(to_remove) > 0:
        carts = [c for i, c in enumerate(carts) if i not in to_remove]
        if len(carts) == 1:
            print(carts[0][1], carts[0][0])
            sys.exit()
