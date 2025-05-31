class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        return "".join(sorted(list(s1))) == "".join(sorted(list(s2)))