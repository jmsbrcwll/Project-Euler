#takes a list of ordered digits and
#yields a list of ordered permutations of those digits.
#assumes digits are in sorted order
def ordered_permutations(n):
	if len(n) == 2:
		yield n 
		yield [n[1], n[0]]

	for i in n:
		other_digits = [d for d in n if d != i] 
		perms = ordered_permutations(other_digits)
		for perm in ordered_permutations(other_digits):
			yield [i] + perm

if __name__ == '__main__':
	count = 0
	for i in  ordered_permutations([0,1,2,3,4,5,6,7,8,9]):
		count += 1
		if count == 1000000:
			print ''.join(map(str,i))
			break
