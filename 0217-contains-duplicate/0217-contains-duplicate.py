class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mapping ={}
        
        for i in range(len(nums)):
            if mapping.get(nums[i]) == None:
                mapping[nums[i]] = 1
            else:
                return True
        return False
        
            