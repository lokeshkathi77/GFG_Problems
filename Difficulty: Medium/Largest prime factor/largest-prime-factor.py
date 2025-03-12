#User function Template for python3
import math
class Solution:
    def largestPrimeFactor(self, n):
        # code here
        ma=0
        while n % 2 == 0:
            ma=max(ma,2)
            n = n // 2
        
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
        for i in range(3,int(math.sqrt(n))+1,2):
            
            # while i divides n , print i and divide n
            while n % i== 0:
                ma=max(ma,i)
                n = n // i
            
    # Condition if n is a prime
    # number greater than 2
        if n > 2:
            return n
            
        return ma
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.largestPrimeFactor(N))
        print("~")

# } Driver Code Ends