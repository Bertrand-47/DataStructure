class Solution(object):
    def reverseWords(self, s):
        spaces = 0
        numlist = []
        if s == "":
            return ""
        if s ==" ":
            return " "
        s = s.lstrip()
        s = s.rstrip()
    
        for i in range(len(s)):
            if s[i]==" ":
                spaces+=1
                numlist.append(i)
        if spaces == 0:
            return s
        
        length_list =len(s) 
        crap_list = []
        for number in range(len(numlist)):
            if number == 0:
                first  = list(range(0,numlist[0]))
                crap_list.append(first)
            else:
                if number < length_list -1:
                    Starting_point = numlist[number-1] + 1
                    Stopping_point = numlist[number]
                    other = list(range(Starting_point,Stopping_point))
                    crap_list.append(other)
            if number ==len(numlist)-1 and numlist[-1] < length_list:
                other = list(range(numlist[-1]+1,length_list))
                crap_list.append(other)
                
        reversed_order = crap_list[::-1]
        reversed_s = ""
        sublist = len(reversed_order)
        a = 0
        for lists in reversed_order:
            for number in lists:
                reversed_s+=s[number]
            reversed_s+= " "
        return " ".join(reversed_s.split())
        