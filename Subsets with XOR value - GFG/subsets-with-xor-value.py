#User function Template for python3

import math
class Solution:
    def subsetXOR(self, arr, N, K): 
        # code here
        def helper(i,n,k,arr,x):
            if i==n:
                return x==k
            if dp[i][x]!=-1:
                return dp[i][x]
            
            take= helper(i+1,n,k,arr,x^arr[i])
            nonTake = helper(i+1,n,k,arr,x)
            dp[i][x]=take+nonTake
            
            return dp[i][x]
        
        dp=[[-1 for _ in range(201)]for _ in range(21)]
        return helper(0,N,K,arr,0)

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K = input().split()
        N = int(N)
        K = int(K)
        arr = input().split(' ')
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        print(ob.subsetXOR(arr,N,K))
# } Driver Code Ends