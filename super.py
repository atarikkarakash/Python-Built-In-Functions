
'super()'

'Returns a proxy object that delegates method calls to a parent or sibling class of type.'

class Parent:
    def say_hello(self):
        print("Hello from Parent")

class Child(Parent):
    def say_hello(self):
        super().say_hello()
        print("Hello from Child")

child = Child()
child.say_hello()
# Output:
# Hello from Parent
# Hello from Child
