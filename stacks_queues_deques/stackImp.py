# Implementation of stack
# Using the list as a base DS to create the stack.

class Stack(object):
    def __init__(self):
        self.items = []

    # Is empty will return False if there are items as return statement will no longer be true
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    # popping using list in-built pop function
    def pop(self):
        return self.items.pop()

    # Just view the top item ; don't pop/ remove it.
    def peek(self):
        return self.items[len(self.items)-1]

    # Size --> return size of stack
    def size(self):
        return len(self.items)



if __name__=="__main__":
    s = Stack()
    print(s.isEmpty())
    s.push("two")
    print(s.peek())
    s.push(True)
    print(s.peek())
    print(s.size())
    print(s.isEmpty())
    print(s.pop())
    print(s.pop())
    print(s.isEmpty())
