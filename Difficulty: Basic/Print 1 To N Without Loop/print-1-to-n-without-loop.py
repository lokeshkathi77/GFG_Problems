class Solution:
    def solve(self, n):
        if n == 0:
            return
        self.solve(n-1)
        print(n,end=" ")
    def printNos(self,n):
        self.solve(n)