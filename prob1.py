from functools import reduce

number = 51423

# Takes a number and totals the digits
result = reduce(lambda x, y: int(x) + int(y), str(number))
print(result)