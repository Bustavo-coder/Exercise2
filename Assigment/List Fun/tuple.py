number_tuple = tuple(index for index in range(1,21))	
print(number_tuple)

def is_even(num):
	return num % 2 == 0

sum_even_tuple = tuple(filter(is_even,number_tuple))
print(sum (sum_even_tuple))

def is_odd(num):
	return num % 2 == 1
sum_odd_tuple = tuple(filter(is_odd,number_tuple))
print(sum (sum_odd_tuple))

range = max(number_tuple) - min(number_tuple)
print(range)

number_one,number_two,number_three,number_four,number_five,*number = number_tuple
print(number_one,number_two,number_three,number_four,number_five)