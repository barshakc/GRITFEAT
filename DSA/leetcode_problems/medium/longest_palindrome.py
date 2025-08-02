"""
Longest Palindrome Substring
Given a string s, return the longest palindromic substring in s.
https://leetcode.com/problems/longest-palindromic-substring/
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_palindrome(sub):
            return sub == sub[::-1]

        longest = ""
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                if is_palindrome(sub) and len(sub) > len(longest):
                    longest = sub

        return longest
    
if __name__ == "__main__":
    s = "babad"
    solution = Solution()
    result = solution.longestPalindrome(s)
    print(f"The longest palindromic substring in '{s}' is: {result}")