class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        
        while n:
            n = n & (n - 1)
            counter +=1
        return counter
        