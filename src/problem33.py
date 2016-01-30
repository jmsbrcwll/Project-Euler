from decimal import Decimal
from fractions import Fraction

def isCuriousFraction(i, j):
	orig_frac = Decimal(i)/Decimal(j)
	i_digits = map(int,str(i))
	j_digits = map(int,str(j))
	if 0 in i_digits or 0 in j_digits or i_digits == j_digits:
		return False

	if i_digits[1] == j_digits[0]:
		if Decimal(i_digits[0]) / Decimal(j_digits[1]) == orig_frac:
			return True

	return False

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):
    return reduce(lcm, args)

def run():
	curious_fractions = []
	for i in range(10, 100):
		for j in range(10, 100):
			if isCuriousFraction(i, j):
				curious_fractions.append((i,j))

	denominators = tuple([f[1] for f in curious_fractions])
	lcm_ = lcmm(*denominators)
	
	total_numerator = 1
	for frac in curious_fractions:
		total_numerator *= frac[0] * (lcm_ / frac[1])
	
	print Fraction (total_numerator, lcm_**len(curious_fractions)).denominator

if __name__ == "__main__":
	run()
