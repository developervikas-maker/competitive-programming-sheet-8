def squareRange(x, y):
    for i in range(x, y + 1):
        print(i * i, end=" ")

x, y = map(int, input().split())
squareRange(x, y)