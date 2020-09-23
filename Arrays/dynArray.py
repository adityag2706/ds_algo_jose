# Implementation of Dynamic Array in Python
# ctypes --> raw array holder
# _ before methonds name to keep it non public
import ctypes

class DynamicArray(object):

    def __init__(self):

        self.n = 0 # count or start
        self.capacity = 1 # no of elements array can hold
        self.A = self.make_array(self.capacity) # Array holder

    def __len__(self):
        return self.n

    def __getitem__(self,k):

        if not 0 <= k < self.n:
            # checks if index k is within the range of 0 to n
            return IndexError('K is out of bounds')

        return self.A[k]

    # add elements to the array
    def append(self,ele):
        # If count = capacity as in array has reached it's limit then double the capacity
        if self.n == self.capacity:
            self._resize(2*self.capacity) # 2x if capacity isn't enough

        # add element at the end (count) position
        self.A[self.n] = ele
        self.n += 1

    # Double the size of the array
    def _resize(self, new_cap):
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap


    # Method to make the array itself - raw array
    def make_array(self, new_cap):

        return (new_cap * ctypes.py_object)()


if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(1)
    print(len(arr))
    arr.append(2)
    print(len(arr))
    print(arr[0], arr[1])
