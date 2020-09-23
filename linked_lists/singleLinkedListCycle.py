"""
Singly Linked List Cycle Check
Given a singly linked list , write a function which takes in the first node in a
singly linked list and returns a boolean indicating if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a previous node in the list.
This is sometimes known as a circularly linked list.

"""

class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


# My algorthimn - O(1)
# Create a list containing all the nodes
# pick the last node and check if lastnode.nextnode == firstnode
def cycle_check_adi(linked):
    lastEl = linked[len(linked) - 1]
    if lastEl.nextnode == linked[0]:
        return True

    return False


# Instructor solution
# Two markers marker1 and marker2 traversing the list
# Both markers will traverse the linked list
# But marker2 will move two nodes ahead for every one node that marker1 moves.
# Eventually marker2 will be "lapping" with marker1 and they will equal each other
# in a cycle list.
# Marker2 will not lap if linked list is non-cycle
# this is better since my solution uses ordered list which is not how linked list works
# Big O comolexity -- O(N)
def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode
        if marker2 == marker1:
            return True

    return False


if __name__=="__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.nextnode = b
    b.nextnode = c
    c.nextnode = a # cycle
    linkedListA = [a, b, c]
    print(cycle_check_adi(linkedListA))
    print(cycle_check(a))

    x = Node("A")
    y = Node("B")
    z = Node("C")
    x.nextnode = y
    y.nextnode = z # Non-cycle
    linkedListB = [x, y, z]
    print(cycle_check_adi(linkedListB))
    print(cycle_check(x))
