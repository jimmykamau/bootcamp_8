# Generate Fibonacci sequence from 0 to n
def fib(n):
	a = [0]
	b,c = 1,0
	for i in range(n):
		a.append(b)
		b,c = c+b, b
		if b>n:
			return a

#print(fib(20))