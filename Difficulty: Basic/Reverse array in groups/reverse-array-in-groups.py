#User function template for Python

class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, k):
        i=0
        n=len(arr)
        while(i<n):
            low=i
            high=min(i+k-1,n-1)
            ind=high
            while(low<high):
                arr[low],arr[high] = arr[high],arr[low]
                low=low+1
                high=high-1
            i=ind+1
 


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    line_index = 1
    for _ in range(t):
        k = int(data[line_index])
        line_index += 1
        arr = list(map(int, data[line_index].split()))
        line_index += 1
        ob = Solution()
        ob.reverseInGroups(arr, k)
        print(" ".join(map(str, arr)))
        print("~")

# } Driver Code Ends