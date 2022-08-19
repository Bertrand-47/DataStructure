class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        characterFreq = {}
        
        for character in s:
            characterFreq[character]= characterFreq.get(character, 0) + 1
        
        for i in range(len(s)):
            character = s[i]
            if characterFreq[character] == 1:
                return i
        return -1
        