def fizz_buzz(n):
	'''
		Return 'fizz' when 'n' is divisible by 3
		return 'buzz' when 'n' is divisible by 5
		return 'fizzbuzz' when 'n' is divisible by both 3 and 5
	'''

	if n % 3 == 0 and n % 5 == 0:
		return 'FizzBuzz'
	elif n % 3 == 0:
		return 'Fizz'
	elif n % 5 == 0:
		return 'Buzz'
	else:
		return n