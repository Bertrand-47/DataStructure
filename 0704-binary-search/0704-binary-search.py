class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        splitter = int(len(nums)/2)
        
        if target >= nums[splitter]:
            for i in range(splitter, len(nums)):
                if nums[i] == target:
                    return i
            return -1               
        else:
            for i in range(splitter):
                if nums[i] == target:
                    return i
            return -1
 
                
            
        