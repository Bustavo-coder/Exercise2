count = 1
userinput = int(input("Enter You Numebr\n"))
sum = userinput
product = userinput
largest = userinput
smallest = userinput
while(count < 4) :
	sum += userinput
	product = product * userinput
	if userinput > largest :
		largest = userinput
	if userinput < smallest :
		smallest = userinput
	userinput = int(input("Enter You Numebr\n"))
	count += 1
avarge = sum /count 
print(sum ,product,largest,smallest,avarge)