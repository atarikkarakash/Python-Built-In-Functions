
'vars()'

'Returns the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.'

class MyClass:
    def __init__(self):
        self.x = 5
        self.y = 10

obj = MyClass()
print(vars(obj))  # Output: {'x': 5, 'y': 10}
