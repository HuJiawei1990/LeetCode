# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       086_Partition_List.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-19 17:29
@version    0.0.1.20180319
--------------------------------------
Given a linked list and a val x, partition it
    such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

import sys
from _utils import ListNode

## TODO: not completed


class Solution:
    def split(self, head: ListNode, x):
        if head is None:
            return None, None
        
        if head.next is None:
            if head.val < x: return head, None
            else: return None, head
            
        aux1, aux2 = self.split(head.next, x)
        if head.val < x:
            return aux1.add_first(head.val), aux2
        else:
            return aux1, aux2.add_first(head.val)
     
            
    def partition(self, head: ListNode, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None: return head
        
        aux1, aux2 = self.split(head, x)
        return aux1.toList() + aux2.toList()
        
        
if __name__ == "__main__":
    if not None:
        print(0)
    else:
        print(1)
        
