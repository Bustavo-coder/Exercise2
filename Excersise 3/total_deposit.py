count = 1
origial_amount = 1000
r_anual = 7
number_years = 30
amount_deposit = 0
total_deposit = 0
while count <= 30 :
	amount_deposit  = origial_amount * (1 + r_anual) * count
	print(f"The amount deposit for year {count} is {amount_deposit}")
	total_deposit += amount_deposit
	count += 1

print(f"The Total money for 30 years is {total_deposit}")

	