def main():
	highest_length = 0
	highest = 0
	
	for i in range(1,1000000):
   	   length = getCollatzSequence(i)
	   if length > highest_length:
		highest_length = length
		highest = i

	print(highest)	
	


def getCollatzSequence(n):
	 head = n
	 length = 1
	 while head != 1:
		  head = nextNumber(head)
	 	  length += 1
         return length
			
		


def nextNumber(n):
	if n%2 == 0:
		return n/2
	else:
		return 3*n + 1


main()
