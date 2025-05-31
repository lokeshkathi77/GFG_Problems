class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        i=0
        j=len(arr)-1
        while i<=j:
            m=int((i+j)>>1)
            if arr[m]==k:
                return True
            elif arr[m]>k:
                j=m-1
            else:
                i=m+1
        return False