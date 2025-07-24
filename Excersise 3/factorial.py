user_input = int(input("Enter the number you want to factorial \n"))
count = user_input  
factorial = 1
while count > 1 :
	factorial *= count
	count -=1
print(factorial)