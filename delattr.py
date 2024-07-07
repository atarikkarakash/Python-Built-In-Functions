
'delattr()'

'Deletes the named attribute from an object.'

class MyClass:
    def __init__(self):
        self.x = 10

obj = MyClass()
delattr(obj, 'x')
print(hasattr(obj, 'x'))  # Output: False
