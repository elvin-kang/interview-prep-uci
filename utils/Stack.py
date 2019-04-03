class Stack:
    def __init__(self, stack=list()):
        self._stack = stack

    def isEmpty(self):
        return len(self._stack) == 0
    
    def peek(self):
        try:
            return self._stack[-1]
        except:
            raise IndexError("peek from empty stack")

    def pop(self):
        try:
            return self._stack.pop()
        except:
            raise IndexError("pop from empty stack")

    def push(self, item):
        self._stack.append(item)
        return item

    def __len__(self):
        return len(self._stack)

    def toList(self):
        return self._stack
        

    
