"""
Implement a Deque that has the foll features:
Check if its empty
Add to both front and rear
Remove from Front and Rear
Check the size
"""

class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

if __name__=="__main__":
    d = Deque()
    print(d.size())
    print(d.isEmpty())
    d.addFront("one")
    d.addRear(3)
    d.addFront("A")
    print(d.size())
    print(d.removeRear())
    print(d.removeFront())
