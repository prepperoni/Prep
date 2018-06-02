class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        old_nums = {}

        for i, x in enumerate(nums):
        	if target - x in old_nums:
        		return [old_nums[target - x], i]
        	old_nums[x] = i