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
		
		