import md5

input = "abbhdwsy"
# input = "abc"
password = ["_" for x in range(8)]
index = 0

m = md5.new(input)

while "_" in password:
	m2 = m.copy()
	m2.update(str(index))
	hash = m2.hexdigest()
	if hash[0:5] == "00000":
		if int(hash[5],16) < 8 and password[int(hash[5])] == "_":
			password[int(hash[5])] = hash[6]
			print("".join(password))
	index += 1
print("".join(password))