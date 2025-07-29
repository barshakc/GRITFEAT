"""
1. Two Sum
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)

        for i in range(n):
         for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]

        
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")



        