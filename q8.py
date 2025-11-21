def sumArray(arr):
    s = 0
    for x in arr:
        s += x
    return s

n = int(input())
arr = list(map(int, input().split()))
print(sumArray(arr))