user_input = int(input("Enter Your Number\n"))
largest = user_input
second_largest = -999999999999999999
count = 1
while(count < 10):
	if user_input > largest :
		largest = user_input
	user_input = int(input("Enter Your Number\n"))
	count += 1
print(largest,second_largest)