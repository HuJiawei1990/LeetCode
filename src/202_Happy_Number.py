# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       202_Happy_Number.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-28 11:41
@version    0.0.1.20180328
--------------------------------------
202. 快乐数

写一个算法来判断一个数是不是“快乐数”。
一个数是不是快乐是这么定义的：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
    然后重复这个过程直到这个数变为 1，或是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
"""

import sys


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        iter = 0
        ans_list = [n]
        while True:
            iter += 1
            aux = self.square_sum(ans_list[-1])
            if ans_list[-1] == aux: break
            elif aux in ans_list:
                ## If a number already appears before, it means we meet into a limitless iteration.
                return False
            else:
                ans_list.append(aux)
        return ans_list[-1] == 1
        
        
    def square_sum(self, n):
        n_str = str(n)
        ans = 0
        for char in n_str:
            ans += int(char) ** 2
        
        return ans


if __name__ == "__main__":
    Solution().isHappy(18)
