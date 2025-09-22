def is_palidome(name):
    return name == name[::-1]
print(is_palidome("radar"))