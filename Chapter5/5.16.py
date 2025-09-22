list_Lettter = list()
for let in range(20):
    list_Lettter.append(input("Enter any random character: "))
ascend = sorted(list_Lettter)
descend = sorted(list_Lettter, reverse = True)
new_list = list(sorted(set(list_Lettter)))
print(ascend)
print(descend)
print(new_list)
