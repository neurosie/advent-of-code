import sys, itertools
from collections import Counter
from operator import eq

start = '353096'
end = '843212'

part = sys.argv[1]

def choices(prevs):
	if len(prevs) == 6:
		if ((part == '1' and 
			any(map(lambda x: eq(*x), zip(prevs[:-1], prevs[1:])))) or
			(part == '2' and
			any(map(lambda x: x == 2, Counter((prevs)).values())))):
			yield prevs
		return
	for i in range(0 if len(prevs) == 0 else int(prevs[-1]), 10):
		stub = prevs + str(i)
		if stub + '0' * (6 - len(prevs)) > end:
			return
		if stub + '9' * (6 - len(prevs)) < start:
			continue
		for c in choices(stub):
			yield c

print(sum(1 for _ in choices('')))
