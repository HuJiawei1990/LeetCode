# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       738_Monotone_Increasing_Digits.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-02-25 16:41
@version    0.0.1.20190225
--------------------------------------
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.
(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
    Input: N = 10
    Output: 9
Example 2:
    Input: N = 1234
    Output: 1234
Example 3:
    Input: N = 332
    Output: 299
Note: N is an integer in the range [0, 10^9].
"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # if self.isMonotone(N): return N
        
        N_list = self.int2list(N)
        
        # find the first non-monotone list
        digit_last = 0
        is_monotone = 1
        index_strict_monotone = 0
        for index, digit in enumerate(N_list):
            if digit < digit_last:
                is_monotone = 0
                break
            elif digit > digit_last:
                # strictly monotone, refresh index_strict_monotone
                index_strict_monotone = index
            
            digit_last = digit
        
        # if N is monotone, return answer
        if is_monotone: return N
        
        for index, _ in enumerate(N_list):
            if index == index_strict_monotone: N_list[index] -= 1
            if index > index_strict_monotone:
                N_list[index] = 9
        
        #print(N, ':', N_list)
        
        return self.list2int(N_list)
    
    
    def isMonotone(self, N: int) -> bool:
        N_str = str(N)
        digit_last = 0
        for digit in N_str:
            if int(digit) < int(digit_last):
                return False
            else:
                digit_last = digit
        return True
    
    
    def int2list(self, N: int) -> list:
        if N < 0: raise ValueError("Unsupported negative number.")
        N_str = str(N)
        N_list = []
        for digit in N_str:
            N_list.append(int(digit))
        
        return N_list
    
    
    def list2int(self, N_list) -> int:
        l = len(N_list)
        N = 0
        for index, digit in enumerate(N_list):
            N += digit * (10 ** (l - index - 1))
        return N


if __name__ == "__main__":
    sol = Solution()
    assert sol.isMonotone(1234) == True
    assert sol.isMonotone(11222) == True
    assert sol.isMonotone(1113342) == False
    
    assert sol.monotoneIncreasingDigits(332) == 299
    assert sol.monotoneIncreasingDigits(1111110) == 999999
