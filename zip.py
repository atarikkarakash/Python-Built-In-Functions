
'zip()'

'Combines multiple iterables and returns an iterator of tuples, where each tuple contains elements from the iterables at the same position.'

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
combined = zip(names, scores)
print(list(combined))  # Prints [('Alice', 85), ('Bob', 90), ('Charlie', 95)]
