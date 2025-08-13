count = 0
store = []
while(count < 10):
	user_input = int(input("Enter Your Number\n"))
	store.append(user_input)
	count += 1

largest = max(store)
print(largest)
secondlargest = 0

for index in store:
	if index == largest : continue
	if index > secondlargest :
		secondlargest = index
print(secondlargest)
	

	
