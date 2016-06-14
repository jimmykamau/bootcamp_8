# Displays the first n fibonacci numbers
def fib(n):
	a = [0]
	b,c = 1,0
	for i in range(n-1):
		a.append(b)
		b,c = c+b, b
	return a

#print(fib(10))