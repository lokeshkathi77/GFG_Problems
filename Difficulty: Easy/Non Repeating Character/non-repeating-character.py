class Solution:
    def nonRepeatingChar(self,s):
        a=[0]*26
        for i in s:
            a[ord(i)-97]+=1
        for i in s:
            if a[ord(i)-97]==1:
                return i
        return "$"