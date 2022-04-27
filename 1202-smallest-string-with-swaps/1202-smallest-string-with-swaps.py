class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def findSet(x):
            if x != p[x]:
                p[x]=findSet(p[x])
            return p[x]
        def union(x,y):
            return link(findSet(x), findSet(y))
        def link(x,y):
            if rank[x]>rank[y]:
                p[y]=x
            else:
                p[x]=y
                if rank[x] == rank[y]:
                    rank[y] += 1
        
        n = len(s)
        p=[x for x in range(n)]
        rank=[0]*n
        
        for x,y in pairs:
            if findSet(x) != findSet(y):
                union(x,y)
        sets = defaultdict(list)
        for x in range(n):
            sets[findSet(x)] += [x]
        
        res = [None]*n
        for rep in sets:
            indices = sets[rep]
            values = [s[x] for x in indices]
            start = 0
            values.sort()
            for ind in indices:
                res[ind] = values[start]
                start+=1
        ans = "".join(res)
        return ans