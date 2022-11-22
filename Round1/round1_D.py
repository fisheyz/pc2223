
l = input()
M = list(input())
M = [int(x) for x in M]
t = input()
G = set()


def countDiff(l, r):
    for i in range(l, r+1):
        if M[i] not in G:
            G.add(M[i])
    print(len(G))
    G.clear()


def swap(p, x):
    M[p] = int(x)


for i in range(int(t)):
    q = [int(x) for x in input().split()]
    if q[0] == 1:
        swap(q[1], q[2])
    else:
        countDiff(q[1], q[2])
