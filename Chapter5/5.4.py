new_list = [[0,0,0], [0,0,0]]
increas = 1
for count,item in enumerate(new_list):
    for index,num in enumerate(item):
        num = increas
        print(num, end = "\t" * 3)
        increas += 1
    print()

