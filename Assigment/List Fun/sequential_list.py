number_list = []
for index , value in enumerate(range(1,16)):
	number_list.append(value)
	number_list.append(value)
print(number_list)
for index , value in enumerate(number_list):
	if number_list.count(value) > 1:
		number_list.remove(value)

print(number_list)

def add_first_third_element(collection):
	middlepositon = 0
	if len(collection)/2 == 0 :
		collemiddlepositon = (len(collection)/2 - 1) - len(collection)/2
	else : middlepositon = len(collection)//2 
	sum = collection[0] + collection[middlepositon] + collection[len(collection) - 1]
	print(collection[middlepositon])
	return sum

print(add_first_third_element([1,2,3,4,5,6,7]))
