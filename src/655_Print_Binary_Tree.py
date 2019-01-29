# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       655_Print_Binary_Tree.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-01-28 17:08
@version    0.0.1.20190128
--------------------------------------
Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   /
  3
 /
4
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
"""

from _utils import TreeNode


class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        depth = root.getDepth()
        size = 2 ** depth - 1
        grid = [['' for j in range(size)] for i in range(depth)]
        
        # root node is placed at column number =  size / 2 at row 0
        queue = [(root, size / 2)]
        
        # layer number
        l = 0
        
        # difference between position of node,
        # for example, if a node is placed at column idx, its left and right child should be placed in
        # column idx - d and idx + d
        d = 2 ** (depth - 1)
        
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.pop(0)
                node = cur[0]
                idx = cur[1]
                grid[l][idx] = str(node.val)
                if node.left:
                    queue.append((node.left, idx - d / 2))
                if node.right:
                    queue.append((node.right, idx + d / 2))
            d /= 2
            l += 1
        
        return grid
