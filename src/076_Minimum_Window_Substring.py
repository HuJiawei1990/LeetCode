# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       076_Minimum_Window_Substring.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-26 13:37
@version    0.0.1.20180326
--------------------------------------
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S
    which will contain all the characters in T in complexity O(n).
For example,
    S = "ADOBECODEBANC"
    T = "ABC"
    Minimum window is "BANC".

Note:
    If there is no such window in S that covers all characters in T, return the empty string "".
    If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

import sys
import collections


class Solution(object):
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
    
    
    def minWindow1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s): return ""
        
        for char in t:
            if char not in s:
                return ""
        
        positions_list = {char: [] for char in t}
        for idx, char in enumerate(s):
            if char in t:
                positions_list[char].append(idx)
        
        intervals_list = self.window_list(list(positions_list.values()))
        
        ## Assume every character in t is unique
        min_length = len(s)
        min_start = 0
        for (start, length) in intervals_list:
            if length < min_length:
                min_length = length
                min_start = start
        
        return s[min_start:min_start + min_length]
    
    
    def window_list(self, positions: list):
        
        if len(positions) == 1:
            return [(value, 1) for value in positions[0]]
        
        ans_prev = self.window_list(positions[1:])
        ans = []
        for interval in ans_prev:
            left = interval[0]
            right = interval[0] + interval[1]
            
            position_prev = -1
            for position in positions[0]:
                if position < left:
                    position_prev = position
                    continue
                elif position < right:
                    ans.append(interval)
                    break
                else:
                    ans.append((left, position - left + 1))
                    if position_prev > -1:
                        ans.append((position_prev, right - position_prev))
            
            if position < left:
                ans.append((position, right - position))
        
        return ans


if __name__ == "__main__":
    s = "adobecodebancbbcaa"
    T = "abc"
    
    ans = Solution().minWindow(s, T)
    print(ans)
