CACHED_PRIMES = set()
EVEN_DIGITS = {'2', '4', '6', '8'}
def run():
	
	#eligable numbers cannot contain any even digits
	
	eligable_primes = [i for i in range(2, 1000000) if contains_no_even_digits(i) ]
	primes = [i for i in eligable_primes if is_circular(i)]
	print len(primes)

def contains_no_even_digits(n):
	digits = set(str(n))
	return digits.difference(EVEN_DIGITS) == digits

def is_circular(n):
	return all([is_prime(i) for i in circulated_versions(n)])

def circulated_versions(n):
	digits = list(str(n))
	for i in digits:
		yield int(''.join(digits))
		digits.insert(0, digits.pop())
	
	return

def is_prime(n):
	if n in CACHED_PRIMES:
		return True

	for i in xrange(2, n):
		if n % i == 0:
			return False

	CACHED_PRIMES.add(n)
	return True	

if __name__ == "__main__":
	run()


