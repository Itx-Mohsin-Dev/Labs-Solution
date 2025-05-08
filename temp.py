# class Graph:
#     def __init__(self, size):
#         self.V = size
#         self.adj_list = [[] for _ in range(size)]  # Create an adjacency list

#     def addedge(self, v, w):
#         self.adj_list[v].append(w)  # Add w to the list of v

#     def BFS(self, s):
#         visited = [False] * self.V  # Initialize visited list
#         queue = []  # Initialize queue

#         visited[s] = True  # Mark the starting node as visited
#         queue.append(s)  # Enqueue the starting node

#         while queue:  # While the queue is not empty
#             s = queue.pop(0)  # Dequeue a vertex from the queue
#             print(s, end=" ")  # Print the dequeued vertex

#             # Get all adjacent vertices of the dequeued vertex
#             for i in self.adj_list[s]:
#                 if not visited[i]:  # If the vertex has not been visited
#                     visited[i] = True  # Mark it as visited
#                     queue.append(i)  # Enqueue it

# # Create a graph and add edges
# graph = Graph(5)
# graph.addedge(0, 1)
# graph.addedge(0, 2)
# graph.addedge(1, 2)
# graph.addedge(2, 0)
# graph.addedge(2, 3)
# graph.addedge(3, 3)

# print("BFS from index 2:")
# graph.BFS(2)


# # -----------------------
# from collections import deque
# class graph:
#     def _init_(self):
#         self.l={}
#     def addedge(self,p,c):
#         if(p not in self.l):
#             self.l[p]=[]
#         self.l[p].append(c)
#     def _str_(self):
#         return str(self.l)
#     def bfs(self,start):
#         visited=[]
#         queue=deque()
#         visited.append(start)
#         queue.append(start)
#         while queue:
#             node=queue.popleft()
#             print(node)
#             for neighbour in self.l[node]:
#                 if neighbour not in visited:
#                     visited.append(neighbour)
#                     queue.append(neighbour)

# g=graph()
# g.addedge(0,1)
# g.addedge(0,2)
# g.addedge(1,2)
# g.addedge(2,0)
# g.addedge(2,3)
# g.addedge(3,3)
# print(g)
# print("The BFS Traversal of the Graph is:")
# g.bfs(1)



from collections import deque
class graph:
    def _init_(self):
        self.l=[]
    def addedge(self,p,c):
        if(p not in self.l):
            self.l[p]=[]
        self.l[p].append(c)
    def _str_(self):
        return str(self.l)
    def bfs(self,start,goal):
        visited=[]
        queue=deque()
        visited.append(start)
        queue.append(start)
        while queue:
            node=queue.popleft()
            print(node)
            if(node==goal):
                print("GOAL NODE FOUND...!!!")
                return 1
            for neighbour in self.l[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

g=graph()
g.addedge('A','B')
g.addedge('A','F')
g.addedge('A','D')
g.addedge('A','E')
g.addedge('B','K')
g.addedge('B','J')
g.addedge('B','A')
g.addedge('F','A')
g.addedge('D','G')
g.addedge('D','A')
g.addedge('E','C')
g.addedge('E','H')
g.addedge('E','I')
g.addedge('E','A')
g.addedge('K','N')
g.addedge('K','M')
g.addedge('K','B')
g.addedge('J','B')
g.addedge('G','D')
g.addedge('C','I')
g.addedge('H','I')
g.addedge('I','I')
g.addedge('I','E')
g.addedge('I','L')
g.addedge('N','K')
g.addedge('M','K')
g.addedge('L','I')


print(g)
print("The BFS Traversal of the Graph is:")
g.bfs('A','G')