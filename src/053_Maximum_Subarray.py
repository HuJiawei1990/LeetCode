# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       53_Maximum_Subarray.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-06-03 10:17
@version    0.0.1.20190603
--------------------------------------
Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.

Example:
    Input:          [-2,1,-3,4,-1,2,1,-5,4],
    Output:         6
    Explanation:    [4,-1,2,1] has the largest sum = 6.

Follow up:
    If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

import sys


class Solution:
    def maxSubArray2(self, nums: list) -> int:
        if len(nums) ==1: return nums[0]
        
        return max(self.maxSubArray(nums[1:]), self.maxSubArrayIndex(0,nums))
    
    
    def maxSubArray(self, nums: list) -> int:
        cur, res = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur = nums[i] if cur <= 0 else cur + nums[i]
            res = max(cur, res)
        return res
    
    
    def maxSubArrayIndex(self, i: int, nums: list) -> int:
        """
        
        :param i:
        :param nums:
        :return:
        """
        max_sum = 0
        last_sum = 0
        for j in range(i, len(nums)):
            if j ==i:
                max_sum = nums[i]
                last_sum = nums[i]
            else:
                last_sum += nums[j]
            
            if max_sum < last_sum: max_sum = last_sum
        return max_sum
                
                


if __name__ == "__main__":
    sol = Solution()
    
    assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
