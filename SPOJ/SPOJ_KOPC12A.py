

def f(mid):
    cost = 0
    for i in range(len(h)):
        cost += c[i]*abs((h[i] - mid))
    return cost


def ternary_search(left, right):
    while (left < right):
        left_third = left + (right - left) // 3
        right_third = right - (right - left) // 3
        if f(left_third) < f(right_third):
            right = right_third - 1
        else:
            left = left_third + 1

    return f((left + right) // 2)


t = int(input())
l = 0
r = 10000

for i in range(t):
    s = int(input())
    h = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    sol = ternary_search(l, r)
    print(sol)
