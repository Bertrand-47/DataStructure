class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        i = 0 
        counter = 0
        binary_list = []
        ans = []
        while i <= n:    
            binary = bin(i).replace("0b", "")
            binary_list.append(binary)   
            i+=1
        
        for i in binary_list:
            ans.append(i.count("1"))
        return ans
            
        
            