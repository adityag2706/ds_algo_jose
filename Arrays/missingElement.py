"""
Consider an array of non-negative integers. A second array is formed by shuffling
the elements of the first array and deleting a random element. Given these two arrays,
find which element is missing in the second array itself.
Example:
Frist array is shuffled and the number 5 is removed to construct the second array.
Input:
finder ([1,2,3,4,5,6,7], [3,7,2,1,4,6])
Output:
5 is the missing number
"""
import collections

# Solution 1-> Brute Force -> O(n^2) find the larger array loop through smaller arrayself.
# find different element
# This works!! - Brute force - O(n^2)
def finderBrute(arr1, arr2):
    if len(arr1) == len(arr2):
        return
    elif len(arr1) > len(arr2):
        for i in arr1:
            if i not in arr2:
                return i
    else:
        for i in arr2:
            if i not in arr1:
                return i

# Using Sets - O(1) since using python specific structs ; not ideal for interviews i guess
# The problem here is repeated elements are mremoved so if the array contains repeating elements it is not valid
# Not ideal ; returns as set
def finderSet(arr1, arr2):
     setArr1 = set(arr1)
     setArr2 = set(arr2)
     if len(setArr1) == len(setArr2):
         return
     elif len(setArr1) > len(setArr2):
         diff = setArr1 - setArr2
         return diff
     else:
         diff = setArr2 - setArr1
         return diff

# Dictionary Method - best method yet!!
# Resilient against repeats as we are subtracting counts os repeating elements common to both arrays
# will also be considered.
# Big O complexity O(N) --> Awesome for interviews :). Good Job!!
def finderDict(arr1, arr2):
    count = {} # To count occurences of elements

    if len(arr1) == len(arr2):
        return

    for i in arr1:
        if i in count.keys():
            count[i] = count[i] + 1
        else:
            count[i] = 1

    for i in arr2:
        if i in count.keys():
            count[i] = count[i] - 1
        else:
            count[i] = 1

    for k in count.keys():
        if count[k] > 0:
            return k


# Instructor Solution - O(NlogN) - using Sorting but not sets
# Both of the instructor solutions assume arr1 is greater than arr2
# Element removed from arr2 is assumed -- ask this to the interviewer to confirm
def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]   # Return 1st element if no match.

# Instructor solution using hash tables, similar to mine but using ordered dict/ collections instead

def finderInstDict(arr1,arr2):
    # this Avoids key errors
    # If the key is not in dict instead of throwing an error it will jsut add it to the dict.
    # Removes the step to check if key is present in the dict which is what i did in my algo
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    # If num is not counted i.e not in dict  when iterating through arr2
    # It means that was the removed no; return that no.
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1  # to remove common elements

# Another solution --> Compute sum of all elements in arr1 and then all elements in arr2
# Subtract the two numbers and you get the removed no!! :D (not very scalable also not precise hence not recommended
# - overflow issues if array has large nos, preciseness issue if array has float elements)

# Instructor tricky Method with O(1) complexity.
# Use XOR --> exclusive OR True only when one of the values is True (TF, or FT)
def finderXOR(arr1, arr2):
    result = 0

    # Perform an XOR between numbers in the arrays
    # arr1 + arr2 concatenates (extends) the arrays
    # You then use XOR to weed out the common elements
    for num in arr1+arr2:
        result^=num
        print result

    return result

if __name__=="__main__":
    print(finderBrute([1,2,3,4,5,6,7], [3,7,2,1,4,6]))
    print(finderSet([1,2,3,4,5,6,7], [3,7,2,1,4,6]))
    print(finderDict([1,2,3,4,5,6,7], [3,7,2,1,4,6]))
    print(finder([1,2,3,4,5,6,7], [3,7,2,1,4,6]))
    print(finderInstDict([1,2,3,4,5,6,7], [3,7,2,1,4,6]))
