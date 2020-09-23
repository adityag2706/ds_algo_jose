# Add all elements inside an array

def add_ele(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

if __name__=="__main__":
    print(add_ele([1,2,3,4]))
