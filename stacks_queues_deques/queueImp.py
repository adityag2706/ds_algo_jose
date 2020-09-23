# Implementation of Queue

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # Using insert method from the list module
    # insert takes two args --> index and element
    # Using at 0 so we can pop the elements from the front FIFO style :D
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__=="__main__":
    q = Queue()
    print(q.size())
    print(q.isEmpty())
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
