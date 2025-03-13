class Solution:
    def binarysearch(self, arr, k):
        mi = 0
        ma = len(arr) - 1
        result = -1  # Stores the first occurrence index
        
        while mi <= ma:
            mid = (mi + ma) // 2  # Correct midpoint calculation
            if arr[mid] == k:
                result = mid  # Update result
                ma = mid - 1  # Move left to find the first occurrence
            elif arr[mid] < k:
                mi = mid + 1  # Search right half
            else:
                ma = mid - 1  # Search left half
                
        return result  # Returns -1 if k is not found

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)
        print("~")

# } Driver Code Ends