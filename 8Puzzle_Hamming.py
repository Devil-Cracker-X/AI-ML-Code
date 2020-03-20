
import sys


class Puzzle:
    count = 0
    def check_goal(self,pzl1,pzl2):

        if pzl1==tuple(pzl2):
            print("goal achieved!")
            for j in visited_pzl:
                print(j)
            exit(0)

    def Swap(self, temp_pzl, a, b):
        temp=temp_pzl[a]
        temp_pzl[a]=temp_pzl[b]
        temp_pzl[b]=temp
        return temp_pzl

    def pz0(self,first_pzl,list_pzl):
        graph[first_pzl] = []
        s = self.Swap(list_pzl.copy(), 0, 1)

        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 0, 3)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance


    def pz1(self, first_pzl, list_pzl):
        graph[first_pzl] = []
        s = self.Swap(list_pzl.copy(), 1, 0)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 1, 2)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 1, 4)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance


    def pz2(self, first_pzl, list_pzl):
        graph[first_pzl] = []
        s = self.Swap(list_pzl.copy(), 2, 1)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 2, 5)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance


    def pz3(self, first_pzl, list_pzl):
        graph[first_pzl] = []
        s = self.Swap(list_pzl.copy(), 3, 0)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 3, 4)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 3, 6)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance


    def pz4(self, first_pzl, list_pzl):
        graph[first_pzl] = []
        s = self.Swap(list_pzl.copy(), 4, 1)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 4, 3)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 4, 5)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 4, 7)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance


    def pz5(self, first_pzl, list_pzl):
        graph[first_pzl] = []
        s = self.Swap(list_pzl.copy(), 5, 2)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 5, 4)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 5, 8)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance


    def pz6(self, first_pzl, list_pzl):
        graph[first_pzl] = []
        s = self.Swap(list_pzl.copy(), 6, 3)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 6, 7)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance


    def pz7(self, first_pzl, list_pzl):
        graph[first_pzl] = []
        s = self.Swap(list_pzl.copy(), 7, 4)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 7, 6)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 7, 8)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance


    def pz8(self, first_pzl, list_pzl):
        graph[first_pzl] = []
        s = self.Swap(list_pzl.copy(), 8, 5)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance

        s = self.Swap(list_pzl.copy(), 8, 7)
        if not visited_pzl.__contains__((tuple(s))):
            ham_distance = self.haming(s)
            dist[tuple(s)] = ham_distance


    def find_states(self,first_pzl):
        list_pzl = list(first_pzl)

        if first_pzl[0] == 0:
            self.pz0(first_pzl, list_pzl)


        if first_pzl[1] == 0:
            self.pz1(first_pzl, list_pzl)


        if first_pzl[2] == 0:
            self.pz2(first_pzl, list_pzl)


        if first_pzl[3] == 0:
            self.pz3(first_pzl, list_pzl)


        if first_pzl[4] == 0:
            self.pz4(first_pzl, list_pzl)


        if first_pzl[5] == 0:
            self.pz5(first_pzl, list_pzl)


        if first_pzl[6] == 0:
            self.pz6(first_pzl, list_pzl)


        if first_pzl[7] == 0:
            self.pz7(first_pzl, list_pzl)


        if first_pzl[8] == 0:
            self.pz8(first_pzl, list_pzl)


        v = min(dist.values())
        for key, value in dist.items():
            if v == value:
                s = key
                break
        graph[first_pzl].append(s)
        visited_pzl.append(tuple(s))
        dist.clear()
        self.count += 1
        self.check_goal(s, final)
        self.find_states(s)


    def haming(self, s):
        ham_distance = 0
        for i in range(9):
            if not s[i] == final[i]:
                ham_distance += 1

        return ham_distance


pz = Puzzle()
print("Welcome to 8puzzle")
print("We have to reach from 1, 2, 5, 3, 4, 0, 6, 7, 8  to  1, 4, 2, 3, 7, 5, 6, 0, 8")
start = [1, 2, 5, 3, 4, 0, 6, 7, 8]
parent = {}
final = [1, 4, 2, 3, 7, 5, 6, 0, 8]
graph = {}
path = []
dist = {}

visited_pzl=[tuple(start)]

sys.setrecursionlimit(5000)
print("Sequence is")
pz.find_states(tuple(start))
