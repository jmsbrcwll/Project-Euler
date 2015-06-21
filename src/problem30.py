def run():
	total = 0
	for i in range (2,1000001):
		if is_fifth_power_number(i):
			print 'is a fifth power number: %s' % i
			total += i

	print 'total: %s' % total
def is_fifth_power_number(num):
	total = sum([int(d)**5 for d in str(num)])
	return total == num


if __name__ == "__main__":
	run()
