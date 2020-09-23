"""
Implement a Stack that has the foll features:
Check if it's empty
Push a new item
Pop an item
Peek at the top item
Return the Size
"""

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s.size())
    print(s.isEmpty())
    s.push(1)
    s.push("A")
    s.push(True)
    print(s.size())
    print(s.peek())
    print(s.pop())
    print(s.pop())
