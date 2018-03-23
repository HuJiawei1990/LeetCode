# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       013_Roman_to_Integer.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-23 10:16
@version    0.0.1.20180323
--------------------------------------
13. Roman to Integer

Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""
ROMANS = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        prev_val = 0
        ## counting from right to left
        for i in range(len(s)-1,-1,-1):
            ans = ans + ROMANS[s[i]] if prev_val >= ROMANS[s[i]] else ans - ROMANS[s[i]]
            prev_val = ROMANS[s[i]]
        
        return ans
        

