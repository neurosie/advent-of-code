import sys
import operator

def get_arg(code, a):
	val, mode = a
	return val if mode else code[val]

def basic_op(op, code, a, b, c):
	code[c[0]] = int(op(get_arg(code, a), get_arg(code, b)))

def read_in(code, address):
	code[address[0]] = int(input())

def print_out(code, address):
	print(get_arg(code, address))

def jump_if(val, code, tst, goto):
	if bool(get_arg(code, tst)) == val:
		return get_arg(code, goto)

def partial(f, a):
	return lambda *x: f(a, *x)

opcodes = {
	'01': (3, partial(basic_op, operator.add)),
	'02': (3, partial(basic_op, operator.mul)),
	'03': (1, read_in),
	'04': (1, print_out),
	'05': (2, partial(jump_if, True)),
	'06': (2, partial(jump_if, False)),
	'07': (3, partial(basic_op, operator.lt)),
	'08': (3, partial(basic_op, operator.eq)),
}

def run_intcode(code):
	pc = 0
	while pc >= 0 and pc < len(code) and code[pc] != 99:
		instr = str(code[pc]).zfill(5)
		opcode = instr[-2:]
		if opcode not in opcodes:
			break
		arity, fun = opcodes[opcode]
		pc += 1
		args = zip(code[pc : pc + arity], reversed(list(map(int, instr[:-2]))))
		pc += arity
		ret = fun(code, *args)
		if ret is not None:
			pc = ret

with open(sys.argv[1]) as f:
	code = list(map(int, f.read().split(',')))

run_intcode(code)