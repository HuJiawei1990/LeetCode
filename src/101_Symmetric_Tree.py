# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       101_Symmetric_Tree.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-20 17:48
@version    0.0.1.20180320
--------------------------------------
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
"""

import sys
from _utils import TreeNode, list2TreeNode


class Solution(object):
    def isSymmetric(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        root_reverse = root.reverse()
        return root_reverse == root
        
        
if __name__ == "__main__":
    list_test = [1, 2, 2, 3, 4, 4, 3]
    tree_test = list2TreeNode(list_test)
    
    if Solution().isSymmetric(tree_test):
        print('true')
