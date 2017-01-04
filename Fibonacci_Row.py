# Fibonacci

count = int(raw_input("How many fibonacci numbers need to be generated: "))

c = 1



a = 0

b = 1

line = 1

while c <= count:
	old_a = a
	old_b = b

	a = old_b
	b = old_a + old_b

	print "%03d: %d" % (line, old_a)
	
	c = c + 1
	
	line = line + 1
