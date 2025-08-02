"""
Multiply Strings
This module provides a function to multiply two non-negative integers represented as strings.
The function returns the product as a string.
https://leetcode.com/problems/multiply-strings/

"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        n1 = len(num1)
        n2 = len(num2)
        result = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                sum_ = mul + result[p2]

                result[p2] = sum_ % 10
                result[p1] += sum_ // 10

        start = 0
        while start < len(result) - 1 and result[start] == 0:
            start += 1

        return ''.join(map(str, result[start:]))
    
if __name__ == "__main__":
    num1 = "123"
    num2 = "456"
    solution = Solution()
    result = solution.multiply(num1, num2)
    print(f"The product of {num1} and {num2} is: {result}")