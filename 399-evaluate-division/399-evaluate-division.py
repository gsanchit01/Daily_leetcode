class Solution:
    
	# find path in graph equationValues
    def findPath(self, A: str, B: str) -> float:
        if A == B:
            return 1 if A in self.equationValues.keys() else -1
        
        seen = set()
        queue = [(A, 1)]
        while queue:
            Ai, value = queue.pop()
            for Bi, valuei in self.equationValues[Ai].items():
                if B == Bi:
                    return value * valuei
                else:
                    if Bi not in seen:
                        seen.add(Bi)
                        queue.append((Bi, value * valuei))
        return -1
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
		# set up graph
        self.equationValues = defaultdict(dict)
        for (Ai, Bi), value in zip(equations, values):
            self.equationValues[Ai][Bi] = value
            self.equationValues[Bi][Ai] = 1 / value
    
        ans = []
        for (Cj, Dj) in queries:
            ans.append(self.findPath(Cj, Dj))
                
        return ans