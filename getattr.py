
'getattr()'

'Returns the value of the named attribute of an object.'

class MyClass:
    def __init__(self):
        self.x = 10

obj = MyClass()
print(getattr(obj, 'x'))  # Output: 10
