# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       352_Data_Stream_Disjoint_Intervals.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-04-16 17:04
@version    0.0.1.20180416
--------------------------------------
352. Data Stream as Disjoint Intervals

Given a data stream input of non-negative integers a1, a2, ..., an, ...,
summarize the numbers seen so far as a list of disjoint intervals.
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
        
class SummaryRanges:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.content = []
        self.intervals = []
        self.last = None
        self._interval_list = []
    
    
    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        self.content.append(val)
        self.last = val
        
        self._interval_list = self.insertIntoIntervals(val, self._interval_list)
        
    
    
    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        nums = len(self._interval_list)
        ans = []
        for i in range(int(nums/2)):
            ans.append(Interval(self._interval_list[i*2], self._interval_list[2*i+1]))
        
    def insertIntoIntervals(self, val, list1):
        if not list1:
            return [val, val]
        
        if val in list1: return list1
        
        left = 0
        
        while left < len(list1):
            if self._interval_list[left] < val:
                left += 1
            else:
                break
        
        if left % 2 == 1: return list1
        
        l1 = self._interval_list[0:left]
        l2 = self._interval_list[left:]
        
        if l1 == []:
            return [val] + l2[1:] if val == l2[0] -1 else [val,val] + l2
        
        if l2 == []:
            return l1[0:-1] + [val] if val == l1[-1]+1 else l1 + [val,val]
        
        if (l1[-1] + 1 == val) & (l2[0] - 1 == val):
            return l1[0:-1] + l2[1:]
        return l1[0:-1] + [val] + l2 if l1[-1] + 1 == val else l1 + [val] + l2[1:]
        
            

# Your SummaryRanges object will be instantiated and called as such:
def run():
    obj = SummaryRanges()
    obj.addNum(0)
    param_2 = obj.getIntervals()


if __name__ == "__main__":
    run()
