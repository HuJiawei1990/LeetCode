# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       637_Average_of_Levels_in_Binary_Tree.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-01-25 15:16
@version    0.0.1.20190125
--------------------------------------
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
        3
       / \
      9  20
        /  \
       15   7
Output: [3, 14.5, 11]
Explanation:
    The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
    The range of node's value is in the range of 32-bit signed integer.
"""

import sys
from _utils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None: return []
        
        sum_root = self.SumofLevel(root)
        
        return [i[0]/i[1] for i in sum_root]
    
    def SumofLevel(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None: return []
        sum_l = self.SumofLevel(root.left)
        sum_r = self.SumofLevel(root.right)
        
        sum_root = [(root.val, 1)]
        for i in range(max(len(sum_l), len(sum_r))):
            if i >= len(sum_l):
                sum_root.append(sum_r[i])
            elif i >= len(sum_r):
                sum_root.append(sum_l[i])
            else:
                sum_root.append((sum_r[i][0]+sum_l[i][0], sum_r[i][1]+sum_l[i][1]))
        return sum_root



