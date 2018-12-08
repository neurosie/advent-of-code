from collections import Counter
input = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""".split('\n')

with open("06_input.txt") as f:
	input = f.read().strip().split('\n')
	
	print("".join([Counter([line[i] for line in input]).most_common(1)[0][0] for i in range(len(input[0]))]))
	