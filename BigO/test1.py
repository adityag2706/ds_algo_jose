
# Slower -- literally adds the numbers O(n) -- one for loop
def sum1(n):
    final_sum = 0
    for x in range(n+1):
        final_sum += x

    return final_sum

# faster --> uses a formula / algorithm to calculate result. Formula sum = (n*(n+1)) / 2
def sum2(n):
    return (n*(n+1)/2)

if __name__=="__main__":
    print(sum1(10))
    print(sum2(10))
