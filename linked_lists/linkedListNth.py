"""
Write a function that takes a head node and an integer value n
and then returns the nth to last node in the linked list

If you put 2 as n and the length of the list is 6
it will return the 6 - 2 = 4th element
"""

class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

# -- Not clear on thos one ---

# My algorithm-- It worked!! :D
# So creating two pointers and two head reference
# Big O complexity 2*O(n) not ideal but will do fine for interviews
# traverse the entire linked list to get the length
# Subtract n from the lenth this  will give the length -n element that you need
# Use a marker variable to track what element you are in
# When marker == length -n you have found the element , return it
def nthLastNode_adi(n, head):
    count = 1
    marker = 0
    current = head

    # this will give length of the list.
    while head.nextnode != None:
        count = count + 1
        head = head.nextnode

    # To find the nth from last node
    position = count - n
    #print("position :{}".format(position))

    while current.nextnode != None:
        if marker == position:
            return current
        marker = marker + 1
        current = current.nextnode

# Instructor solution -- using a marker similar to the Cycle option
# One marker with single step and another with n steps.
def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n-1):
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list')

        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:

        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer


if __name__=="__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    d.nextnode = e

    print(nthLastNode_adi(2,a).value)
    print(nth_to_last_node(2,a).value)
