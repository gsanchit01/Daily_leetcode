class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

		# minimum[i] = min(nums[:i + 1])
        minimum = [nums[0]] * len(nums)
        for i, num in enumerate(nums[1:]):
            minimum[i + 1] = min(minimum[i], num)

        monStack = []
		# we traverse nums from the back
        for i, num in enumerate(reversed(nums)):
		    # if num is larger than the top of the stack (so it could a the nums[k] < nums[j] situation)
            while monStack and monStack[-1] < num:
			    # we check if there is a possible nums[i] < nums[k] situation
                if monStack.pop() > minimum[~i]:   # ~i == -(i + 1)
                    return True
            monStack.append(num)
            
        return False