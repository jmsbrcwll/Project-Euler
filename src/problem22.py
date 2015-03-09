def get_char_score(char):
	return ord(char) - 64

file  = open('p022_names.txt','r')
txt   = file.read()
names = sorted([name.replace('"','') for name in txt.split(',')])
score = 0

for i in range(0,len(names)):
	score +=  (i+1) * sum([get_char_score(char) for char in names[i]])

print 'score:%s' % score
