t = input()

for i in range(int(t)):
    a, b = [x for x in input().split()]
    pos = 0
    count = len(a)
    for i in range(len(b)):
        if b[i] == a[pos]:
            count -= 1
            pos += 1
        if count == 0:
            print("yes")
            break
    if count > 0:
        print("no")
