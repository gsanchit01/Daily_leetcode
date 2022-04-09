class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict()
        l=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in range(k):
            l.append(max(zip(d.values(), d.keys()))[1])
            d[max(zip(d.values(), d.keys()))[1]]=0
        return l