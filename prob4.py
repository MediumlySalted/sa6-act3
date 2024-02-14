
a = [1, 2, 3, 4]
b = [7, 2, 6, 5, 4, 1]

# Filters list a based off if it's in b
c = list(filter(lambda x: x in b, a))
print(c)