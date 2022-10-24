class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        L = 0
        
        
        for r in range(len(nums)):
            if nums[r] !=0:
                temp = nums[L]
                nums[L] = nums[r]
                nums[r] = temp
                L+=1
                
            