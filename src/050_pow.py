# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       050_pow.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-07-23 08:56
@version    0.0.1.20190723
--------------------------------------
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:
    输入: 2.00000, 10
    输出: 1024.00000

示例 2:
    输入: 2.10000, 3
    输出: 9.26100

示例 3:
    输入: 2.00000, -2
    输出: 0.25000
    解释: 2-2 = 1/22 = 1/4 = 0.25

说明:
    -100.0 < x < 100.0
    n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
"""


class Solution():
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if (n >= 1) & (n % 2 == 0):
            return self.myPow(x*x, n / 2 )
        elif (n >= 1) & (n % 2 == 1):
            return self.myPow(x*x, (n-1) / 2) * x
        else:
            return 1 / self.myPow(x, -n)


if __name__ == "__main__":
    sol = Solution()
    
    print(sol.myPow(2.10000,3))
    print(sol.myPow(0.00001,2147483647))
    assert sol.myPow(2.10000,3) == 9.26100
