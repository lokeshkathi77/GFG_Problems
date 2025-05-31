#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        fib_sequence = []
    
        # Handle special cases for n
        if n <= 0:
            return fib_sequence
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
    
        # Start with the first two Fibonacci numbers
        fib_sequence = [0, 1]
    
        # Generate Fibonacci numbers up to n
        for i in range(2, n):
            next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_fib)
    
        return fib_sequence

