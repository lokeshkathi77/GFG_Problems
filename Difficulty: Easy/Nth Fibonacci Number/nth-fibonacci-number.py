
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n==0:
            return "0"
        elif n==1:
            return "1"
        else:
            n0=0
            n1=1
            for i in range(1,n):
                fib=n0+n1
                n0=n1
                n1=fib
            return fib
