import math
from functools import reduce
import sys

solution = []
tmp = []


def updateValue(root, left, right, i, val):
    if (i < left or i > right):
        return

    if (left >= i and right <= i):
        tree[root] = val

    if (right != left):
        mid = left+(right-left)//2
        updateValue(2*root+1, left, mid, i, val)
        updateValue(2*root+2, mid+1, right, i, val)
        tree[root] = tree[2*root+1] * tree[2*root+2]


def buildTree(root, left, right):
    if right < left:
        return

    if left == right:
        tree[root] = k[left]
        return

    mid = left+(right-left)//2
    buildTree(2*root+1, left, mid)
    buildTree(2*root+2, mid+1, right)
    tree[root] = tree[2*root+1] * tree[2*root+2]


def query(root, left, right, a, b):
    if left > b or right < a:
        return 0
    elif left >= a and right <= b:
        tmp.append(tree[root])
        return
    mid = left+(right-left)//2
    query(2*root+1, left, mid, a, b)
    query(2*root+2, mid+1, right, a, b)
    return


def sign(x):
    if x == 0:
        return 0
    elif x < 0:
        return '-'
    else:
        return '+'


n, l = [int(x) for x in input().split()]

while True:

    nodes = 2*(2**math.ceil(math.log2(n)))
    tree = [0] * nodes

    k = [int(x) for x in input().split()]

    buildTree(0, 0, n-1)
    try:
        for i in range(l):
            q = [x for x in input().split()]
            if q[0] == 'C':
                # the starting index on the test cases is 1 but python starts at 0,
                # hence we subtract 1 from indexes on the test cases
                updateValue(0, 0, n-1, int(q[1])-1, int(q[2]))
            else:
                query(0, 0, n-1, int(q[1])-1, int(q[2])-1)
                prod = reduce((lambda x, y: x*y), tmp)
                solution.append(sign(prod))
                tmp.clear()

        print(*solution, sep='')

        solution.clear()
        tree.clear()

        n, l = [int(x) for x in input().split()]

    except EOFError:
        sys.exit(1)
