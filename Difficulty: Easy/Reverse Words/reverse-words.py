class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        for i in range(len(s)):
           if s[i].isalpha():
                f=i
                break
        for j in range(len(s)-1,-1,-1):
            if s[j].isalpha():
                r=j
                break
        x=s[f:r+1]
        m=x.split()
        k=""
        for i in range(len(m)-1,-1,-1):
             k=k+m[i]+" "
        z=k[0:len(k)-1]
        return z