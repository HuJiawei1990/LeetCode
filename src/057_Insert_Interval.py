# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       057_Insert_Interval.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-22 16:09
@version    0.0.1.20180322
--------------------------------------
57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""

import sys
from _utils import Interval


class Solution:
    def insert(self, intervals, new_interval: Interval):
        """
        intervals were initially sorted according to their start times.
        :param intervals:
        :param new_interval:
        :return:
        """
        if intervals == []: return [new_interval]
        
        new_start = new_interval.start
        new_end = new_interval.end
        l1 = []
        l_intersection = []
        idx2 = 0
        
        for idx, interval in enumerate(intervals):
            idx2 = idx
            if interval.end < new_interval.start:
                l1.append(interval)
                continue
            if interval.start > new_end:
                idx2 = idx - 1
                break
            l_intersection.append(interval)
        
        idx2 += 1
        l2 = intervals[idx2:]
        
        new_interval2 = Interval(s=min(l_intersection[0].start, new_start),
                                 e=max(l_intersection[-1].end, new_end)) if l_intersection != [] else new_interval
        
        return l1 + [new_interval2] + l2


def test1(list1, new):
    intervals_list = list1
    intervals = [Interval(i[0], i[1]) for i in intervals_list]
    new_interval = Interval(new[0], new[1])
    
    ans = Solution().insert(intervals, new_interval)
    
    for interval in ans:
        print("[%i, %i]" % (interval.start, interval.end))


if __name__ == "__main__":
    #test1([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], (4, 9))
    test1([[1,3],[6,9]], (2,5))