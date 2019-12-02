import sys
from operator import add, mul

def run_intcode(code):
	pc = 0
	while pc >= 0 and pc < len(code) and code[pc] != 99:
		op, arg1, arg2, dst = code[pc:pc+4]
		if op == 1:
			fun = add
		elif op == 2:
			fun = mul
		else:
			break
		code[dst] = fun(code[arg1], code[arg2])
		pc += 4
	return code[0]

with open(sys.argv[1]) as f:
	code = list(map(int, f.read().split(',')))

if sys.argv[2] == '1':
	code[1] = 12
	code[2] = 2
	print(run_intcode(code))
else:
	for i in range(100):
		for j in range(i + 1):
			code_copy = list(code)
			code_copy[1:3] = [i, j]
			if run_intcode(code_copy) == 19690720:
				print(100 * i + j)
				sys.exit()
