class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sort_nums = sorted(nums)
        
        if nums == sort_nums:
            return 0
        low = min(i for i in range(n) if nums[i] != sort_nums[i])
        high = max(i for i in range(n) if nums[i] != sort_nums[i])
        
        return high-low+1