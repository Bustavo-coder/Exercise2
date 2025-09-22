summarize_string = "Adyemi Is A Boy He Lives In Adedayo EF Gh IJ KL,NMOPQRSTUVWZ ADDDDE,"
def function(char):
    return char.isalpha()
def summarize(string):
    new_string = list(filter(function,list(string.lower())))
    new_set = set(new_string)
    new_list = list()
    for index in new_set:
        new_list.append((index,new_string.count(index)))
    if len(new_set) == 26 : print("It contains 26 Letters")
    else : print("It does not contain 26 Letters")
    return new_list
print(summarize(summarize_string))