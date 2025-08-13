def getFactorial(number):
	product = 1
	for num in range(1,(number + 1)):
		product = num * product
	return product

		
def mathematicalConstant(number):
	constant = 1
	for num in range(1, (number + 1)):
		constant += 1 / (getFactorial(num))
	return constant

print(mathematicalConstant(10))
