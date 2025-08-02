"""
Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^
31, 2^31 - 1], then return 0.
https://leetcode.com/problems/reverse-integer/
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10

        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
        
if __name__ == "__main__":
    x = 123
    solution = Solution()
    result = solution.reverse(x)
    print(f"The reverse of {x} is: {result}")
    