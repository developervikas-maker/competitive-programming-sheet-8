import math

def areaEllipse(a, b):
    return math.pi * a * b

a, b = map(int, input().split())
print(areaEllipse(a, b))