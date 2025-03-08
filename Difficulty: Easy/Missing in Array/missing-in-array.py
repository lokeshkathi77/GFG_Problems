class Solution:
    def missingNumber(self, arr):
        s=set(arr)
        for i in range(1,len(arr)+2):
            if i not in s:
                return i
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends