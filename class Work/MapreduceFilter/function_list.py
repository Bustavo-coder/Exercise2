def get_squares(number):
	if type(number) == str :
		raise TypeError
	if(number < 0):
		return 0
	return number * number

def map_list(number_list):
	if type(number_list) != list:
		raise ValueError
	return list(map(get_squares,number_list))

def get_length(collection):
	if type(collection) == int:
		raise ValueError
	return len(collection)

def list_of_length(letter_list):
	if type(letter_list) != list:
		raise ValueError
	return list(map(get_length,letter_list))

def get_even(num):
	if type(num) == str :
		raise TypeError
	return num % 2 == 0

def get_even_list(list_num):
	if type(list_num) != list :
		raise ValueError
	if all(type(item) != int for item in list_num):
		raise TypeError
	return list(filter(get_even,list_num))

def get_length_OF_item(letter):
	return len(letter) > 5

def filter_length(list_value):
	if type(list_value) != list :
		raise ValueError
	if all(type(item) == int for item in list_value):
		raise TypeError
	return list(filter(get_length_OF_item,list_value))

	

