class Solution:
    def calPoints(self, ops: List[str]) -> int:
        r = []
        for i in ops:
            if i == '+':
                r.append(r[-1] + r[-2])
            elif i == 'D':
                r.append(2*r[-1])
            elif i == 'C':
                r.remove(r[-1])
            else:
                r.append(int(i))
        return sum(r)