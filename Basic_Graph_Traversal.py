import csv

graph = {}
w = csv.writer(open("output.csv", "w"))


def add_parent():
    print("Enter Parent")
    x = int(input())
    return x


def to_csv():
    for key, val in graph.items():
        w.writerow([key, val])


def add_child():
    p = add_parent()
    print("number of child")
    n = int(input())
    if n == 0:
        print("No Child")
    print("Enter Child")
    gList = []
    i = 0
    while i < n:
        ch = int(input())
        gList.insert(i, ch)
        graph[p] = gList
        i += 1
    del gList


def bfs():
    queue = []
    final = []
    for x in graph:
        if not queue.__contains__(x):
            queue.append(x)
            final.append(x)
        temp = graph[x]
        for y in temp:
            if not queue.__contains__(y):
                queue.append(y)
                final.append(y)
    print(final)


print("enter number of nodes ")
nn = int(input())
j = 0
while j < nn:
    add_child()
    j += 1

to_csv()
print(graph)
bfs()
