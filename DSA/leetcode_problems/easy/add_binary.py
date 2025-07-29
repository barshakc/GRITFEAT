"""
Add Binary
Given two binary strings a and b, return their sum as a binary string.
https://leetcode.com/problems/add-binary/
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a1= int(a,2)
        b1= int(b,2)

        sum=a1+b1
        sum=bin(sum)[2:]
        return sum
        
if __name__ == "__main__":
    a = "1010"
    b = "1101"
    solution = Solution()
    result = solution.addBinary(a, b)
    print(f"The sum of binary strings '{a}' and '{b}' is: {result}")