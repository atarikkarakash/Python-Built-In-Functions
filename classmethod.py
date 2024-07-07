
'classmethod()'

'Converts a method into a class method.'

class MyClass:
    @classmethod
    def my_classmethod(cls):
        return 'class method called'

print(MyClass.my_classmethod())  # Output: 'class method called'
