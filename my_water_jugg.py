class waterjug:
    c = int()
    d = int()
    parent = int()


global p

obj = {}

p = 0

obj


obj[p] = waterjug()

obj[p].c = 0
obj[p].d = 0
obj[p].parent = 0


lis = [[0, 0]]
vlist = []
n = 0
check = 1


def fillA(lis, n):
    global p
    a = lis[n][0]
    b = lis[n][1]
    a = 3
    if [a, b] not in lis:
        lis.append([a, b])
        p = p + 1
        obj[p] = waterjug()
        obj[p].c = a
        obj[p].d = b
        obj[p].parent = n


def fillB(lis, n):
    global p
    a = lis[n][0]
    b = lis[n][1]
    b = 4
    if [a, b] not in lis:
        lis.append([a, b])
        p = p + 1
        obj[p] = waterjug()
        obj[p].c = a
        obj[p].d = b
        obj[p].parent = n


def emptyA(lis, n):
    global p
    a = lis[n][0]
    b = lis[n][1]
    a = 0

    if [a, b] not in lis:
        lis.append([a, b])
        p = p + 1
        obj[p] = waterjug()
        obj[p].c = a
        obj[p].d = b
        obj[p].parent = n


def emptyB(lis, n):
    global p
    a = lis[n][0]
    b = lis[n][1]
    b = 0

    if [a, b] not in lis:
        lis.append([a, b])
        p = p + 1
        obj[p] = waterjug()
        obj[p].c = a
        obj[p].d = b
        obj[p].parent = n


def BA(lis, n):
    global p
    a = lis[n][0]
    b = lis[n][1]
    v = a + b
    if (v > 3):
        a = 3
        b = v - 3
    else:
        a = v
        b = 0
    if [a, b] not in lis:
        lis.append([a, b])
        p = p + 1
        obj[p] = waterjug()
        obj[p].c = a
        obj[p].d = b
        obj[p].parent = n


def AB(lis, n):
    global p
    a = lis[n][0]
    b = lis[n][1]
    v = a + b
    if (v > 4):
        a = v - 4
        b = 4
    else:
        a = 0
        b = v
    if [a, b] not in lis:
        lis.append([a, b])
        p = p + 1
        obj[p] = waterjug()
        obj[p].c = a
        obj[p].d = b
        obj[p].parent = n


while ( True ):
    try:
        if check == 1:
            vlist.append([lis[n][0], lis[n][1]])
            fillA(lis, n)
            fillB(lis, n)
            emptyA(lis, n)
            emptyB(lis, n)
            AB(lis, n)
            BA(lis, n)
            n = n + 1
    except:
        check = 0
        print("stop now", n)
        break


# lis


n = 14

index = 0
x = 0
m = 2
k = 0
print(m, k)
while True:
    if (obj[x].c == m and obj[x].d == k):
        index = (obj[x].parent)
        m = lis[index][0]
        k = lis[index][1]
        print(m, k)
        if (index == 0):
            break
        x = 0
    x = x + 1


a = 0
while (a != 14):
    print(obj[a].c, obj[a].d, obj[a].parent)
    a = a + 1