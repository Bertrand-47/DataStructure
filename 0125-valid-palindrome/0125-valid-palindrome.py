class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == " ":
            return True
        
        s = s.lower()
        cleaned_string = ''.join(ch for ch in s if ch.isalnum())
        
        reversed_string = cleaned_string[::-1]
        
        if cleaned_string == reversed_string:
            return True
        return False