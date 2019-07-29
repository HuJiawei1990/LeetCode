# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       295_mdeian.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-07-23 09:24
@version    0.0.1.20190723
--------------------------------------
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
    void addNum(int num) - 从数据流中添加一个整数到数据结构中。
    double findMedian() - 返回目前所有元素的中位数。

示例：
    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3)
    findMedian() -> 2

进阶:
    如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
    如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
"""


class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.numbers = []
        self.length = 0
        self.median = None
    
    
    def addNum(self, num: int) -> None:
        if self.length == 0:
            self.numbers.append(num)
        else:
            for idx, n in enumerate(self.numbers):
                if n >= num:
                    l1, l2 = self.numbers[0:idx], self.numbers[idx:]
                    self.numbers = l1 + [num] + l2
                    break
                elif idx == self.length - 1:
                    self.numbers += [num]
                    break
        self.length += 1
        
    
    
    def findMedian(self) -> float:
        print(self.numbers)
        if self.length > 0:
            if self.length % 2 == 0:
                self.median = (self.numbers[int(self.length/2)] + self.numbers[int(self.length/2)-1])/2
            else:
                self.median = (self.numbers[int((self.length-1) / 2)])
        return self.median

if __name__ == "__main__":
    # Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    obj.addNum(3)
    obj.addNum(4)
    param_2 = obj.findMedian()
    
    print(param_2)
