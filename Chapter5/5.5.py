letter =  'abcdefghijklmnopqrstuvwxyz'
def get_string(stop = 27,start = 0,count = 1):
    new_string = letter[start:stop:count]
    return new_string
len_letter = len(letter)
print(get_string(13,0))
print(get_string(13))
print(get_string(27,13))
print(get_string(start = 13))
print(get_string(count = 2))
print(get_string(start = 27 , stop = 0, count = -1))
print(get_string(count = -3,start = 27, stop = 0))




