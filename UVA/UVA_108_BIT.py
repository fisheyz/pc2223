
import io
import sys
import os
input = io.BytesIO(os.read(0,
                           os.fstat(0).st_size)).readline
# sys.stdout.write(str(sol) + "\n")


def getsum(BITTree, i):
    s = 0
    i = i+1
    while i > 0:

        s += BITTree[i]
        i -= i & (-i)
    return s


def updatebit(BITTree, n, i, v):

    i += 1

    # Traverse all ancestors and add 'val'
    while i <= n:

        # Add 'val' to current node of BI Tree
        BITTree[i] += v

        # Update index to that of parent in update View
        i += i & (-i)


def construct(arr, n):

    BITTree = [0]*(n+1)

    for i in range(n):
        updatebit(BITTree, n, i, arr[i])

    # Uncomment below lines to see contents of BITree[]
    # for i in range(1,n+1):
    #     print BITTree[i],
    return BITTree


a = [0, 9, -4, -1]
b = [-2, 2, 1, 8]
c = [-7, -6, -4, 0]
d = [-1, 8, 0, -2]


col1 = construct(a, len(a))
col2 = construct(b, len(b))
col3 = construct(c, len(c))
col4 = construct(d, len(d))
sum = 0
for i in range(len(a)):
    print(getsum(col1, i))
    print(getsum(col2, i))
    print(getsum(col3, i))
    print(getsum(col4, i))

    tmp = getsum(col1, i) + \
        getsum(col2, i) + \
        getsum(col3, i) + \
        getsum(col4, i)
    print("tmp", tmp)
    sum = max(sum, tmp)
print(sum)
# BITTree = construct(a, len(a))
# print("Sum of elements in arr[0..2] is " + str(getsum(BITTree, 2)))
# a[3] += 6
# print(a)
# updatebit(BITTree, len(a), 3, 6)
# print("Sum of elements in arr[0..5]" +
#       " after update is " + str(getsum(BITTree, 3)))
