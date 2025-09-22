from operator import itemgetter

list_main = list()
def write_invoice(part_numbr,part_description,quantity,item_price):
    new_tup = (part_numbr,part_description,quantity,item_price)
    list_main.append(new_tup)

write_invoice( 24,"Electric sander",6,57.98)
write_invoice( 83,"Power Saw",18,99.9)
b = sorted(list_main,key = itemgetter(0), reverse = True)
c = sorted(list_main,key = itemgetter(2), reverse = True)
d = sorted(list_main,key = itemgetter(3), reverse = True)