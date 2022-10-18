class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        for i in range(len(s)):
            if t[i] in mapping.values() and mapping.get(s[i])== None:
                return False
            if mapping.get(s[i])!= None:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                mapping[s[i]] = t[i]
        return True