# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       227_Basic_Calculator_II.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-06-04 18:03
@version    0.0.1.20190604
--------------------------------------
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
    The integer division should truncate toward zero.

Example 1:
    Input: "3+2*2"
    Output: 7
Example 2:
    Input: " 3/2 "
    Output: 1
Example 3:
    Input: " 3+5 / 2 "
    Output: 5

Note:
    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.
"""


class Solution():
    def calculate(self, s: str) -> int:
        # remove all espace
        s = s.replace(' ', '')
        
        num_start = 0
        s_list = []
        
        for i, digit in enumerate(s):
            if (digit in ['+', '-', '*', '/']) or (i == len(s) - 1):
                last_num, operator = (s[num_start:i + 1], []) if i == len(s) - 1 else (s[num_start:i], [digit])
                
                if s_list == []:
                    s_list.append(last_num)
                elif s_list[-1] == '*':
                    aux = int(s_list[-2]) * int(last_num)
                    s_list = s_list[0:-2] + [str(aux)]
                elif s_list[-1] == '/':
                    aux = int(int(s_list[-2]) / int(last_num))
                    s_list = s_list[0:-2] + [str(aux)]
                else:
                    s_list.append(last_num)
                
                num_start = i + 1
                s_list += operator
            
            # print('step', i, ':', digit, s_list)
        
        return self.calculateSimple(s_list)
    
    
    def calculateSimple(self, s_list):
        if not s_list: return 0
        if len(s_list) == 1: return int(s_list[0])
        
        aux = self.calculateSimple(s_list[0:-2])
        if s_list[-2] == '+':
            return aux + int(s_list[-1])
        elif s_list[-2] == '-':
            return aux - int(s_list[-1])
        else:
            raise ValueError("Invalid input list..")
    
    
    def calculate2(self, s: str):
        print(s)
        
        s = s.replace(' ', '') + '+'
        num = 0
        last = 0
        sign = '+'
        aux = 0
        for i, digit in enumerate(s):
            if digit.isnumeric():
                num = num * 10 + int(digit)
                continue
            
            if sign == '+':
                aux += last
                last = num
            elif sign == '-':
                aux += last
                last = -num
            elif sign == '*':
                last = last * num
            elif sign == '/':
                last = int(last / num)
            
            print('Step %i: last = %i, num = %i, aux = %i' % (i, last, num, aux))
            
            num = 0
            sign = digit
        
        return aux + last


if __name__ == "__main__":
    sol = Solution()
    
    assert sol.calculate2("1-1") == 0
    assert sol.calculate2(" 3+5 / 2 *2*7/4") == 10
    
    # sol.calculate2("2*3+4")
