# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       446_Arithmetic_Slices_2-Subsequence.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-02-20 14:30
@version    0.0.1.20190220
--------------------------------------
A sequence of numbers is called arithmetic if it consists of at least three elements
    and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.
1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array
    is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0 < P1 < ... < Pk < N.
A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic
    if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k ≥ 2.
The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -2^31 and 2^31-1 and 0 ≤ N ≤ 1000.
    The output is guaranteed to be less than 2^31-1.

Example:
Input: [2, 4, 6, 8, 10]
Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
"""

import sys
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        
        :param A:List[int]
        :return:int
        """
        pre = defaultdict(int)
        post = defaultdict(int)
        pos = defaultdict(list)
        seq = [defaultdict(int) for _ in range(len(A))]
    
        for i, a in enumerate(A):
            post[a] += 1
            pos[a].append(i)
    
        for i, a in enumerate(A):
            post[a] -= 1
            for b in pre:
                c = (a << 1) - b
                if c in post and post[c] > 0:
                    n = pre[b]
                    if b in seq[i]:
                        n += seq[i][b]
                    for j in pos[c]:
                        if j > i:
                            seq[j][a] += n
            pre[a] += 1
    
        return sum([sum(p.values()) for p in seq])
        
        


if __name__ == "__main__":
    pass
