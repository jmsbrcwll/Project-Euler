
def run():
	palindromic_numbers = [
		i
		for i in range(1, 1000000)
		if is_palindromic_both_bases(i)
	]
	print palindromic_numbers
	print sum(palindromic_numbers)

def is_palindromic_both_bases(i):
	print i
	return is_palindromic(i) and is_palindromic("{0:b}".format(i))

def is_palindromic(i):
	i_str = str(i)
	print i_str
	return i_str == i_str[::-1]

if __name__ == "__main__":
	run()
