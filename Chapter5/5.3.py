def meter (height):
    return height * 0.0254
list_numb = [69,77,54]
new_list = list((x,meter(x)) for x in list_numb)
print(new_list)

