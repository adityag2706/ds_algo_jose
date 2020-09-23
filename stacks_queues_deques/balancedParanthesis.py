"""
Balanced Parentheses Check
Given a string of opening and closing Parentheses, check whether it is balanced.
3 types of Parentheses:
round brackets --> ()
square brackets --> []
curly brackets --> {}
Assume string does not contain any characters other than these
Assume no spaces, words or numbers
Balanced --> ([])
Unbalanced --> '([)]'
Complement of ( is )
Complement of [ is ]
Complement of { is }
Every bracket opened needs to be closed in a reversed order  for a Parentheses to be balance--> Stacks!!!!
Eg:
([{}]) --> Balanced
( is opened first but closed ")" last
{ is opened last buy closed "}" first

"""

# Big O complexity --> O(N) only looping through string once.
# This works!! This is epic!! :D . O(N) --> Good Job!! :D
"""
My algo explained -->
Create a dictionary with opening paranthesis as key and closing as value
Since the string needs to be balanced...this is similar to a deque structer
The element at the front (value) must be matched to the element at the rear (key)
So element in the front == value for the key in the rear in the dictionary
"""
def balancedParaCheck(arr):
    paraDict = {"(":")", "{":"}", "[":"]"}
    arr = list(arr)
    while len(arr) != 0:
        rear = arr.pop(0)
        front = arr.pop()
        if paraDict[rear] != front:
            return False
    return True

# Instructor solution
# Push all opening paranthesis to a stack
# For closing paranthesis check if the first closed paranthesis matched
# This is not working on Python3 for some reason..need to debug.
def balance_check(s):
    # If no of paranthesis are not even it is already Unbalanced
    if len(s)%2 != 0:
        print("length: {}".format(len(s)))
        return False

    opening = set('([{')
    matches = set([('(',')'),('[',']'),('{','}')]) # Passing tuples of matching parameters.
    stack = []

    for paren in list(s):
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                print("Here")
                return False
            last_open = stack.pop()

            if (last_open, paren) != matches:
                return False
    print("Stack {}".format(stack))
    return len(stack) == 0


if __name__=="__main__":
    print(balancedParaCheck("([])"))
    print(balancedParaCheck("([{}])"))
    print(balancedParaCheck("([)]"))
    print(balancedParaCheck("(({{[{()}]}}))"))
    print("-"*50)
    print(balance_check("([])"))
    print(balance_check("([{}])"))
    print(balance_check("([)]"))
    print(balance_check("(({{[{()}]}}))"))
