class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        n = len(arr)
        for i in range(n):
            
            for j in range(0, n-i-1):
                if (arr[j] > arr[j+1]):
                    arr[j],arr[j+1] = arr[j+1], arr[j]