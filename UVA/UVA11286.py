import sys
from collections import defaultdict

# was under the impression Sets had order, they dont!!!! so I believe there is no need to use one

solution = []
popularity = defaultdict(lambda: int(0))
# classesset = set()
t = sys.stdin.readline()

while int(t) != 0:
    for i in range(int(t)):
        froshclasses = sys.stdin.readline().split()
        # classesset = sorted(set([int(x) for x in froshclasses]))
        classesset = sorted([int(x) for x in froshclasses])
        popularity[str(classesset)] += 1

    maxval = max(popularity.values())
    maxcounter = len([k for (k, v) in popularity.items() if v == maxval])

    if maxval == 1:
        maxval = sum(popularity.values())
    else:
        maxval = maxval*maxcounter

    solution.append(maxval)
    popularity.clear()
    t = sys.stdin.readline()

print(*solution, sep='\n')
