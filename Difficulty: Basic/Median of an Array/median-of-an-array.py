class Solution:
    def findMedian(self, arr):
        #code here.
        arr.sort()
        n=len(arr)
        if len(arr)%2==0:
            return (arr[n//2]+arr[(n//2)-1])/2
        else:
            return arr[n//2]