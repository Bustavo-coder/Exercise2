print("number", end = '	')
print("Square", end = '	')
print("cube",)

for row in range(6):
	print(f"{row}\t{row ** 2}\t{row ** 3}", end = '')
	print()