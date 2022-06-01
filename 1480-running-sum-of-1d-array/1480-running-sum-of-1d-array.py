class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        s=0
        for i in nums:
            s=s+i
            l.append(s)
        return l