import math


def func(x):
    return a*x + b*math.sin(x) - c


def mySearch():
    high = 1000000
    low = -1000000
    prev = None
    while prev != round((high+low) / 2.0, 6):
        middle = low + (high-low)/2.0
        f = func(middle)
        if f == 0:
            return round(middle, 6)
        elif f > 0:
            high = middle+1
        else:
            low = middle
        prev = round(middle, 6)
    return prev


t = int(input())

for i in range(t):
    config = input().split()
    a, b, c = [int(x) for x in config]
    print(mySearch())
