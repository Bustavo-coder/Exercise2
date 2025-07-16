print("Display the sum, average, product, smallest and largest of the numbers") 
firstnumber = int(input("Enter First Number"))
secondnumber = int(input("Enter Second Number"))
thirdnumber = int(input("Enter Third Number"))
sum = firstnumber + secondnumber + thirdnumber
print("The Sum of the number is", sum)
average = (thirdnumber + secondnumber  + firstnumber)/3
print("The Average of the number is", average)
product = (thirdnumber * secondnumber  * firstnumber)
print("The Average of the number is", product)
max = firstnumber
min = firstnumber
if secondnumber > max : max = secondnumber 
if thirdnumber > max : max = thirdnumber

if secondnumber < min : min = secondnumber 
if thirdnumber < min :min = thirdnumber 
print("The Highest Numer is", max ,"and the lowest Number is", min)



