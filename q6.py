import math
def volumeSphere(r):
    return (4 * math.pi * r * r * r) / 3
r = int(input())
print(volumeSphere(r))