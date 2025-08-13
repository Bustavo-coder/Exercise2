userinput = input("Enter The Number\between one and zero to convert to base 10\n")
get_length = len(userinput) * 2
base = 0
for alphas in userinput:
	multi = (int)(alphas) * get_length
	base += multi
	if get_length > 2 :
		get_length //= 2
	else : get_length -= 1
print(base)

	
	