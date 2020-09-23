# Implementation of a singly linked list


class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None


if __name__=="__main__":
    # Initialize 3 nodes
    a = Node(1)
    b = Node(2)
    c = Node(3)

    # To link these nodes in a linked list
    # Point nextnode for a to b and nextnode for b to c
    # c nextnode will be none :). That simple!!
    a.nextnode = b
    b.nextnode = c

    print(a.value)
    print(a.nextnode.value)
    print(c.value)
    print(b.nextnode.value)
