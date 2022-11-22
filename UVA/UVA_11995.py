import heapq
from collections import deque


t = input()
while True:
    isQ, isStk, isHp = True, True, True
    q, stk, hp = deque(), deque(), []

    try:
        for i in range(0, int(t)):
            cmd = (input().split())
            if cmd[0] == '1':
                q.append(cmd[1])
                stk.append(cmd[1])
                # since heapq doesnt have any straightfoward way to get the max value I believe
                # the simplest way to do it is to inver the numbers. Then heapify will sort the values
                # from the lowest to the highest and when we take the absolute value of the lowest negative number
                # in the array we get the highest number
                hp.append(-int(cmd[1]))
                heapq.heapify(hp)
            else:
                if isQ and (len(q) == 0 or q.popleft() != cmd[1]):
                    isQ = False
                if isStk and (len(stk) == 0 or stk.pop() != cmd[1]):
                    isStk = False
                if isHp and (len(hp) == 0 or abs(heapq.heappop(hp)) != int(cmd[1])):
                    isHp = False
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

# let T be the number of line on the input file
# Appending to a list in done in O(1)
# heapq.heapify() is done in O(n)
# deque.popleft is O(1)
# deque.pop() is O(n)
# heapq.heappop is O(log(n))
# Since all the methods are independant from each other the overall time complexity would be O(n)
