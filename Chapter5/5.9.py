for count in range(3,1000):
    check = True
    for i in range(2,count):
        if count % i == 0:
            check = False
    if check:
        print(count)

