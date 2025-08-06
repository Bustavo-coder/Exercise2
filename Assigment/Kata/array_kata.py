def maximum_int_in_list(number_list):
	if type(number_list) != list:
		raise TypeError
	largest = max(number_list)
	return largest

def minimum_int_in_list(number_list):
	if type(number_list) != list:
		raise TypeError
	return min(number_list)

def sum_of_list(number_list):
	if type(number_list) != list :
		raise TypeError
	return sum(number_list)

def sum_of_even(number_list):
	if type(number_list) != list :
		raise TypeError
	even_sum = 0
	for number in number_list:
		if number % 2 == 0:
			even_sum += number
	return even_sum

def sum_of_odd(number_list):
	if type(number_list) != list :
		raise TypeError
	odd_sum = 0
	for number in number_list:
		if number % 2 == 1:
			odd_sum += number
	return odd_sum

def maximum_minimum_int_in_list(number_list):
	if type(number_list) != list :
		raise TypeError
	contain_max_min = [min(number_list),max(number_list)]
	return contain_max_min


def numbers_of_odd(number_list):
	if type(number_list) != list :
		raise TypeError
	odd_numbers = 0
	for number in number_list:
		if number % 2 == 1:
			odd_numbers += 1
	return odd_numbers

def numbers_of_even(number_list):
	if type(number_list) != list :
		raise TypeError
	even_numbers = 0
	for number in number_list:
		if number % 2 == 0:
			even_numbers += 1
	return even_numbers


def even_numbers_in(number_list):
	if type(number_list) != list :
		raise TypeError
	even_list = []
	for number in number_list:
		if number % 2 == 0 :
			even_list.append(number)
	return even_list


def odd_numbers_in(number_list):
	if type(number_list) != list :
		raise TypeError
	odd_list = []
	for number in number_list:
		if number % 2 == 1 :
			odd_list.append(number)
	return odd_list
		
		
	

	