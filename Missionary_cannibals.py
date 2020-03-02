class Position:

        def c2r(self, state):
            j = (state[0] - 2, state[1], 1, state[3] + 2, state[4])
            if not ((j[0] > j[1] >= 1) or (j[3] > j[4] >= 1)):
                if not visited_nodes.__contains__((state[0] - 2, state[1], 1, state[3] + 2, state[4])):
                    j = (state[0] - 2, state[1], 1, state[3] + 2, state[4])
                    visited_nodes.append((state[0] - 2, state[1], 1, state[3] + 2, state[4]))
                    graph[state].append([state[0] - 2, state[1], 1, state[3] + 2, state[4]])
                    graph[j] = []
                    parent[j] = state
                    self.goal(j)

        def m2r(self, state):
            j = (state[0], state[1] - 2, 1, state[3], state[4] + 2)  # move two missionaries to right side
            if not ((j[0] > j[1] >= 1) or (j[3] > j[4] >= 1)):
                if not visited_nodes.__contains__((state[0], state[1] - 2, 1, state[3], state[4] + 2)):
                    j = (state[0], state[1] - 2, 1, state[3], state[4] + 2)
                    visited_nodes.append(j)
                    graph[state].append([state[0], state[1] - 2, 1, state[3], state[4] + 2])
                    graph[j] = []
                    parent[j] = state
                    return j

        def m11cr(self, state):
            j = (state[0] - 1, state[1] - 1, 1, state[3] + 1, state[4] + 1)
            if not ((j[0] > j[1] >= 1) or (j[3] > j[4] >= 1)):
                if not visited_nodes.__contains__((state[0] - 1, state[1] - 1, 1, state[3] + 1, state[4] + 1)):
                    j = (state[0] - 1, state[1] - 1, 1, state[3] + 1, state[4] + 1)
                    visited_nodes.append(j)
                    graph[state].append([state[0] - 1, state[1] - 1, 1, state[3] + 1, state[4] + 1])
                    graph[j] = []
                    parent[j] = state
                    return j

        def c2l(self, state):
            j = (state[0] + 2, state[1], 0, state[3] - 2, state[4])
            if not ((j[0] > j[1] >= 1) or (j[3] > j[4] >= 1)):
                if not visited_nodes.__contains__((state[0] + 2, state[1], 0, state[3] - 2, state[4])):
                    j = (state[0] + 2, state[1], 0, state[3] - 2, state[4])
                    visited_nodes.append((state[0] + 2, state[1], 0, state[3] - 2, state[4]))
                    graph[state].append([state[0] + 2, state[1], 0, state[3] - 2, state[4]])
                    graph[j] = []
                    parent[j] = state
                    return j

        def m2l(self, state):
            j = (state[0], state[1] + 2, 0, state[3], state[4] - 2)
            if not ((j[0] > j[1] >= 1) or (j[3] > j[4] >= 1)):
                if not visited_nodes.__contains__((state[0], state[1] + 2, 0, state[3], state[4] - 2)):
                    j = (state[0], state[1] + 2, 0, state[3], state[4] - 2)
                    visited_nodes.append(j)
                    graph[state].append([state[0], state[1] + 2, 0, state[3], state[4] - 2])
                    graph[j] = []
                    parent[j] = state
                    return j

        def m11cl(self, state):
            j = (state[0] + 1, state[1] + 1, 0, state[3] - 1, state[4] - 1)
            if not ((j[0] > j[1] >= 1) or (j[3] > j[4] >= 1)):
                if not visited_nodes.__contains__((state[0] + 1, state[1] + 1, 0, state[3] - 1, state[4] - 1)):
                    j = (state[0] + 1, state[1] + 1, 0, state[3] - 1, state[4] - 1)
                    visited_nodes.append(j)
                    graph[state].append([state[0] + 1, state[1] + 1, 0, state[3] - 1, state[4] - 1])
                    graph[j] = []
                    parent[j] = state
                    return j

        def c1l(self, state):
            j = (state[0] + 1, state[1], 0, state[3] - 1, state[4])
            if not ((j[0] > j[1] >= 1) or (j[3] > j[4] >= 1)):
                if not visited_nodes.__contains__((state[0] + 1, state[1], 0, state[3] - 1, state[4])):
                    j = (state[0] + 1, state[1], 0, state[3] - 1, state[4])
                    visited_nodes.append(j)
                    graph[state].append([state[0] + 1, state[1], 0, state[3] - 1, state[4]])
                    graph[j] = []
                    parent[j] = state
                    return j

        def m1l(self, state):
            j = (state[0], state[1] + 1, 0, state[3], state[4] - 1)
            if not ((j[0] > j[1] >= 1) or (j[3] > j[4] >= 1)):
                if not visited_nodes.__contains__((state[0], state[1] + 1, 0, state[3], state[4] - 1)):
                    j = (state[0], state[1] + 1, 0, state[3], state[4] - 1)
                    visited_nodes.append(j)
                    graph[state].append([state[0], state[1] + 1, 0, state[3], state[4] - 1])
                    graph[j] = []
                    parent[j] = state
                    return j

        def find_solution(self, state):

                if state[2] == 0:
                    if state[0] >= 2:
                        self.c2r(state)

                    if state[1] >= 2:
                        p = self.m2r(state)                             # move two missionaries to right side
                        self.goal(p)

                    if state[0] > 0 and state[1] > 0:                 # move 1 missionary and 1 cannibal to right side
                        p = self.m11cr(state)
                        self.goal(p)

                else:
                    if state[3] >= 2:                                 # move two cannibals to left side
                        p = self.c2l(state)
                        self.goal(p)

                    if state[4] >= 2:                                  # move two missionaries to left side
                        p = self.m2l(state)
                        self.goal(p)

                    if state[3] > 0 and state[4] > 0:      # move 1 missionary and 1 cannibal to left side
                        p = self.m11cl(state)
                        self.goal(p)

                    if state[3] > 0:
                        p = self.c1l(state)
                        self.goal(p)

                    if state[4] > 0:                             # move 1 missionary to left side
                        p = self.m1l(state)
                        self.goal(p)

                i = visited_nodes.index(state)
                k = visited_nodes[i + 1]
                self.find_solution(k)

        def goal(self, state):
            if state == goal_state:
                self.parent(state)

        def parent(self, j):

            while j != start:
                path.append(j)
                self.parent(parent[j])
            path.append(start)

            for n in range(len(path)-1,0,-1):
                print(path[n])
            print(path[0])
            print("Graph: ", graph)
            exit(0)


m = Position()
graph = {}
parent = {}
path = []
temp = int(input("Enter the number of missionaries or cannibels: "))
while not temp > 0:
    temp = int(input("Enter the number of missionaries or cannibels, they should be equal in numbers!"))

start = (temp, temp, 0, 0, 0)
visited_nodes = []
bank = start[2]
print("Solution:")
print("Cannibals Missionaries River_Bank Cannibals Missionaries")
goal_state = (0, 0, 1, temp, temp)
visited_nodes.append(start)
graph[start] = []
m.find_solution(start)
