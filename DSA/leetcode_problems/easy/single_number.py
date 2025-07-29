"""
Single Number
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.
https://leetcode.com/problems/single-number/
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single_num = 0 
        for num in nums:
            single_num ^= num 
         
        return single_num
    
if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    solution = Solution()
    result = solution.singleNumber(nums)
    print(f"The single number in the array {nums} is: {result}")