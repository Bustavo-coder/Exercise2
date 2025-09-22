from random import randint
storeNumber = {
    '2' : ['A','B','C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y'],
}
def generate_phrase(numbers):
    phrase = ""
    for number in numbers:
        rand_int = randint(0, 2)
        phrase += storeNumber[number][rand_int]
    return phrase



def print_meaning(number):
    condition=  all(char > '1'for char in number)
    condition = condition and len(number) < 8
    new_list = list()
    if condition:
        for _ in range(2187):
             new_list.append(generate_phrase(number))
        return new_list
    else: return "Number Does Not Have A Valid Charcter"

print(print_meaning("2844363"))


