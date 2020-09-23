"""
Function to reverse a linked List in place
The function will take in the head of the ist as input
and return the new head of the list

"""

class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


# Not sure about this one -- using instructor solution

    def reverse_adi(head):
        nextEl = head.nextnode
        head.nextnode = None




# Instructor solution
# Want to make the function operate in O(1)
# Algorithm is O(N)
# Get current node's next node before changing it to previous node
def reverse(head):
    current = head
    previous = None
    nextnode = None

    while current:
        # Grab the current nextnode
        nextnode = current.nextnode

        # Point the current next node to previous for reversal
        current.nextnode = previous
        previous = current

        # To cycle to the next node
        current = nextnode

    return previous

if __name__=="__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    # A is the head here need to reverse it to D
    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    print (a.nextnode.value)
    print (b.nextnode.value)
    print (c.nextnode.value)
    reverse(a)
    print (d.nextnode.value)
    print (c.nextnode.value)
    print (b.nextnode.value)
