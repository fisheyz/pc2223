import heapq
from collections import deque

q = deque()
stk = deque()
hp = []


t = input()
while True:
    isQ, isStk, isHp = True, True, True
    try:
        for i in range(0, int(t)):
            cmd = (input().split())
            if cmd[0] == '1':
                q.append(cmd[1])
                stk.append(cmd[1])
                hp.append(-int(cmd[1]))
                heapq.heapify(hp)
            else:
                tmp = abs(heapq.heappop(hp))
                if q.popleft() != cmd[1]:
                    isQ = False
                if stk.pop() != cmd[1]:
                    isStk = False
                if tmp != int(cmd[1]):
                    isHp = False
        # print("q", isQ)
        # print("stk", isStk)
        # print("hp", isHp)

        if not isQ and not isStk and not isHp:
            print("impossible")
        elif not isStk and not isHp:
            print("queue")
        elif not isQ and not isHp:
            print("stack")
        elif not isQ and not isStk:
            print("priority queue")
        else:
            print("not sure")
        t = input()
    except EOFError as e:
        break
# print("Solution")
