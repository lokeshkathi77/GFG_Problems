class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        if n:
            return int(n*(n+1)/2)
        else:
            return 0