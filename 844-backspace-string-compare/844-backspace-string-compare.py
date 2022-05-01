class Solution:
    def backspaceCompare(self, s, t):
        return self.parse(s) == self.parse(t)
    
    def parse(self, x):
            res = []
            for c in x:
                if c != "#":
                    res.append(c)
                else:
                    if res: res.pop()
            return res
        