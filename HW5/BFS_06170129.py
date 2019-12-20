from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def BFS(self, s): 
        queue = []
        explored = []
        queue.append(s) 
        visited = []
        
        while len(queue) > 0:
            v = queue.pop(0)
            explored.append(v)  
            if v not in visited:
                visited.append(v)
                for i in self.graph[v]:
                    explored.append(i)
                    for j in explored:
                        queue.append(j)
        return visited

    def DFS(self, s):
        stack = []
        explored = []
        stack.append(s) 
        visited = []
        
        while len(stack) > 0:
            v = stack.pop()
            explored.append(v)
            if v not in visited:
                visited.append(v)
                for i in self.graph[v]:
                    if i not in explored:
                        explored.append(i)
                        for j in explored:
                            stack.append(j)
        return visited
