def run():
	count = 1
	for i in fibonacci():
		if len(str(i)) == 1000:
			print count
			break
		count += 1

def fibonacci():
	n_minus_one = 1
	n_minus_two = 1
	yield 1
	yield 1
	while True:
		n = n_minus_one + n_minus_two
		n_minus_two = n_minus_one
		n_minus_one = n
		yield n

if __name__ == '__main__':
	run()
