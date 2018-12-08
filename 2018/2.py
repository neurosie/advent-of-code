import sys

part = 2

with open(sys.argv[1], 'r') as f:
    if part == 1:
        two_count = 0
        three_count = 0
        for line in f:
            twos = set()
            threes = set()
            chars = dict()
            for c in line:
                if c not in chars:
                    chars[c] = 0
                chars[c] += 1
                if chars[c] == 2:
                    twos.add(c)
                elif chars[c] == 3:
                    twos.remove(c)
                    threes.add(c)
                elif chars[c] == 4:
                    threes.remove(c)
            if len(twos):
                two_count += 1
            if len(threes):
                three_count += 1
        print(two_count * three_count)
    else:
        partials = set()
        for line in f:
            for i in range(len(line)):
                w = line[:i] + line[i+1:]
                if (w, i) in partials:
                    print(w)
                    sys.exit()
                partials.add((w, i))
