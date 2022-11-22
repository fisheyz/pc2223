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


def rangeUpdate(BITTree, l, r, n, val):
    updatebit(BITTree, n, l, val)
    updatebit(BITTree, n, r+1, -val)


t = int(input().decode())
for c in range(t):
    N, U = [int(x) for x in input().decode().split()]
    BITTree = [0]*(N+1)
    for u in range(U):
        L, R, Val = [int(x) for x in input().decode().split()]
        rangeUpdate(BITTree, L, R, N, Val)
    Q = int(input().decode())
    for q in range(Q):
        i = int(input().decode())
        sys.stdout.write(str(getsum(BITTree, i)) + "\n")
