"""
Divide two integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part.
Return the quotient after dividing dividend by divisor.
If it is overflow, return 2^31 - 1.
https://leetcode.com/problems/divide-two-integers/
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max_val = 2**31 - 1
        min_val = -2**31

        if dividend == min_val and divisor == -1:
            return max_val

        negative = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            negative = True

        dividend = abs(dividend)
        divisor = abs(divisor)

        count = 0
        while dividend >= divisor:
            dividend = dividend - divisor
            count = count + 1

        if negative:
            count = -count

        return count

if __name__ == "__main__":
    dividend = 10
    divisor = 3
    solution = Solution()
    result = solution.divide(dividend, divisor)
    print(f"The result of dividing {dividend} by {divisor} is: {result}")