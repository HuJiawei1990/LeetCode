# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       662_Max_Width_of_Binary_Tree.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-27 15:30
@version    0.0.1.20180327
--------------------------------------
662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree.
    The width of a tree is the maximum width among all levels.
    The binary tree has the same structure as a full binary tree, but some nodes are None.
The width of one level is defined as the length between the end-nodes
    (the leftmost and right most non-None nodes in the level, where the None nodes
    between the end-nodes are also counted into the length calculation.
"""

import sys
from _utils import TreeNode, list2TreeNode


class Solution(object):
    def widthOfBinaryTree(self, root):
        def dfs(node, depth=0, pos=0):
            if node:
                yield depth, pos
                yield from dfs(node.left, depth + 1, pos * 2)
                yield from dfs(node.right, depth + 1, pos * 2 + 1)

        left = {}
        right = {}
        ans = 0
        for depth, pos in dfs(root):
            left[depth] = min(left.get(depth, pos), pos)
            right[depth] = max(right.get(depth, pos), pos)
            ans = max(ans, right[depth] - left[depth] + 1)

        return ans
        

if __name__ == "__main__":
    tree =list2TreeNode([1,1,1,1,1,1,1,None,None,None,1,None,None,None,None,2,2,2,2,2,2,2,None,2,None,None,2,None,2])
    print(Solution().widthOfBinaryTree(tree))
