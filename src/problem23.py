import math
def run():
	abundant_nums = [n for n in xrange(1,28124) if is_abundant(n)]
	abundant_sum = sum({i for i in abundant_sums(abundant_nums, 28123)})
	sum_all = sum(i for i in xrange(1, 28124))
	print 'total:%s' % (sum_all - abundant_sum) 

def abundant_sums(abundant_nums, n):
	for i in abundant_nums:
		for j in abundant_nums:
			sum_ = i + j
			if sum_ <= n :
				yield sum_

def is_abundant(n):
	total = 0
	for i in xrange(1, int((n/2) + 1)):
		if n % i == 0:
			total += i

	return total > n

if __name__ == '__main__':
	run()

