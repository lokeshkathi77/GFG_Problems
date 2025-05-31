class Solution:
    def isPalindrome(self, s: str) -> bool:
		# code here
		if s == s[::-1]:
            return True
        else:
            return False