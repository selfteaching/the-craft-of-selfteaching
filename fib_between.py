def fib_between(start, end):
	a, b = 0, 1
	while a < end:
		if a >= start:
			print(a, end=' ')
		a, b = b, a + b

fib_between(1, 100)
