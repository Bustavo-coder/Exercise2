userinput = int(input("Enter your price in dollars"))
change = 100 - userinput 
quaters = change // 25
dimes = change % 25 // 10
pennies =  change % 25 % 10

print(f"Your Change is :\n {quaters} qaters \n {dimes} dimes \n {pennies} pennies") 