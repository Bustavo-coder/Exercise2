pricipal =  int(input("Enter The Amount you wish to borrow:  "))
duration = int(input("Enter the amount duration for your loan:  "))
annual_intrest_rate = int(input("Enter the annual intrest rate:  "))
MONTH_IN_YEARS = 12
PERCENTAGE = 100
number_of_month = duration * MONTH_IN_YEARS
percentage_monthly_rate = (annual_intrest_rate / PERCENTAGE) / (number_of_month)
print( "our Monthly percenatge rate is" , percentage_monthly_rate , " %")
monthly_payment = pricipal *((percentage_monthly_rate *(1 + percentage_monthly_rate) ** number_of_month) / ((1 +percentage_monthly_rate) ** number_of_month-1) )
print("Your Mortage monthly payment is", monthly_payment)
