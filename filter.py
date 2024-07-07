
'filter()'

'Applies a function to every item of an iterable and returns a new iterable with items that return True.'

numbers = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))  # Prints [2, 4]
