t = int(input())

for i in range(t):
    a = sorted([int(k) for k in input().split()])
    if a[2] == a[0]+a[1]:
        print("Yes")
    else:
        print("No")
