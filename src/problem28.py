
def run():
	diag_total = 0
	start = 1
	for i in range(2,502):
		start, diagonals = next_level(start,i)
		diag_total += sum(diagonals)	
	print diag_total + 1


def next_level(start, curr_level):
	size  = (2*curr_level) -1
	#bottom_right = start + (length - 1)
	#bottom_left = bottom_right + (width - 1)
	#top_left = bottom_left + (length -1)
	#top_right = top_left + (width - 1)
	prev = start
	diagonals = []
	for i in range(1,5):
		next_ = prev + size - 1
		diagonals.append(next_)
		prev = next_

	return diagonals[-1], diagonals 	

if __name__ == '__main__':
	run()
