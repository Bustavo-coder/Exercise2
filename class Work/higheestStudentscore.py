SCORE_A = int(input("Enter the first score"))
SCORE_B = int(input("Enter the second score"))
SCORE_C = int(input("Enter the third score"))
highest_score = SCORE_A
if SCORE_B > highest_score :
	highest_score = SCORE_B
if SCORE_C  > highest_score :
	highest_score = SCORE_C
print("The Highest score is ",highest_score)

	
N_DAYS = int(input("Enter The day we are in\n"))

match N_DAYS:
	case 1 : print("Monday")
	case 2 : print("Tuesday")
	case 3 : print("Wednesday")
	case 4 : print("Thursday")
	case 5 : print("Friday")
	case 6 : print("Saturday")
	case 7 : print("Sunday")
	case _ : print("Invalid day")


FIRST_X = int(input("Enter Your Number"))
FIRST_Y = int(input("Enter your number"))
FIRST_Z = int(input("Enter your"))

highest = FIRST_X
secondlargest = -99999999999

if FIRST_Y > highest : highest = FIRST_Y
if FIRST_Z > highest : highest = FIRST_Z
print("The Hihest is", highest)

if highest > FIRST_X  and FIRST_X > secondlargest : secondlargest = FIRST_X
if highest > FIRST_Y  and FIRST_Y > secondlargest : secondlargest = FIRST_Y
if highest > FIRST_Z  and FIRST_Z > secondlargest : secondlargest = FIRST_Z
print("The Second Hihest is", secondlargest)
