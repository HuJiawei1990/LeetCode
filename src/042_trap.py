# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       042_trap.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-07-16 16:35
@version    0.0.1.20190716
--------------------------------------
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例:
    输入: [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6
"""


class Solution():
    def trap(self, height: list) -> int:
        n = len(height)
        if n <= 2: return 0
        max_l = height[0]
        max_r = height[n - 1]
        
        left_max = {i: max_l for i in range(n)}
        right_max = {i: max_r for i in range(n)}
        
        for i in range(n):
            left_max[i] = max_l
            right_max[n - 1 - i] = max_r
            
            if height[i] > max_l:
                max_l = height[i]
                for j in range(max(i,n - 1 - i), n):
                    left_max[j] = max_l
            
            if height[n - 1 - i] > max_r:
                max_r = height[n - 1 - i]
                for j in range(min(i, n-1-i)):
                    right_max[j] = max_r
        
        aux = 0
        for i in range(n):
            # print(i, height[i], left_max[i], right_max[i])
            depth = min(left_max[i], right_max[i])
            aux += max(0, (depth - height[i]))
        
        return aux


if __name__ == "__main__":
    sol = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print("solution:", sol.trap(height))
    # assert sol.trap(height) == 6
