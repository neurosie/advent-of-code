import sys
import operator
import itertools
from dataclasses import dataclass, field

@dataclass
class ProgramState:
	code: list
	in_buf: list = field(default_factory=list)
	out_buf: list = field(default_factory=list)
	pc: int = 0

def get_arg(code, a):
	val, mode = a
	return val if mode else code[val]

def basic_op(op, state, a, b, c):
	state.code[c[0]] = int(op(get_arg(state.code, a), get_arg(state.code, b)))

def read_in(state, address):
	state.code[address[0]] = state.in_buf.pop(0)

def print_out(state, address):
	state.out_buf.append(get_arg(state.code, address))

def jump_if(val, state, tst, goto):
	if bool(get_arg(state.code, tst)) == val:
		return get_arg(state.code, goto)

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

def run_intcode(state, halt_on_output = False):
	while state.pc >= 0 and state.pc < len(state.code) and state.code[state.pc] != 99:
		instr = str(state.code[state.pc]).zfill(5)
		opcode = instr[-2:]
		if opcode not in opcodes:
			break
		arity, fun = opcodes[opcode]
		args = zip(state.code[state.pc + 1:state.pc + 1 + arity],
					reversed(list(map(int, instr[:-2]))))
		ret = fun(state, *args)
		if ret is not None:
			state.pc = ret
		else:
			state.pc += arity + 1
		if halt_on_output and len(state.out_buf):
			return

def run_amps(code, phase_settings, feedback = False):
	amps = [ProgramState(list(code), [phase_settings[i]]) for i in range(5)]
	signal = 0
	last_signal = 0
	while True:
		for i in range(5):
			amps[i].in_buf.append(signal)
			run_intcode(amps[i], True)
			if not len(amps[i].out_buf):
				return last_signal
			signal = amps[i].out_buf.pop(0)
		last_signal = signal
		if not feedback:
			return last_signal

def max_amps(code, feedback = False):
	return max(run_amps(code, settings, feedback) for settings in 
		itertools.permutations(range(5,10) if feedback else range(5)))


with open(sys.argv[1]) as f:
	code = list(map(int, f.read().split(',')))

if sys.argv[2] == '1':
	print(max_amps(code))
else:
	print(max_amps(code, True))
