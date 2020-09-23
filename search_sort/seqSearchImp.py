"""
Implementation of Sequential Search in an ordered and unordered list
"""

def seq_search(arr, ele):

    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == ele:
            found = True
        else:
            pos = pos + 1

    return found


def ordered_seq_search(arr, ele):
    """
    Input array must be ordered/sorted
    """
    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True

            else:
                pos = pos + 1
    return found




if __name__== "__main__":
    arr = [1,2,3,4,5]
    print(seq_search(arr,1))
    print(ordered_seq_search(arr,6))
