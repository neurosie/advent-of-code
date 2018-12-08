import sys

part = 2

def reactable(l, r):
    return l != r and l.lower() == r.lower()

def reacted_length(polymer, skip=None):
    index = 0
    built = []
    for c in polymer:
        if c.lower() == skip:
            continue
        built.append(c)
        while len(built) >= 2 and reactable(built[-1], built[-2]):
            del built[-1]
            del built[-1]
    return len(built)

with open(sys.argv[1], 'r') as f:
    polymer = f.read().rstrip()

    if part == 1:
        print(reacted_length(polymer))
    else:
        units = set(c.lower() for c in polymer)
        print(min(reacted_length(polymer, skip=c) for c in units))
