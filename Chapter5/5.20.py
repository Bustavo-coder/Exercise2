def display_table(two_d_list):
    for items in two_d_list:
        for item in items:
            print(item, end = "\t" * 2)
        print()

display_table([[1,2,3],[4,5,6],[7,8,9]])