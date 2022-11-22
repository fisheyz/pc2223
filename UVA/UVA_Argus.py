import heapq

q = []
solution = []

#   for _ in range(nr of queries):
#       pop the highest priority elements
#       increment priority(period) of each element
#       add them on the queue again
#

t = input()
while t != '#':
    line = t.split()
    q.append((int(line[2]), int(line[1]), int(line[2])))
    heapq.heapify(q)
    t = input()

# let there be k queries to do and since the time complexity of the heapreplace method is log(n)
# the overall time complexity on the program is klog(n)
#
# https://stackoverflow.com/questions/33701160/python-heapq-difference-between-heappushpop-and-heapreplace
for i in range(1, int(input())+1):
    tmp = q[0]
    solution.append(tmp[1])
    heapq.heapreplace(q, (tmp[0]+tmp[2], tmp[1], tmp[2]))

print(*solution, sep='\n')
