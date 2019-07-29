# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       872_Leaf-Similar_Trees.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-06-02 14:46
@version    0.0.1.20190602
--------------------------------------
Consider all the leaves of a binary tree.  From left to right order,
    the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:
Both of the given trees will have between 1 and 100 nodes.
"""

from _utils import TreeNode


def run():
    pass


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leaf_seq(root1) == self.leaf_seq(root2)
    
    
    def leaf_seq(self, root:TreeNode) -> list:
        if (root.left is None) & (root.right is None):
            return [root.val]
        elif root.left is None:
            return self.leaf_seq(root.right)
        elif root.right is None:
            return self.leaf_seq(root.left)
        else:
            return self.leaf_seq(root.left) + self.leaf_seq(root.right)
        

