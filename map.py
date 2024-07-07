
'map()'

'Applies a function to every item of an iterable and returns a new iterable.'

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Prints [1, 4, 9, 16, 25]
