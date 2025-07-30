import math
def divide_or_square(number):
	if type(number) == str or number < 0: 
		raise ValueError
	elif number % 5 == 0 : return round(math.sqrt(number),2)
	else : return number % 5

	
