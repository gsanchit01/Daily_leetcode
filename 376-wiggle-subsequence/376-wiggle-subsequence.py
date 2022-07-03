class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        new_nums = [nums[0]]
        for x in nums[1:]:
            if x == new_nums[-1]:
                continue
            if len(new_nums)==1: 
                new_nums.append(x)
                continue
            if x > new_nums[-1] < new_nums[-2] or x < new_nums[-1] > new_nums[-2]:
                new_nums.append(x)
            else:
                new_nums[-1] = x
        return len(new_nums)