class Solution:
    def evenlyDivides(self, n):
        # code here
      c=0
      n1=n
      while n>0:
        n2=n%10
        n=n//10
        if n2!=0 and n1%n2 ==0:
            c+=1
      return c