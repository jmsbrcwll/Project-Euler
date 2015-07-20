"""
Upper limit for digits:
Highest digit factorial = 9! = 362880
Therefore, for an n-digit number, 362880n is the highest
possible number to achieve. We can see for n=7,
362880 x 7 < 9999999
"""
factorial = {
	'0' : 0,
	'1' : 1,
	'2' : 2,
	'3' : 6,
	'4' : 24,
	'5' : 120,
	'6' : 720,
	'7' : 5040,
	'8' : 40320,
	'9' : 362880,
}

total = 0

for i in range(3, 10000000):
	d_sum = sum([factorial[d] for d in str(i)])
	if d_sum == i:
		total += d_sum

print 'total:%s' % total
