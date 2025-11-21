import math
def squareRoot(a):
    r = int(math.sqrt(a))
    if r * r == a:
        return r
    return -1

a = int(input())
print(squareRoot(a))