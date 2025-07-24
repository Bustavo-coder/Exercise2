user_input = int(input("Enter Your Number\n"))
largest = user_input
second_largest = -999999999999999999
count = 1
while(count < 10):
	if user_input > largest :
		largest = user_input
	if user_input > largest and user_input < second_largest :
		second_largest =   user_input

print(largest,second_largest)