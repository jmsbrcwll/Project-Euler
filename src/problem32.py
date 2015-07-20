
def run():
	products = set()
	for i in range(1, 10000):
		for j in range(1, 10000):
			product = i * j
			digits = str(i) + str(j) + str(product)
			if is_pandigital(digits):
				products.add(product)

	print 'total: %s' % sum(products)


def is_pandigital(digits):
	return set(digits) == set('123456789') and len(digits) == 9

if __name__ == "__main__":
	run()
