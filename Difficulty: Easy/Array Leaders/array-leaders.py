class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders_list = []
        max_from_right = arr[-1]  # Rightmost element is always a leader
        leaders_list.append(max_from_right)

        # Traverse from second-last element to the leftmost
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                leaders_list.append(arr[i])

        # Reverse to maintain order
        return leaders_list[::-1]
#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends