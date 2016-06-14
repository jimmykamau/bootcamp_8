def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.append(i)
    return i
    
def get_primes(n):
	
	# Validate input
	if n <= 0:
		return "Invalid number"
	
	primes = [] # Empty list to hold prime numbers
	i, p = 2, 0 # i=first prime number, p=number of prime numbers found
	while True:
	    if prime(i, primes):
	        p += 1
	        if p == n:
	            return primes
	    i += 1

nth = 50 # 50 prime numbers
primes_list = get_primes(nth) # Get first 50 prime numbers
print(primes_list) 

# Test prime-checking functions
'''
def test_primes(n, prime_list):
 	# Generate list of prime numbers using sieve algorithm
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    new_primes = [2] + [i for i in xrange(3,n,2) if sieve[i]]

    if new_primes != prime_list:
    	return "Failed"
    else:
    	return "Passed"

last_prime = primes_list[-1]+1
print (test_primes(last_prime, primes_list))
'''
# End tests