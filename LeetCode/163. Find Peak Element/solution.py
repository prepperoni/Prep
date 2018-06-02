class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def neighbors(nums, i):
            left, right = -float('inf'), -float('inf')
            
            if i != 0:
                left = nums[i-1]
            if i != len(nums) - 1:
                right = nums[i+1]
            
            return left, right
        
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = int((lo + hi) / 2)
            midVal = nums[mid]
            leftVal, rightVal = neighbors(nums, mid)
            
            if leftVal < midVal > rightVal:
                return mid
            if leftVal > midVal:
                hi = mid - 1
            else:
                lo = mid + 1
        
    