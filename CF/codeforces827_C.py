t = int(input())

for i in range(t):
    size = int(input())
    a = sorted([int(k) for k in input().split()])
    if len(a) == 1:
        print("yes")
    else:
        for i in range(size-1):
            if a[i] == a[i+1]:
                print("No")
                break
            if i == size-2:
                print("Yes")
