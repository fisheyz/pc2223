from collections import defaultdict


t = list(map(int, input().split()))
c = input().split()

frequency = []
h = defaultdict(lambda: int(0))


def get_key(val):
    for key, value in h.items():
        if val == value:
            return key


for i in range(t[0]):
    h[str(c[i])] += 1
frequency = list(h.values())

frequency.sort(reverse=True)
for i in range(len(frequency)):
    tmp = get_key(frequency[i])
    for j in range(frequency[i]):
        print(tmp, end=' ')
    del h[tmp]
