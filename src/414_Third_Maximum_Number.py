# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       414_Third_Maximum_Number.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-22 11:07
@version    0.0.1.20180322
--------------------------------------
414. Third Maximum Number

Given a non-empty array of integers, return the third maximum number in this array.
    If it does not exist, return the maximum number.
    The time complexity must be in O(n).
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.nthMax(nums, 3)
    
    
    def nthMax(self, nums: list, n):
        if nums is None or nums == []: print("Error: Empty list get.")
        N = len(set(nums))
        #nums = list(set(nums))
        if N < n: return max(nums)
        if N == n: return min(nums)
        if n == 1: return max(nums)
        
        aux = []
        for number in nums:
            if len(aux) < n:
                aux.append(number)
            else:
                if (number not in aux) and (min(aux) < number):
                    aux.remove(min(aux))
                    aux.append(number)
                    
        return min(aux)


    def thirdMax2(self, nums):
        """
        more pythonic
        :param nums:
        :return:
        """
        ## remove duplicate elements
        nums = list(set(nums))
        n = 3
        
        if len(nums) < n: return max(nums)
        for i in range(n-1): nums.remove(max(nums))
        return max(nums)


if __name__ == "__main__":
    print(Solution().thirdMax(list(range(3, 20))))
    print(Solution().thirdMax([1, 2]))
    print(Solution().thirdMax([5, 2, 4, 1, 3, 6, 0]))
