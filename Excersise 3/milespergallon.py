galons_used = int(input("Enter the gallon user (-1 to exit application) : "))
total_miles = 0
total_gallons = 0
while(galons_used != -1) :
	miles_driven = int(input("Enter the miles driven : "))
	miles_per_galoon = galons_used / miles_driven
	print(f"The Miles/Gallon for this tank was : {miles_per_galoon}")
	galons_used = int(input("Enter the gallon user (-1 to exit application) : "))
	total_miles += galons_used
	total_gallons += miles_driven

overall_average = total_miles / total_gallons
print(f"The Average overall miles/gallon was {overall_average}")


	