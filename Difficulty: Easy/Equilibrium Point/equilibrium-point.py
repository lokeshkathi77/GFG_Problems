# User function Template for python3
class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        lowersum = 0
        totalsum = sum(arr)
        # if lowersum = highersum then
        # totalsum = 2lowersum + a[i]
        for i in range(1,len(arr)-1):
            lowersum = lowersum + arr[i-1]
            if totalsum == (2*lowersum + arr[i]):
                return i
        return -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends