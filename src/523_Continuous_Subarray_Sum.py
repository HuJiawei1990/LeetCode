# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       523_Continuous_Subarray_Sum.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-04-25 11:45
@version    0.0.1.20180425
--------------------------------------
Given a list of non-negative numbers and a target integer k, write a function to check
    if the array has a continuous subarray of size at least 2 that sums up to the multiple of k,
    that is, sums up to n*k where n is also an integer.
"""

from collections import Counter


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        k = abs(k)
        
        if len(nums) == 1: return False
        if len(nums) > 2*k: return True
        if k == 0: return True if (0,0) in [(nums[i], nums[i+1]) for i in range(len(nums)-1)] else False

        sums = [0]
        for idx, num in  enumerate(nums):
            sums.append((sums[-1]+num) % k)
        
        pos_dict = {}   # restore {value: position}
        for pos, r1 in enumerate(sums):
            if r1 not in pos_dict:
                pos_dict[r1] = pos
            elif pos - pos_dict[r1] > 1:
                return True
        
        return False
        
        
if __name__ == "__main__":
    list1 = [23, 2, 4, 6, 7]
    print(Solution().checkSubarraySum(list1, 6))
