"""
Implementation of binary search
Two versions of simple binary search
"""
# Basic binary search
def binary_search(arr, ele):
    first = 0
    last = len(arr)-1

    found = False

    while first <= last and not found:
        mid = int((first + last)/2)

        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

# Binary search with recursion
def rec_binary_search(arr, ele):
    # Base case
    if len(arr) == 0:
        return False
        # Recursive case
    else:
        mid = len(arr)//2
        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return rec_binary_search(arr[:mid], ele)
            else:
                return rec_binary_search(arr[mid+1:], ele)




if __name__=="__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(binary_search(arr,12))
    print(binary_search(arr,1))
