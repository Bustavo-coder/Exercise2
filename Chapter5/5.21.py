new_list = []
def enque(value):
    new_list.append(value)
    print(new_list)
def dqueue():
    new_list.pop(0)
    print(new_list)
enque(3)
enque(2)
enque(1)
for _ in range(3):
    dqueue()

