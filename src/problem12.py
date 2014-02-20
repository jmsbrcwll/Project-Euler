def main():
	i = 2
	finished = False
	while not finished :
		#create the ith triangle number	
		triangle = sum(range(1,i))
		
		#check number of factors
		if len(factors(triangle)) > 500:
			print(triangle)
			finished = True
		i += 1

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))	


main()
