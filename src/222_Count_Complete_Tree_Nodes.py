# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       222_Count_Complete_Tree_Nodes.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-23 11:08
@version    0.0.1.20180323
--------------------------------------
222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
    is completely filled, and all nodes in the last level are as far left as possible.
    It can have between 1 and 2h nodes inclusive at the last level h.
"""

from _utils import TreeNode


class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None: return 0
        
        if root.left is None : return 1;
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


if __name__ == "__main__":
    run()
