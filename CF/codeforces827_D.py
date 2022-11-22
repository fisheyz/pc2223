
import math
t = int(input())
solution = [0]


def printPairs(arr, n):
    tmp = 0

    for i in range(0, n):
        for j in range(i, n):
            print(i, j)
            if (math.gcd(arr[i], arr[j]) == 1):
                tmp = (i+j) if tmp < (i+j) else tmp
    if tmp == 0:
        return -1
    else:
        return tmp+2


for i in range(t):

    size = int(input())
    a = [int(k) for k in input().split()]
    test = printPairs(a, size)
    if test == 0:
        print(-1)
    else:
        print(test)
