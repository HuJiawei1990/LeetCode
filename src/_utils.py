# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       _utils.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-20 10:11
@version    0.0.1.20180320
--------------------------------------
<enter description here>
"""

import sys


class TreeNode(object):
    """
    Binary Tree class
    """
    def __init__(self, x=None):
        if x is None:
            self = None
        else:
            self.val = x
            self.left = None
            self.right = None
        
        
    def reverse(self):
        if self is None: return None
        ans = TreeNode(self.val)
        ans.left = self.right.reverse() if self.right is not None else None
        ans.right = self.left.reverse() if self.left is not None else None
        
        return ans
    


def list2TreeNode(l1: list):
    if not l1: return None
    
    tree_struc = TreeNode(l1[0])
    list_l = l1[1::2]
    list_r = l1[2::2]
    
    if (not list_l) or (list_l[0] is None): tree_struc.left = None
    else: tree_struc.left = list2TreeNode(list_l)
    
    if (not list_r) or (list_r[0] is None): tree_struc.right = None
    else: tree_struc.right = list2TreeNode(list_r)
    
    return tree_struc


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def add_first(self, x):
        self.next = self
        self.val = x
    
    def toList(self):
        if self is None:
            return []
        
        if self.next is None:
            return [self.val]
        
        return [self.val] + self.next.toList