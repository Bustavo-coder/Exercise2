number_list = [5,10,15,20,25,90,100]
sum = 0
for number in range(0,len(number_list)):
	sum += number_list[number]
print(sum) 


word_list = ["Adeyemi","Qudus","Yemi","Fatia"]
word_len_list = []

for word in range(0,len(word_list)):
	word_len_list.append(len(word_list[word]))
print(word_len_list)
n4

value_list = [2,3,4,8,9,10,16,8]

for value in range(0,len(value_list)):
	if value % 2 == 1 :
		print(value_list[value])