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
import datetime


class TreeNode(object):
    """
    Binary Tree class
    """
    
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
    
    def getDepth(self):
        if self is None: return 0
        if self.left is None and (self.right is None): return 1
        if self.left is None: return 1 + self.right.getDepth()
        if self.right is None: return 1 + self.left.getDepth()
        
        return max(self.left.getDepth(), self.right.getDepth()) + 1
    
    
    def reverse(self):
        # if self is None: return None
        ans = TreeNode(self.val)
        ans.left = self.right.reverse() if self.right is not None else None
        ans.right = self.left.reverse() if self.left is not None else None
        
        return ans
    
    def isMirror(self, tree1, tree2):
        """
        Judge two tree nodes whether they are mirror symmetric.
        :param tree1: TreeNode
        :param tree2: TreeNode
        :return: boolean    True:   tree2 is the mirror of tree1
                            False:  otherwise
        """
        if tree1 is None and tree2 is None: return True
        if tree1 is None or tree2 is None: return False
        
        if tree1.val != tree2.val: return False
        
        return (self.isMirror(tree1.left, tree2.right)) and (self.isMirror(tree1.right, tree2.left))
    
    def isSymmetric(self):
        if self is None: return True
        return self.isMirror(self.left, self.right)
    
    def equals(self, tree2):
        if tree2 is None: return False
        if self.val != tree2.val: return False
        if self.getDepth() != tree2.getDepth(): return False
        
        left_equals = self.left.equals(tree2.left) if self.left is not None else tree2.left is None
        right_equals = self.right.equals(tree2.right) if self.right is not None else tree2.right is None
        
        return left_equals and right_equals
    
    
    def toList(self):
        """
        Convert a tree node to a List[List[val]]. Every element in result is a list of
            val elements, from left to right.
        :return: List[List[val]]
        """
        # TODO: need to complete none node as None type in list
        list_left = self.left.toList() if self.left is not None else []
        list_right = self.right.toList() if self.right is not None else []
        
        if (list_left == []) + (list_right == []) == 1:
            if list_right:
                list_left = [[None for _ in sublist] for sublist in list_right]
            else:
                list_right = [[None for _ in sublist] for sublist in list_left]
        
        return [[self.val]] + combine_list(list_left, list_right)


def combine_list(l1, l2):
    """
    combine two list of lists element by element
    :param l1:  List[List]
    :param l2:  List[List]
    :return: List[List]
    """
    if not l1: return l2
    if not l2: return l1
    
    return [l1[0] + l2[0]] + combine_list(l1[1:], l2[1:])


def list2TreeNode(l1: list):
    if not l1: return None
    
    tree_struc = TreeNode(l1[0])
    nums_list = len(l1)
    depth = 1
    
    list_l = []
    list_r = []
    
    while True:
        list_l += l1[2 ** depth - 1: 3 * 2 ** (depth-1) - 1]
        list_r += l1[3 * 2 ** (depth-1) - 1: min(nums_list, 2 ** (depth + 1) - 1)]
        if nums_list < 2 ** (depth + 1): break
        else: depth += 1
    
    if (not list_l) or (list_l[0] is None):
        tree_struc.left = None
    else:
        tree_struc.left = list2TreeNode(list_l)
    
    if (not list_r) or (list_r[0] is None):
        tree_struc.right = None
    else:
        tree_struc.right = list2TreeNode(list_r)
    
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
        
        return [self.val] + self.next.toList()


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e



def run_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func()
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('Call function \"%s\": cost %s seconds' % (func.__name__, total_time))
        
        
    return int_time
