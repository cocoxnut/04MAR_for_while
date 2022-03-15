for x in range(-100,1000):
	if x >= 100:
		print(x, "1st IF")
	if x < 0:
		print(x, "2nd IF")
	if x % 2 == 0:
		print(x, "3rd IF")
	if x % 31 == 0:
		print(x, "4th IF")
	if x > 100 and x % 17 == 0 or x > 150 and x == 13 ** 2:
		print(x, "5th IF")

