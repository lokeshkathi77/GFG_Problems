class Solution:
    def primeDivision(self, n):
        # Step 1: Generate all prime numbers up to n using Sieve of Eratosthenes
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        
        # Step 2: Find two prime numbers that sum up to n
        for i in range(2, n):
            if primes[i] and primes[n - i]:  # Check if both numbers are prime
                return [i, n - i]  # Return the first valid pair (smallest lexicographically)
        
        return None  # If no valid pair is found

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1, end=" ")
        print(p2)

        print("~")
# } Driver Code Ends