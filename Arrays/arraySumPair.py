"""
Array Sum Pair problem
Given an integer array, output all the unique pairs that sum up to a specific value of k
Input
pair_sum([1,3,2,2], 4)

will return 2 pairs
(1,3)
(2,2)
Output should return no of pairs
"""

# Brute force pick one element add it to each element in the list and see if it matches the sum
# this will be O(n^2) least effiecient

# 2nd solution subtract element from the sum then check if the subtration is present in the list
# --> this would have worked had we required to only find one pair
"""
count = 0
cmplt = []
for ele in arr1:
    res = sum - ele
    cmplt.append(res)

for c in cmplt:
    if c in ele:
        count++
return count

"""
## My solution - doesn't work.... :( )
# Not sure what would be the limits for while
"""
def pair_sum(arr,sum):
    count = 0
    lower = 0
    upper = len(arr)
    whileL = len(arr) - 2
    arr = arr.sort()
    while lower != whileL:
        res = arr[upper] + arr[lower]
        if res < sum:
            lower = lower + 1
        elif res > sum:
            upper = upper - 1
        else:
            count = count + 1
    return count
"""
# Trying brute force- Not exactly brute force , Decent Algo, O(n) complexity - not bad
# This could fail in some conditions ..need to test more
def pairSumBrute(arr,sum):
    count = 0
    for i in arr:
        cmplt = sum - i
        if cmplt in arr:
            count = count + 1
            arr.remove(cmplt)
            arr.remove(i)
    return count

# Instructor Solution - O(n)
# Instructor also using target - complement
def pair_sum(arr,k):

    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num,target)), max(num,target)))


    #return len(output)
    print ('\n'.join(map(str,list(output))))






if __name__=="__main__":
    #print("Weird while algo")
    #print(pair_sum([1,3,2,2], 4))
    #print("-"*50)
    print("Subtract algo")
    print(pairSumBrute([1,3,2,2], 4))
    print(pair_sum([1,3,2,2], 4))
