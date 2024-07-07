
'setattr()'

'Sets the value of the named attribute of an object.'

class MyClass:
    pass

obj = MyClass()
setattr(obj, 'x', 10)
print(obj.x)  # Output: 10
