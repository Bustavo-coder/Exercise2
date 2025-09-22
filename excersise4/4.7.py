from datetime import datetime
from random import randint


def print_date_time():
    print(datetime.today())
print_date_time()

#  4.8
def print_rate(number,toround):
    print(round(number,toround))

for i in range(4):
        print_rate( 13.56449,i)

# 4.9

def convertTof(celcius):
    fahrenhit = ((9 / 5) * celcius) + 32
    return round(fahrenhit, 2)
print("Celcius", end = '\t' * 3)
print("Fahrhit")
for i in range(101):
    print(i, end = '\t' * 4)
    print(convertTof(i))

# 5.0
def game():
    secret_numb = randint(1,1000)
    print(secret_numb)
    while(True):
        guess = int(input("Guess A Random Number From 1 - 1000\n"))
        if secret_numb > guess:
            print("To Low Try Again")
        elif secret_numb < guess:
            print("Too High Try Again")
        else :
            print("Correct")
            break
    key = int(input("Press 1 to continue and 0 to stop"))
    if key == 1:game()
#game()

#4.14
pass_response = ['Very good!', 'Nice work!' ,'Keep up the good work!']
failed_response = ['No. Please try again.', 'Wrong. Try once more.','No. Keep trying.' ]
def choose_question():
    menu = """Choose For The Follwing Qustions
    1.>>>   Addition question
    2.>>>   Subtraction question
    3.>>>   Multiplication question
    4.>>>   Division question
    5.>>>   Random question
    """
    return menu
def question(firstnumber,secondnumber):
    chosse_question = int(input("Which question would you like to choose?\n"))
    qustion_symbols  = ["+","-","*","/"]
    print(f" What Is {firstnumber} {qustion_symbols[chosse_question-1]} {secondnumber}\n")
    return chosse_question

def choose_level_question():
    response = int(input("Pick a level from 1 - 3\n"))
    chosse_question = int(input("Which question would you like to choose?\n"))
    qustion_symbols = ["+", "-", "*", "/"]
    i, j = 0, 0
    if response == 1:
        i, j = 1, 10
    elif response == 2:
        i, j = 5, 10
    elif response == 3:
        i, j = 10, 15
    first_number = randint(i, j)
    second_number = randint(i, j)
    return first_number, second_number

def generate_question():
    first_number , second_number = choose_level_question()
    print(choose_question())
    while(True):
        question(first_number, second_number)
        random_number = randint(0,3)
        result = first_number * second_number
        user_anser = int(input())
        if user_anser == result:
            print(pass_response[random_number])
            generate_question()
        else : print(failed_response[random_number])

generate_question()

