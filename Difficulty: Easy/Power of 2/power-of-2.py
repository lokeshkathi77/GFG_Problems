class Solution:
    # Function to check if given number n is a power of two.
    import math
    def isPowerofTwo(self, n):
        return math.log2(n).is_integer()