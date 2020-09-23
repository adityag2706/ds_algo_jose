"""
Write a recursive function which takes an integer and computes the cumulative sum of 0
to that integer
for example if n=4 , return 4+3+2+1+0 = 10
"""

# My solution --> Instructor solution is also same; this was pretty straightforward
def cumulativeSum(n):
    # Base case
    if n == 0:
        return 0

    else:
        return n + cumulativeSum(n-1)

if __name__=="__main__":
    print(cumulativeSum(4))
    print(cumulativeSum(5))
