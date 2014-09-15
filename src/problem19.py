
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#define monday as 1 and sunday as 7
day = 1
num_of_sundays = 0

for year in range(1900,2001):
	if year % 4 == 0:
		month_days[1] = 29
	else:
		month_days[1] = 28

	for month in month_days:
		day += month 		
		if day % 7 == 0 and year > 1900:
			num_of_sundays +=  1	

print(num_of_sundays)		
