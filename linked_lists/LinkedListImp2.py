"""
Implement a singly linked list and a doubly linked list
"""

# Singly Linked List Class Definition
class SinglyNode(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


# Doubly linked list class definition. 
class DoublyNode(object):


    def __init__(self, value):
        self.value = value
        self.previousnode = None
        self.nextnode = None


if __name__=="__main__":

    #Singy Linked List

    a = SinglyNode(1)
    b = SinglyNode(2)
    c = SinglyNode(3)

    a.nextnode = b
    b.nextnode = c

    # Doubly Linked List
    x = DoublyNode("A")
    y = DoublyNode("B")
    z = DoublyNode("C")

    x.nextnode = y
    y.previousnode = x
    y.nextnode = z
    z.previousnode = y
