#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        d={}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        m=max(arr)
        mi=float('inf')
        for i in range(1,m):
            if i not in d:
                mi = i
        if mi == float('inf'):
            mi = m+1
        return [max(d, key=d.get),mi]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends