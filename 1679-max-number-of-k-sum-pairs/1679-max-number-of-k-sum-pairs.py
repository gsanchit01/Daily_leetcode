class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        b = {}
        ans = 0
        for i in nums:
			# If there is num in table and is not used
            if k - i in b and b[k - i] > 0:
                ans += 1
                b[k - i] -= 1  # used
            elif i not in b:
                b[i] = 1
            else:
                b[i] += 1
        
        return ans