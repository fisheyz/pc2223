import sys

t = sys.stdin.readline()
inpt = []
s = set()
outpt = []

for i in range(int(t)):
    lines = sys.stdin.readline()
    # take the snowflakes and put themm into an array
    for _ in range(int(lines)):
        inpt += sys.stdin.readline().split()
    inpt = [int(x) for x in inpt]
    k, j, tmpmax = 0, 0, 0
    # Iterate over the array of snowflakes, for every element, check if they are in set(s)
    # If element k IS NOT in set(s) we add it to the set(s) and update the tmpmax var with the size of the set (which is currently the longest thread of snowflakes)
    # If element k IS IN set(s) it meant it is a duplicated element so we remove all the ementent in the array untill the first ocurrence of inpt[k]
    while k < int(lines):
        if inpt[k] not in s:
            s.add(inpt[k])
            tmpmax = max(tmpmax, len(s))
        else:
            while j < k and inpt[k] != inpt[j]:
                s.remove(inpt[j])
                j += 1
            j += 1
        k += 1
    outpt.append(tmpmax)
    s.clear()
    inpt.clear()
print(*outpt, sep='\n')
