# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       463_Island_Perimeter.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-04-08 16:36
@version    0.0.1.20180408
--------------------------------------
463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land
    and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally).
    The grid is completely surrounded by water, and there is exactly one island (
    i.e., one or more connected land cells). The island doesn't have "lakes"
    (water inside that isn't connected to the water around the island).
    One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
    Determine the perimeter of the island.
"""

import sys


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        ans = sum([self.computeBlocks(row) for row in grid]) + \
              sum([self.computeBlocks([row[i] for row in grid]) for i in range(num_cols)])
        
        return 2 * ans
    
    
    def computeBlocks(self, l1):
        last_carre = 0
        blocks = 0
        for carre in l1:
            if (carre == 1) & (last_carre == 0):
                blocks += 1
            last_carre = carre
        
        return blocks


if __name__ == "__main__":
    grid = [[0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]]
    
    print(Solution().islandPerimeter(grid))
