student_score = [["Basit","Qudus","Faruq"],[79,80,85],[21,19,10]]

for score in student_score:
	for obj in score:
		print(obj ,end = " ")
	print()

student = ["Basit","Qudus","Faruq"]
print(all(type(items) == str for items in student))
