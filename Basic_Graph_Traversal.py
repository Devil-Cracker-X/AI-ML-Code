
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
    print("Enter Child")
    glist = []
    i = 0
    while i < n:
        ch = int(input())
        glist.insert(i, ch)
        graph[p] = glist
        i += 1
    del glist


print("enter number of nodes")
nn = int(input())
j = 0
while j < nn:
    add_child()
    j += 1

to_csv()
print(graph)
