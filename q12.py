import math

def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)

a, b = map(int, input().split())
print(hypotenuse(a, b))