def placement(dist):
    placed = 1
    pos1 = 0
    # if placed == c:
    #     return 1
    for pos2 in range(1, n):
        if houses[pos2] - houses[pos1] >= dist:
            placed += 1
            pos1 = pos2
            if placed >= c:
                return True
    return False


def mysearch():
    low = 0
    high = houses[-1]//c
    while(low < high):
        # Used the +1 because, to prevent infinite loop
        mid = low + (high-low+1)//2
        if (placement(mid) == True):
            low = mid
        else:
            high = mid - 1
    return low


t = int(input())
for i in range(t):
    n, c = [int(x) for x in input().split()]
    houses = []

    for i in range(n):
        houses.append(int(input()))

    houses.sort()

    sol = mysearch()
    print(sol)
