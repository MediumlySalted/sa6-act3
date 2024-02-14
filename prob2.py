
list_of_strings = ['yellow', 'turtle', 'mongoose', 'closet', 'Elphaba']

# Sorts string by length then alphabet on same length strings.
sorted_strings = sorted(list_of_strings, key=lambda x: (len(x), (x)))
print(sorted_strings)