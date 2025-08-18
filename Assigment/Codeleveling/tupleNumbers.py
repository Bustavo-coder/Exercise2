length_numbers = (1,2,3,4,5)
length_numbers+= (6,7)
print(length_numbers)


numbers = (1,2,[3,4],5)
numbers[2][1] = 99
print(numbers)


names = ('apple','Bannana','cherry')
names = list(names)
print(names)

names.append('Mango')
names = tuple(names)
print(names)

number_variable = (10,20,30,40)
a,b, *name= number_variable
print(a,b,name)


number_value = [[2,3,4],[1,5,7],[4,6,8]]
num = list(map(sum,number_value))
print(num)




