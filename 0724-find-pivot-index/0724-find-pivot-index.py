class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index in range(len(nums)):
            if index == 0:
                right_element_sum = sum(nums[1:len(nums)])
                left_element_sum = 0
                if right_element_sum == 0:
                    return index
            pivot_element = index
            right_element_sum = sum(nums[index+1:len(nums)])
            left_element_sum = sum(nums[0:pivot_element])
            if right_element_sum == left_element_sum:
                return pivot_element
        return -1
            
        
        
        