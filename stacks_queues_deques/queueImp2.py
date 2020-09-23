"""
Implement a queue with the foll features:
Check if a queue is empty
Enqueue
Dequeue
Return the size of the Queue
Stack --> LIFO
Queue --> FIFO

"""
class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__=="__main__":
    q = Queue()
    print(q.isEmpty())
    print(q.size())
    q.enqueue(1)
    q.enqueue("two")
    q.enqueue("SD")
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
