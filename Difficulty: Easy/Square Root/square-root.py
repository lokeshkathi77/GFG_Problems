class Solution:
    def floorSqrt(self, n):
        
        #Your code here
        if n in (0,1):
            return n
        low  = 1
        high = n
        while low < high :

            mid = (low + high)//2

            if (mid*mid) <= n:
                ans = mid
                low = mid + 1
            else:
                high = mid
            
        return ans