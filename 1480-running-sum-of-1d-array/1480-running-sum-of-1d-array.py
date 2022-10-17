class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        sum_list =[]
        for i in nums:
            sum+=i
            sum_list.append(sum)
        return sum_list