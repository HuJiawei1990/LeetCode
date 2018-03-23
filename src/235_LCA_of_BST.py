# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       235_LCA_of_BST.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-22 17:14
@version    0.0.1.20180322
--------------------------------------
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
    “The lowest common ancestor is defined between two nodes v and w as the lowest node in T
    that has both v and w as descendants (where we allow a node to be a descendant of itself).”
"""

from _utils import TreeNode


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        Find the Lowest Common Ancestor of tree nodes p and q in root.
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        ## Suppose every val in node is unique
        if root is None: return None
        if root.equals(p) or root.equals(q): return root
        
        if self.isAncestor(root.left, p) and self.isAncestor(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        if self.isAncestor(root.right, p) and self.isAncestor(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
    
    def isAncestor(self, tree1, tree2):
        """
        Judge if tree1 is an ancestor of tree2.
        :type tree1:    TreeNone
        :type tree2:    TreeNone
        :return:        True: if tree1 is ancestor of tree2.
        """
        if tree2 is None: return True
        if tree1 is None: return False
        if tree1.getDepth() < tree2.getDepth(): return False
        
        if tree1.equals(tree2): return True
        
        return self.isAncestor(tree1.left, tree2) or self.isAncestor(tree1.right, tree2)


    @classmethod
    def lowestCommonAncestor2(self, root, p, q):
        """
        More simple and pythonic, but take care about the assumptions.
        :param root:    TreeNode
        :param p:       TreeNode
        :param q:       TreeNode
        :return:        Lowest Common Ancestor of p and q in root.
        NOTE:
            1. Assume that every node's value is unique, and the value of left
                if smaller than that of right node, if they exist.
        """
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root


if __name__ == "__main__":
    pass
