import math
def divide_or_square(number):
	if type(number) == str or number < 0: 
		raise ValueError
	elif number % 5 == 0 : return round(math.sqrt(number),2)
	else : return number % 5

def cal_future_investment(investment_amount, monthly_rate,amount_of_years):
	if type(investment_amount) == str or type(monthly_rate) == str or type(amount_of_years) == str :
		raise ValueError
	numberOfMonths = 12 * amount_of_years
	future_investment_value = (investment_amount *(1+monthly_rate))**numberOfMonths
	return future_investment_value

def only_floats(firstNumber,secondNumber):
	if type(firstNumber) == str or type(secondNumber) == str or firstNumber< 0 or secondNumber < 0:
		raise ValueError

	if type(firstNumber) == float and type(secondNumber) == float :
		return 2
	elif type(firstNumber) == float or type(secondNumber) == float :
		return 1
	else : return 0