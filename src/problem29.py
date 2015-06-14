def run():
	terms = {t for t in power_terms()}
	print len(terms)

def power_terms():
	for a in range (2, 101):
		for b in range(2,101):
			yield a**b

if __name__ == '__main__':
	run()
