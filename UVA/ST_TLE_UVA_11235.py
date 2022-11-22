# based on https://falloutcodes.com/2017/03/28/uva-11235-frequent-values/
import math
from collections import defaultdict
import io
import sys
import os
import time
input = io.BytesIO(os.read(0,
                           os.fstat(0).st_size)).readline

st = time.perf_counter()

count = defaultdict(lambda: int(0))


def buildTree(root, left, right):
    if right < left:
        return
    if left == right:
        tree[root] = frequencies[left]
        return
    mid = left+(right-left)//2
    buildTree(2*root+1, left, mid)
    buildTree(2*root+2, mid+1, right)
    tree[root] = max(tree[2*root+1], tree[2*root+2])


def query(root, left, right, a, b):

    if left > b or right < a:
        return 0
    elif left >= a and right <= b:
        return tree[root]
    mid = left+(right-left)//2
    tmp_l = 2*root+1
    tmp_r = 2*root+2
    l = query(tmp_l, left, mid, a, b)
    r = query(tmp_r, mid+1, right, a, b)
    return max(l, r)


frequencies = []
start = []

t = input()
while int(t.split()[0]) != 0:
    n, q = [int(x) for x in t.split()]
    arr = [int(k) for k in input().split()]

    N = len(arr)
    nodes = 2*(2**math.ceil(math.log2(N)))
    tree = [0] * nodes

    '''
    # lets say we query the range [5,6], arr[5] = 5, arr[6] = 5 and we know that the input is of stricly increasing order so there is no value !=,
    so all we need to do it count the ammount of repetitions from one end of the range to the other
    #  if we query the range [i,j] for example. arr[i] = 5, arr[j] = 10, then the most frequent number will be either arr[i] or arr[j] or in between these.
    - the frequency of arr[i] can be found by count[i]+start[i]
    - the frequecy of arr[j] j - start[j] + 1
    - the most frequent element fro arr[i+1, j-1] we can find by querying the segment tree
    '''

    '''We create 2 arrays, frequencies[] which stores the maximum frequecy for each value of arr[] and start which stores the index they first appear
    '''

    for x in arr:
        count[x] += 1

    # previous implementation was O(N^2) because:
    # while i<N
    #   while arr[i] != previous
    #       ...append to arrays
    prev = arr[0]
    tmp = 0
    for i in range(0, N):
        frequencies.append(count[arr[i]])
        if arr[i] != prev:
            tmp = i
        start.append(tmp)
        prev = arr[i]

    buildTree(0, 0, N-1)

    for i in range(q):
        a, b = [int(x)-1 for x in input().split()]
        if arr[a] != arr[b]:
            k = frequencies[a]+start[a]
            cnt1 = k-a
            cnt2 = b - start[b] + 1
            cnt3 = query(0, 0, N-1, k, start[b]-1)
            sol = max(cnt1, cnt2, cnt3)
            sys.stdout.write(str(sol) + "\n")
        else:
            sol = b-a+1
            sys.stdout.write(str(sol) + "\n")
    t = input()
    count.clear()
    frequencies.clear()
    start.clear()
    tree.clear()
end = time.perf_counter()

print("DURATION", end-st)
