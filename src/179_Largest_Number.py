# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       179_Largest_Number.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-04-16 14:23
@version    0.0.1.20180416
--------------------------------------
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.
For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

"""

import sys


class Solution:
    def largestNumber(self, nums):
        ans = self.largestNumber2(nums)
        return "0" if ans[0] == "0" else ans
        
    
    def largestNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        ans = ""
        if nums == []: return ""
        if len(nums) == 1: return str(nums[0])
        
        l1,l2 = [], []
        element_0 = str(nums[0])
        for num in nums[1:]:
            if self.bigger_new(element_0, str(num)):
                l2.append(num)
            else:
                l1.append(num)
        
        return self.largestNumber2(l1) + element_0 + self.largestNumber2(l2)
        
    
    ## define a new order
    def bigger_new(self, x1, x2):
        if x1 == x2: return True
        
        min_len = min(len(x1), len(x2))
        for i in range(min_len):
            if x1[i] != x2[i]:
                return x1[i] > x2[i]
        
        if len(x1) > min_len:
            return self.bigger_new(x1[min_len:], x2)
        else:
            return self.bigger_new(x1, x2[min_len:])
            


if __name__ == "__main__":
    ans = Solution().largestNumber([3, 30, 34, 5, 9])
    print(ans)
    print(Solution().bigger_new("33", "333333"))
