import sys
part = 2

gens = 50000000000 if part == 2 else 20

def pot_sum(pots, offset):
    return sum((p == "#") * (i + offset) for i, p in enumerate(pots))

with open(sys.argv[1]) as f:
    lines = f.read().rstrip().split("\n")
pots = "..." + lines[0].split(" ")[2] + "..."
offset = -3
rules = {}
for line in lines[2:]:
    r = line.split(" => ")
    rules[r[0]] = r[1]

diffs = []
s = pot_sum(pots, offset)
for g in range(gens):
    new_pots = ""
    for i in range(len(pots) - 4):
        state = pots[i:i+5]
        new_pots += rules[state] if state in rules else "."
    l = new_pots.find("#")
    r = len(new_pots) - new_pots.rfind("#") - 1
    pots = "." * (3 - l) + new_pots + "." * (3 - r)
    offset += l - 1
    new_sum = pot_sum(pots, offset)
    diffs.append(new_sum - s)
    s = new_sum
    if len(diffs) > 10:
        if len(set(diffs[-10:])) == 1:
            print(s + diffs[-1] * (gens - g - 1))
            sys.exit()

print(pot_sum(pots, offset))
