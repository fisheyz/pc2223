import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def getsum(BITTree, i):
    s = 0
    while i > 0:

        s += BITTree[i]
        i -= i & (-i)

    return s


def updatebit(BITTree, m, i, v):
    while i <= m:

        BITTree[i] += v
        i += i & (-i)


t = input().decode()
for c in range(int(t)):
    N, M, K = [int(x) for x in input().decode().split()]
    japan = []
    BITTree = [0]*(M+5)
    for i in range(K):
        japan.append(tuple(map(int, input().decode().split())))

    japan = sorted(japan, key=lambda x: x[0], reverse=True)
    totalsum = 0
    for i in range(K):
        updatebit(BITTree, M, japan[i][1], 1)
        totalsum += getsum(BITTree, japan[i][1]-1)
    print("Test case %1d: %1d" % (c, totalsum))
