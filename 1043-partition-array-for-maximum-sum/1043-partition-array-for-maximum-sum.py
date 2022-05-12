class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], K: int) -> int:
        dp = [0 for i in range(len(arr))]
        for i in range(len(arr)):
            dp[i] = arr[i] + (dp[i-1] if i-1>=0 else 0)
            temp = arr[i]
            for j in range(1,K):
                if i-j>=0:
                    index = i-j
                    temp = max(temp,arr[i-j])
                    dp[i] = max(dp[i],temp*(i-index+1) + (dp[index-1] if index-1 >=0 else 0))
        return dp[-1]