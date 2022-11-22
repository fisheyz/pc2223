from collections import defaultdict
from itertools import islice
d = defaultdict(lambda: 0)
t = input()
big_s = ""


def take(n, iterable):
    return list(islice(iterable, n))


for i in range(int(t)):
    s = input()
    big_s += s
n = len(big_s)
test = big_s

while n > 0:
    tmp = test[:2]
    d[str(tmp)] += 1
    test = test[1:]
    n = len(test)

sorted_d = {val[0]: val[1]
            for val in sorted(d.items(), key=lambda x: (-x[1], x[0]))}
n = take(5, sorted_d.items())
for i in range(5):
    print(n[i][0], n[i][1])
