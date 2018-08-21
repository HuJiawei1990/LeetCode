# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       132_Palindrome_Partitioning_2.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-04-12 10:37
@version    0.0.1.20180412
--------------------------------------
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
For example, given s = "aab",
    Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

"""

import sys


class Solution:
    def minCut(self, s):
        if self.isPalindrome(s): return 0
        
        cut = [x for x in range(-1, len(s))]
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j]):
                    cut[j + 1] = min(cut[j + 1], cut[i+1] + 1)
        return cut[-1]
    
    
    def isPalindrome(self, s):
        n = len(s)
        if n == 0: return True
        if n == 1: return True
        
        for i in range(int(n / 2) + 1):
            if s[i] != s[n - 1 - i]:
                return False
        return True


if __name__ == "__main__":
    #str1 = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
    str1 = 'bb'
    ans = Solution().minCut(str1)
    
    print("length of string is %d" % len(str1))
    print(ans)
