import bisect
t = int(input())
solution = []

for i in range(t):
    n, q = [int(k) for k in input().split()]
    step = [int(k) for k in input().split()]
    questions = [int(k) for k in input().split()]

    prev = 0
    totalsteps = []
    maxstep = []
    for j in range(0, len(step)):
        totalsteps.append((step[j]+prev))
        prev = totalsteps[j]

    prv = 0
    for s in range(0, len(step)):
        prv = max(step[s], prv)
        maxstep.append(prv)

    for x in questions:
        if x == 0 or x < step[0]:
            solution.append(0)
        else:
            sol = bisect.bisect_right(maxstep, x)-1
            solution.append(totalsteps[sol])
    print(*solution, sep=" ")
    solution.clear()
