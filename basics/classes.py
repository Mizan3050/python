
class Stack:

    def __init__(self):
        self.name = 'Meezan'

    def __str__(self) -> str:
        return self.name

    def printSelf(self):
        print(self.name)

_self = Stack()
print(_self)