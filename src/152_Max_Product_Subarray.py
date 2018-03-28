# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       152_Max_Product_Subarray.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-27 18:07
@version    0.0.1.20180327
--------------------------------------
152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, n * big, n * small), min(n, n * big, n * small)
            maximum = max(maximum, big)
        return maximum


if __name__ == "__main__":
    print(Solution().maxProduct([1, 2, 3]))
