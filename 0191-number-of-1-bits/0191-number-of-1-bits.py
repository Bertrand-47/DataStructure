class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        
        while n:
            counter += n%2
            n = n >> 1
            
        return counter
        