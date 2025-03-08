class Solution:
    def getSecondLargest(self, arr):
        a=set(arr)
        b=list(a)
        b.sort()
        if len(b)==1:
            return -1
        return b[-2]
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends