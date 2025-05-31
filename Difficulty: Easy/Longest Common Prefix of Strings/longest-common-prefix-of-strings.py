#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        arr.sort()
        a = arr[0]
        b = arr[-1]
        l = min(len(a), len(b))
        res = ""
        for i in range(l):
            if a[i] != b[i]:
                return res
            res += a[i]
        return res