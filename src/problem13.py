with open('problem_13_numbers.txt', 'r') as file:
	nums = file.readlines()
	
nums  = [int(num.rstrip('\n')) for num in nums]	
		
print "total:%s" % sum(nums) 

