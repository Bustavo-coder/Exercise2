storeNumber = {
    ('A', 'B', 'C'): '2',
    ('D', 'E', 'F'): '3',
    ('G', 'H', 'I') : '4',
    ('J', 'K', 'L'): '5',
    ('M', 'N', 'O'): '6',
    ('P', 'R', 'S'): '7',
    ('T', 'U', 'V'): '8',
    ('W', 'X', 'Y'): '9',

}
def generate_number(phrase):
    phrase = phrase.upper()
    count = 0
    for key in storeNumber.keys():
        if key.__contains__(phrase[0]):
            new_phone += storeNumber[key]
        if count < len(storeNumber)-1:
            count+=1
            print(count, storeNumber[key])
    return new_phone
print(generate_number("BIGDATA"))


