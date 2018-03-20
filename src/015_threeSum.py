# -*- coding:utf-8 -*-
"""
@file       015_threeSum.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-20 13:28
@version    0.0.1.20180320
--------------------------------------
15. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
"""


class Solution:
    def find_n_sum(self, sorted_nums, target, n: int, result_prefix: list, results: list):
        """
        Find an n-element tuple in a sorted list, whose sum equals to target.
        :param sorted_nums: a SORTED list of numbers(integers/floats)
        :param target:      the target sum of tuple
        :param n:           number of elements wanted in tuple
        :param result_prefix:  add prefix elements in results (when n > 2, we need to add the smallest elements into results)
        :param results:     list of lists
                        all satisfied n-element tuples will be added into list
        :return:    return status:
                        0:  successful status
                        -1: WARNING: n (number of elements in tuple) is bigger than length of list
                        -2: WARNING: target sum is too small/large, failed to find the target
        NOTE:
            1.parameter sorted_nums MUST be sorted;
            2.all tuples find will be APPENDED into list results.
        """
        nums_len = len(sorted_nums)
        if n > nums_len:
            return -1
        
        ## as sorted_nums is a sorted list, we can simplify some special conditions
        if (target < sorted_nums[0] * n) or (target > sorted_nums[-1] * n):
            return -2
        
        if n == 1:
            ## initial condition n = 1
            for num in sorted_nums:
                if num == target:
                    results.append([num])
                    return 0
            return -2
        elif n == 2:
            ## initial condition n = 2
            ## find 2 elements in list whose sum == target
            ## find these 2 elements from two sides of the list
            ##      sorted_nums[idx_l] is the smaller element
            ##      sorted_nums[idx_r] is the bigger element
            idx_l, idx_r = 0, nums_len - 1
            while idx_l < idx_r:
                element_sum = sorted_nums[idx_l] + sorted_nums[idx_r]
                if element_sum < target:
                    ## when the sum is too small, try to increase the smaller element
                    idx_l += 1
                elif element_sum > target:
                    ## when the sum is too large, try to reduce the bigger element
                    idx_r -= 1
                else:
                    ## a 2-element tuple is found
                    ## add this solution into results list
                    aux = result_prefix + [sorted_nums[idx_l], sorted_nums[idx_r]]
                    results.append(aux)
                    
                    idx_l += 1
                    idx_r -= 1
                    
                    ## to pass duplicate elements in list
                    while (idx_l < idx_r) & (sorted_nums[idx_l] == sorted_nums[idx_l - 1]):
                        idx_l += 1
                    while (idx_l < idx_r) & (sorted_nums[idx_r] == sorted_nums[idx_r + 1]):
                        idx_r -= 1
            return 0
        else:
            ## Try the SMALLEST element sorted_nums[i] in the n-tuple
            ##  and find the other (n-1)-tuple in remaining list sorted_nums[i+1:]
            for i in range(0, len(sorted_nums) - n + 1):
                if sorted_nums[i] * n > target:
                    break
                elif (i > 0) & (sorted_nums[i] == sorted_nums[i - 1]):
                    pass
                else:
                    self.find_n_sum(sorted_nums[i + 1:],
                                    target - sorted_nums[i],
                                    n - 1,
                                    result_prefix + [sorted_nums[i]],
                                    results)
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results_3 = []
        self.find_n_sum(sorted(nums), target=0,  n=3, result_prefix=[], results=results_3)
        
        return results_3


if __name__ == "__main__":
    S = [-1, 0, 1, 2, -1, -4]
    result = Solution().threeSum(S)
    print(result)