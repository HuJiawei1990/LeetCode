# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       190_Reverse_bits.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-20 17:29
@version    0.0.1.20180320
--------------------------------------
190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
    return 964176192 (represented in binary as 00111001011110000010100101000000).
"""

import sys


class Solution:
    @classmethod
    def reverseBits(self, n):
        """
        Reverse bits of a given 32 bits unsigned integer.
        general performance.
        :param n: int
        :return: int
        """
        n_bin_reverse = 0
        n_binary = bin(n)[2:]
        
        if len(n_binary) > 32:
            return -1
        n_binary = '0' * (32 - len(n_binary)) + n_binary
        
        for i in range(32):
            n_bin_reverse += int(n_binary[i]) * 2 ** i
        
        return n_bin_reverse


if __name__ == "__main__":
    print(Solution().reverseBits(43261596 ))
