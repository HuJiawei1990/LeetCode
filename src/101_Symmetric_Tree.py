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
For example, this binary tree [1,2,2,3,4,4,3] is symmetric.

Note:
Bonus points if you could solve it both recursively and iteratively.
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
        return self.isMirror(root.left, root.right)
        
    
    def isMirror(self, tree1: TreeNode, tree2: TreeNode):
        if tree1 is None and tree2 is None: return True
        if tree1 is None or tree2 is None: return False
        
        if tree1.val != tree2.val: return False
        
        return (self.isMirror(tree1.left, tree2.right)) and (self.isMirror(tree1.right, tree2.left))


    def isSymmetric2(self, root):
        """
        Iterative method.
        :param root:    TreeNode
        :return:        boolean
        """
        if root is None: return True
        
        stack = [[root.left, root.right]]
        
        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]
            
            if (left is None) + (right is None) == 1:
                return False
            if left.val == right.val:
                stack.insert(0, [left.left, right.right])
                stack.insert(0, [left.right, right.left])
            else:
                return False
        return True


if __name__ == "__main__":
    #list_test = [1, 2, 2, 3, 4, 4, 3]
    list_test = [2, 3, 3, 4, 5, 5, 4, None, None, 8, 9, 9, 8]
    tree_test = list2TreeNode(list_test)
    
    #print(tree_test.toList())
    
    if Solution().isSymmetric(tree_test):
        print('true')
