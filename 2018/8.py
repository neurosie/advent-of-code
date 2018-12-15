import sys

part = 2

with open(sys.argv[1]) as f:
    stream = [int(n) for n in f.read().rstrip().split(' ')]

def parse(stream, i, depth = 0):
    # nodes = stream[i]
    # entries = stream[i+1]
    # print(depth * '  ', nodes, entries)
    children = []
    pos = i + 2
    for _ in range(stream[i]):
        child, pos = parse(stream, pos, depth + 1)
        # print('  ' * depth, child)
        children.append(child)

    metadata = stream[pos:pos+stream[i+1]]
    # print('  ' * depth, children, metadata, i, pos+stream[i+1])
    return (children, metadata), pos+stream[i+1]

def sum_metadata(tree):
    return sum(sum_metadata(n) for n in tree[0]) + sum(tree[1])

def tree_value(tree):
    if len(tree[0]) == 0:
        return sum(tree[1])
    else:
        vals = [tree_value(n) for n in tree[0]]
        return sum(vals[m-1] if m > 0 and m <= len(vals) else 0 for m in tree[1])

tree, _ = parse(stream, 0)

if part == 1:
    print(sum_metadata(tree))
else:
    print(tree_value(tree))
