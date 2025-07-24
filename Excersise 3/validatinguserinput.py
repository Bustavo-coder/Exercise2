GENRATE_RANDOM = 20
user_input = int(input("Enter your Guess You Have Ten Trials\n"))
scores = 0

while scores < 10 and GENRATE_RANDOM != user_input :
	if user_input  > GENRATE_RANDOM :
		print("Too High Enter again")
		scores += 1 
	if user_input < GENRATE_RANDOM :
		print("Too Low Enter again")
		scores += 1
	user_input = int(input("Enter your Guess You Have Ten Trials\n"))
	

if scores == 10 :print("You Have Exceded the number of trials")
else : print(f"You Won the Game You Used {scores} trials")

