import sys
from collections import deque

players = int(sys.argv[1])
marbles = int(sys.argv[2])
scores = [0 for _ in range(players)]

circle = deque([0])
for m in range(1, marbles + 1):
    if m % 23 == 0:
        scores[m % players] += m
        circle.rotate(-7)
        scores[m % players] += circle.pop()
    else:
        circle.rotate(2)
        circle.append(m)
print(max(scores))
