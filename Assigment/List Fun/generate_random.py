from random import randint
def get_random(starting,stop):
	return randint(starting,stop)

def get_random_range_and_list_size(start,stop,list_size):
	if type(start) != int or type(stop) != int or type(list_size) != int:
		raise ValueError
	list_randomNumbers = []
	for numb in range(1,(list_size + 1)):
		list_randomNumbers.append(get_random(start,stop))
	return list_randomNumbers

def get_length(collections):
	if type(collections) == int :
		raise ValueError
	list_length = 0
	for numb in collections:list_length += 1
	return list_length
		
def getEven(collections):
	if type(collections) == str:
		raise TypeError
	sum_list = [collections[index] for index, _ in enumerate(collections) if index % 2 == 0 and index > 0]
	total_sum = sum(sum_list)
	return total_sum

def get_odd_sum(collections):
	if type(collections) == str:
		raise TypeError
	sum_list = [collections[index] for index , _ in enumerate(collections) if index % 2 == 1 and index > 0]
	total_sum = sum(sum_list)
	return total_sum

def multiply_odd_third(collections):
	if type(collections) == str:
		raise TypeError
	sum_list = [collections[index] for index , _ in enumerate(collections) if index % 3 == 0 and index > 0]
	total_sum = 1
	for index in sum_list: total_sum *= index
	return total_sum


def get_average(collections):
	if type(collections) == str:
		raise TypeError
	sum_list = [collections[index] for index, _ in enumerate(collections)]
	average_sum = sum(sum_list)/len(sum_list)
	return average_sum

def get_largest(collections):
	if type(collections) == str:
		raise TypeError
	return max(collections)


def get_smallest(collections):
	if type(collections) == str:
		raise TypeError
	return min(collections)

	
	

	