class Solution:
    def getPairs(self, arr):
        ret=set()
        arr.sort()
        lth=len(arr)
        right=lth-1
        for left in range(lth):
            if left>=right:
                break
            while arr[right]>-arr[left]:
                right-=1
            if left<right and arr[right]+arr[left]==0:
                ret.add((arr[left],arr[right],))
        return sorted(ret)


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.getPairs(arr)
        if len(res) == 0:
            print()
        else:
            IntMatrix().Print(res)
        print("~")
# } Driver Code Ends