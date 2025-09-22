def duplicate(iterable):
    iterable = set(sorted(iterable))
    return list(iterable)

print(duplicate([1,2,3,4,5,6,7,8,1,2,34,5,3,4]))
print(duplicate(["adeyemi","qudus","qudus",]))
