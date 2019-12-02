import sys

with open(sys.argv[1]) as f:
	modules = map(int, f.read().split())

def fuel_required(mass: int) -> int:
	ans = 0
	while True:
		fuel = mass // 3 - 2
		if fuel <= 0:
			return ans
		ans += fuel
		mass = fuel

if sys.argv[2] == '1':
	print(sum(map(lambda x: x // 3 - 2, modules)))
else:
	print(sum(map(fuel_required, modules)))
