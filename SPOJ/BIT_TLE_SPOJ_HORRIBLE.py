import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def getsum(BITTree, i):
    s = 0
    i = i+1
    while i > 0:

        s += BITTree[i]
        i -= i & (-i)

    return s


def updatebit(BITTree, n, i, v):
    i = i+1
    while i <= n:

        BITTree[i] += v
        i += i & (-i)


def rangeUpdate(BITTree1, BITTree2, l, r, n, val):
    updatebit(BITTree1, n, l, val)
    updatebit(BITTree1, n, r+1, -val)

    updatebit(BITTree2, n, l, val * (l - 1))
    updatebit(BITTree2, n, r + 1, -val * r)


def summation(x, BITTree1, BITTree2):
    return (getsum(BITTree1, x) * x) - getsum(BITTree2, x)


def rangeSum(l, r, BITTree1, BITTree2):
    return summation(r, BITTree1, BITTree2) - summation(
        l - 1, BITTree1, BITTree2)


T = int(input().decode())
for t in range(T):
    N, C = [int(x) for x in input().decode().split()]
    BITTree1 = [0]*(N+1)
    BITTree2 = [0]*(N+1)
    for c in range(C):

        command = [int(x) for x in input().decode().split()]
        if command[0] == 0:
            l = command[1]-1
            r = command[2]-1
            v = command[3]
            rangeUpdate(BITTree1, BITTree2, l, r, N, v)
        else:

            p = command[1] - 1
            q = command[2] - 1
            tmp = rangeSum(p, q, BITTree1, BITTree2)
            sys.stdout.write(str(tmp) + "\n")
