class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def combSum(ind, ans, ds):
            if len(ds)>k or sum(ds)>n:
                return
            if len(ds)==k and sum(ds)==n:
                ans.append(ds.copy())
                return
            for i in range(ind, 10):
                ds.append(i)
                combSum(i+1, ans, ds)
                ds.pop()
            return ans
                
        return combSum(1, [], [])