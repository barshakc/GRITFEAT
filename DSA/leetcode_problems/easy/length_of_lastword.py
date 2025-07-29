"""
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/
Given a string s consisting of words and spaces, return the length of the last word in the string.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst= s.split()
        last_word=lst[-1]
        return len(last_word)
    
if __name__ == "__main__":
    s = "Hello World"
    solution = Solution()
    result = solution.lengthOfLastWord(s)
    print(f"The length of the last word in '{s}' is: {result}")