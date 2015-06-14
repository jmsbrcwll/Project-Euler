
cached_primes = set()

def run():
	max_a = max_b = 0
	max_primes = 0

	for i in range(-999, 1000):
		for j in range(-999, 1000):
			num_primes =  get_primes(i,j)
			if num_primes > max_primes:
				max_a = i
				max_b = j
				max_primes = num_primes

	print max_a * max_b

def get_primes(a, b):
	n = 0
	while is_prime(n**2 + a*n + b):
		n += 1

	return n

def is_prime(n):
	global cached_primes

	if n <= 0:
		return False
	if n in cached_primes:
		return True

	for i in range(2,n):
		if n % i == 0:
			return False

	cached_primes.add(n)
	return True
		

if __name__ == "__main__":
	run()
