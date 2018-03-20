# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       103_Zigzag_binary_tree.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-20 09:48
@version    0.0.1.20180320
--------------------------------------
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values.
    (ie, from left to right, then right to left for the next level and alternate between).
"""

from _utils import TreeNode, list2TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        """
        Return the zigzag level order traversal of a binary tree's nodes' values.
        :param root: TreeNode           a binary tree
        :return: List[List[int]]        the zigzag level order of root
        """
        return self.zigzagLevelOrder2(root, True)
    
    
    def zigzagLevelOrder2(self, root: TreeNode, from_left=True):
        """
        
        :param root:
        :param from_left:
        :return:
        """
        if root is None: return []
        
        tree_l, tree_r = root.left, root.right
        
        return [[root.val]] + self.combine_list(self.zigzagLevelOrder2(tree_l, not from_left),
                                                self.zigzagLevelOrder2(tree_r, not from_left),
                                                not from_left)


    def combine_list(self, l1, l2, from_left=True):
        if not l1: return l2
        if not l2: return l1
        
        if from_left:
            return [l1[0] + l2[0]] + self.combine_list(l1[1:], l2[1:], not from_left)
        else:
            return [l2[0] + l1[0]] + self.combine_list(l1[1:], l2[1:], not from_left)

        
if __name__ == "__main__":
    #tree_list = [3, 9, 20, None, None, 15, 7]
    tree_list = [1, 2]
    
    tree_node = list2TreeNode(tree_list)
    
    tree_zigzag = Solution().zigzagLevelOrder(tree_node)
    
    print(tree_zigzag)
    