# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       699_Falling_Squares.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-20 14:12
@version    0.0.1.20180320
--------------------------------------
699. Falling Squares

On an infinite number line (x-axis), we drop given squares in the order they are given.
The i-th square dropped (positions[i] = (left, side_length)) is a square
    with the left-most point being positions[i][0] and side length positions[i][1].
The square is dropped with the bottom edge parallel to the number line,
    and from a higher height than all currently landed squares.
    We wait for each square to stick before dropping the next.
The squares are infinitely sticky on their bottom edge,
    and will remain fixed to any positive length surface they touch
    (either the number line or another square).
    Squares dropped adjacent to each other will not stick together prematurely.

Return a list ans of heights. Each height ans[i] represents the current highest height of any square we have dropped, after dropping squares represented by positions[0], positions[1], ..., positions[i].
"""
from datetime import datetime
import bisect


class Solution:
    ## 由于square的边长远大于squares的个数, 利用区间存储高度
    @classmethod
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        heights = {}
        ## heights中存储了某个区间内[idx_left, idx_right[内的最大高度
        for pos in positions:
            left, side_length = pos[0], pos[1]
            right = left + side_length
            inter_heights = []
            for (interval_left, interval_right) in heights:
                if interval_right > left and interval_left < right:
                    inter_heights.append(heights[(interval_left, interval_right)])
            
            heights[(left, right)] = max(inter_heights) + side_length if inter_heights != [] else side_length
            
            
            if ans:
                ans.append(max(ans[-1], heights[(left, right)]))
            else:
                ans.append(side_length)
        
        return ans
    
    
    @classmethod
    def fallingSquares1(self, positions):
        """
        Bad Performance. Time out error.
        :param positions:
        :return:
        """
        ans = []
        heights = {}
        for pos in positions:
            left, side_length = pos[0], pos[1]
            max1 = 0
            for x in range(left, left + side_length):
                if x in heights:
                    max1 = heights[x] if max1 < heights[x] else max1
        
            for x in range(left, left + side_length):
                heights[x] = max1 + side_length
        
            if ans:
                ans.append(max(ans[-1], max1 + side_length))
            else:
                ans.append(side_length)
    
        return ans


    @classmethod
    def fallingSquares2(self, positions):
        """
        Best performance.
        :param positions:
        :return:
        """
        height = [0]
        pos = [0]
        res = []
        max_h = 0
        for left, side in positions:
            i = bisect.bisect_right(pos, left)
            j = bisect.bisect_left(pos, left + side)
            high = max(height[i - 1:j] or [0]) + side
            pos[i:j] = [left, left + side]
            height[i:j] = [high, height[j - 1]]
            max_h = max(max_h, high)
            res.append(max_h)
        return res


if __name__ == "__main__":
    #positions = [[1, 2], [2, 3], [6, 1]]
    start_time = datetime.now()
    positions = [[13259169,614936],[633696,602282],[34120526,531664],[909832,846630],[5790720,608795],[50628732,941784]]
    ans = Solution().fallingSquares(positions)
    
    end_time = datetime.now()
    
    print(ans)
    print("It takes %.3f seconds." % ((end_time-start_time).seconds + (end_time-start_time).microseconds / 1e6))
