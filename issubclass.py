
'issubclass()'

'Returns True if the specified class is a subclass of the specified parent class.'

class Parent:
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent))  # Output: True
