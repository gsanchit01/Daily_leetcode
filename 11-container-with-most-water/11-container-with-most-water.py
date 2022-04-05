class Solution:
    def maxArea(self, a: List[int]) -> int:
        l=0
        r=len(a)-1
        tw=0
        while l<r:
            if a[l]>a[r]:
                tw=max(tw,a[r]*(r-l))
                r-=1
            else:
                tw=max(tw,a[l]*(r-l))
                l+=1
        return(tw)
            