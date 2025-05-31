#User function Template for python3
#User function Template for python3

class Solution:
    def get_min_max(self, arr):
        arr.sort()
        return arr[0],arr[-1]