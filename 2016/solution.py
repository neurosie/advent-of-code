import re
input = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn""".split('\n')

with open("07_input.txt") as f:
	input = f.read().strip().split('\n')
	
	prog = re.compile(r'.*(.)(?!\1)(.)\2\1.*')
	negative = re.compile(r'.*\[.*(.)(?!\1)(.)\2\1.*\].*')
	count = 0
	for line in input:
		if prog.match(line) and not negative.match(line):
			count += 1
		elif count < 10 and negative.match(line):
			print(line)
	print(count)