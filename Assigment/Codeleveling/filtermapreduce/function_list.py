def get_even(num):
	return num % 2 == 0
def filter_element(collection):
	if type(collection) != list or any(type(element) != int for element in collection) :
		raise TypeError('Can Only Accept an Iterable With Number Elment')
	filterd_list = list(filter(get_even,collection))
	return filterd_list
def is_length(word):
	if type(word) != str :
		raise ValueError("Value Must Be String")
	return len(word) >= 5
def filters_words(collections):
	if type(collections) != list or any(type(element) == int for element in collections):
		raise TypeError
	filter_word_list = list(filter(is_length,collections))
	return filter_word_list 
def is_greater(num):
	if type(num) != int or num < 1 :
		raise ValueError("Whole Positve Numbers Expected only")
	return num > 2
def is_divisible_by_three_n_five(num):
	if type(num) != int :
		raise ValueError("Can only Accept Integers")
	return num % 3 == 0 and num % 5 == 0

def filter_collction_num_divided_by_3_n_s(collections):
	if type(collections) != list or any(type(element) == str for element in collections) :
		raise TypeError
	new_list = list(filter(is_divisible_by_three_n_five,collections))
	return new_list

def is_palidome(word):
	if type(word) != str :
		raise ValueError("Value Must Be String")
	return word == word[-1::-1]

def filter_collection_palidome(collections):
	if type(collections) != list or any(type(element) == int for element in collections):
		raise TypeError
	filtered_list = list(filter(is_palidome,collections))
	return filtered_list

