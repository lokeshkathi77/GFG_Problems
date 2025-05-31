class Solution:
    def countFreq(self, arr, target):
        #code here
        a=arr.count(target)
        return a
        for i in rang(0,len(arr)):
            if arr[i]!=target:
                return 0