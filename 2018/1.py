import sys

with open(sys.argv[1], 'r') as f:
    freq = 0
    freqs = set()
    freqs.add(0)
    lines = []
    for line in f:
        lines.append(int(line))
    while True:
        for line in lines:
            freq += line
            if freq in freqs:
                print("first double:", freq)
                sys.exit()
            freqs.add(freq)
    print(freqs)
    print(freq)
