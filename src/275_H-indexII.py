# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       275_H-indexII.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-10-26 11:52
@version    0.0.1.20181026
--------------------------------------
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher,
    write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have
    at least h citations each, and the other N − h papers have no more than h citations each."

## Example:
Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
             received 0, 1, 3, 5, 6 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.

## Note:
If there are several possible values for h, the maximum one is taken as the h-index.

## Follow up:
This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?
"""

import sys


class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        N = len(citations)
        
        if N == 0: return 0
        
        for idx in range(N):
            if citations[idx] < (N - idx):
                continue
            else:
                return N - idx
        
        return 0


if __name__ == "__main__":
    citation1 = [0, 1, 3, 5, 6]
    citation2 = [0, 0, 4, 4]
    
    sol = Solution()
    res = sol.hIndex(citation2)
    print('Answer is %i' % res)
