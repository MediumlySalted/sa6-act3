from functools import reduce

numbers = [20, 5, 7, 1]

# Finds the maximum number in the list
test = reduce(lambda x, y: x if x > y else y, numbers)

print(test)