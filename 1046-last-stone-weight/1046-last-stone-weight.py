class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            a=max(stones)
            stones.remove(max(stones))
            b=max(stones)
            stones.remove(max(stones))
            if (a-b)!=0:
                stones.append(a-b)
        if (len(stones)==0):
            return 0
        else:
            return stones[0]