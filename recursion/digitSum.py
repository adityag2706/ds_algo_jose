"""
Given an integer , create a function which returns the sum of all individual digits
in that integer. for example: if n = 4321, return 4 + 3 + 2 + 1
Tip: you can use modulus % 10
Use Modulus and Division to get the answer
4321 % 10 = 1
4321 / 10 = 432
"""

# My algorithm --
# Divide the n by 10 if it returns 0 (single digit) return that no
# Every iteration n/ 10 needs to be passed
# So n/10 is an argument to the recursive function
# This needs to ve added to the modulus to get the sum of the digits.
def digitSum(n):

    # Base case
    if n // 10 == 0:
        return n

    else:
        mod = n % 10
        rem = n // 10
        return mod + digitSum(rem)

# Instructor solution
# Using length
def sum_func(n):
    # Base case
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sum_func(n//10)

if __name__=="__main__":
    print(digitSum(4321))
    print(digitSum(6421))
    print(sum_func(4321))
    print(sum_func(6421))
