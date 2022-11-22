t = input()


def reverse(num):
    tmp = str(num)
    reversed_num = ''
    for i in range(0, len(tmp)):
        reversed_num = tmp[i] + reversed_num

    return reversed_num


for i in range(int(t)):
    s = input().replace("+", " ").replace("=", " ").split()
    tmp = map(reverse, s)
    # a = list(tmp)
    a = [int(x) for x in list(tmp)]
    # print(a[0], "+", a[1], "=", a[2], a[0]+a[1])
    if a[0] + a[1] == a[2]:
        print("true")
    else:
        print("false")
