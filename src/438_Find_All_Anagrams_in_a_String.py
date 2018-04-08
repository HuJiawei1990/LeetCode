# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       438_Find_All_Anagrams_in_a_String.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-04-08 16:50
@version    0.0.1.20180408
--------------------------------------
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings
    s and p will not be larger than 20,100.
The order of output does not matter.
"""

from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_len = len(p)
        p_counter = Counter(p)
        last_counter = Counter(s[0:p_len])
        
        ans = [0] if last_counter == p_counter else []
        
        pos = 0
        while pos < len(s)-p_len:
            char1 = s[pos]
            char2 = s[p_len+pos]
            
            last_counter[char2] += 1
            if last_counter[char1] > 1: last_counter[char1] -= 1
            else: del last_counter[char1]
            
            if last_counter == p_counter:
                ans.append(pos+1)
            if char2 not in p:
                pos += p_len
                last_counter = Counter(s[pos:pos+p_len])
            else: pos += 1
        
        return ans


if __name__ == "__main__":
    ans = Solution().findAnagrams("acdcaeccde", "c")
    print(ans)
