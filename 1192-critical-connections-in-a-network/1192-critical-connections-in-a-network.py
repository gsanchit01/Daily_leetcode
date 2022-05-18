class Solution:
    def union(self, i: int, j: int):
        self.parent[i] = self.find(j)
        
    def find(self, i: int):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
    
    def strongConnect(self, i: int, k: int):
        self.index[i] = self.currIndex
        self.lowLink[i] = self.currIndex
        self.currIndex += 1
        self.stack.append(i)
        self.onStack[i] = True
            
        for j in self.graph[i]:
            if self.find(j) != self.find(k):
                if self.index[j] is None:
                    self.strongConnect(j, i)
                    self.lowLink[i] = min(self.lowLink[i], self.lowLink[j])
                elif self.onStack[j]:
                    self.lowLink[i] = min(self.lowLink[i], self.index[j])
                
        if self.lowLink[i] == self.index[i]:
            while self.stack:
                j = self.stack.pop()
                self.onStack[j] = False
                if i == j:
                    break
                else:
                    self.union(j, i)
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # build graph
        self.graph = defaultdict(set)
        for a, b in connections:
            self.graph[a].add(b)
            self.graph[b].add(a)
        
        # setup for strongConnect
        self.index, self.lowLink = [None] * n, [0] * n
        self.stack, self.onStack = [], [False] * n
        self.currIndex = 0
        self.parent = [i for i in range(n + 1)]
        
        # find strongly connected components
        for i in range(n):
            if self.index[i] is None:
                self.strongConnect(i, n)
        
        # identify critical connections
        toReturn = []
        for i in range(n):
            for j in self.graph[i]:
                if i < j and self.find(j) != self.find(i):
                    toReturn.append([i, j])
                    
        return toReturn