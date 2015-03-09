def build_pyramid():	
	with open('problem_18_numbers.txt', 'r') as file:
		lines = file.readlines()

	return [map(int,line.rstrip('\n').split(' ')) for line in lines]
	
def try_all_paths(level, loc):
	paths = []
	num   = pyramid[level][loc]

	if level == len(pyramid) -1:
		return num
	else:
		if loc == 0:
			paths.append(try_all_paths(level+1,0))
			paths.append(try_all_paths(level+1,1))

		elif loc == len(pyramid[level])-1:	
			paths.append(try_all_paths(level+1,len(pyramid[level+1])-1))
			paths.append(try_all_paths(level+1,len(pyramid[level+1])-2))
	
		else:
			paths.append(try_all_paths(level+1,loc))
			paths.append(try_all_paths(level+1,loc+1))
		
		return  num + max(paths)

pyramid = build_pyramid()

print try_all_paths(0,0)
