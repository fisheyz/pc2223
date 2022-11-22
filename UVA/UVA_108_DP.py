import io
import sys
import os
import math

'''uncomment here, check input()'''
# input = io.BytesIO(os.read(0,
#                            os.fstat(0).st_size)).readline
# sys.stdout.write(str(sol) + "\n")

# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/


def maxSubArraySum(a, size):

    max_so_far = -math.inf
    max_ending_here = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return(max_so_far)


n = int(input())
arr = []
rectangle = [[0]*n for _ in range(n)]

while True:
    try:
        arr += [int(x) for x in input().split()]
    except EOFError:
        break

i = j = 0
for x in arr:
    rectangle[i][j] = x
    j += 1
    if j == n:
        j = 0
        i += 1


def maxSubRectangle():
    maxSum = 0
    col = [0]*n
    maxSum = 0
    for j in range(n):
        for i in range(j, n):
            for k in range(n):
                col[k] = col[k]+rectangle[k][i]
            kadaneData = maxSubArraySum(col, n)
            if kadaneData > maxSum:
                maxSum = kadaneData
        col = [0]*n
    print(maxSum)


maxSubRectangle()
