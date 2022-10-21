class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        order = []
        dictionary_one = {'}':'{',')':'(', ']':'['}
        
        for c in s:
            if c in dictionary_one:
                if order and order[-1] == dictionary_one[c]:
                    order.pop()
                else:
                    return False
            else:
                order.append(c)
        
        return True if not order else False
                
        
            
            
    
        