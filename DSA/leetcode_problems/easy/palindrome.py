"""
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
https://leetcode.com/problems/palindrome-number/
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        if s==s[::-1]:
            return True
        else:
            return False

        
if __name__ == "__main__":
    x = 121
    solution = Solution()
    result = solution.isPalindrome(x)
    print(f"Is {x} a palindrome? {result}")