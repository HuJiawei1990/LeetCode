# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       645._Set_Mismatch.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-06-02 14:17
@version    0.0.1.20190602
--------------------------------------
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers
    in the set got duplicated to another number in the set, which results in repetition of one number
    and loss of another number.
Given an array nums representing the data status of this set after the error. Your task is to firstly find the number
    occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""

import sys


class Solution:
    def findErrorNums(self, nums: list) -> list:
        error = 0
        nums_freq = {}
        
        sum_exp = 0
        sum_real = 0
        for i, n in enumerate(nums):
            sum_real += n
            sum_exp += (i + 1)
            
            if n in nums_freq.keys():
                error = n
            else:
                nums_freq[n] = 1
        
        missing = error + sum_exp - sum_real
        
        # print(error, missing)
        return [error, missing]


if __name__ == "__main__":
    sol = Solution()
    
    assert sol.findErrorNums(nums=[1, 2, 2, 4]) == [2, 3]
