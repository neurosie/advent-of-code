import sys
part = 2

if part == 1:
    input = int(sys.argv[1])
else:
    input = list(int(c) for c in sys.argv[1])
scoreboard = [3, 7]
one = 0
two = 1

while True:
    x = scoreboard[one] + scoreboard[two]
    scoreboard += [int(c) for c in str(x)]
    one = (one + scoreboard[one] + 1) % len(scoreboard)
    two = (two + scoreboard[two] + 1) % len(scoreboard)
    if part == 1:
        if len(scoreboard) >= input + 10:
            print("".join(str(x) for x in scoreboard[input:input + 10]))
            break
    else:
        if len(scoreboard) > len(input):
            if scoreboard[-len(input):] == input:
                print(len(scoreboard) - len(input))
                break
            elif scoreboard[-len(input) - 1: -1] == input:
                print(len(scoreboard) - len(input) - 1)
                break
