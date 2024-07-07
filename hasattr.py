
'hasattr()'

'Returns True if the object has the specified attribute.'

class MyClass:
    def __init__(self):
        self.x = 10

obj = MyClass()
print(hasattr(obj, 'x'))  # Output: True
