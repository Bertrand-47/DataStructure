class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        
        
        original_number = x
        if x >= 0:
            
            while x != 0:
                last_digit = x % 10
                reverse = reverse * 10 + last_digit
                x = x // 10
            if reverse == original_number:
                return True
            else:        
                return False
        else:
            return False
            