userinput = input("Enter The number to check if it is a pallidome")
reversedNum = ""
for num in reversed(userinput):
	reversedNum+= num

print(reversedNum)

if(userinput == reversedNum) :print("It is a palindome")
else : print ("It is not a palidome")
	

	