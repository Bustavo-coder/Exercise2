num = int(input("Enter the numbers to print "))
count = 10
while count < 1000 :
	lastnum = num // count % count
	print(lastnum)
	count *= 10

	
	