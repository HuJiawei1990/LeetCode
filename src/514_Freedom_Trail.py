# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       514_Freedom_Trail.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-30 15:50
@version    0.0.1.20180330
--------------------------------------
514. Freedom Trail

In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial
    called the "Freedom Trail Ring",
    and use the dial to spell a specific keyword in order to open the door.
Given a string ring, which represents the code engraved on the outer ring and another string key,
    which represents the keyword needs to be spelled. You need to find
    the minimum number of steps in order to spell all the characters in the keyword.
Initially, the first character of the ring is aligned at 12:00 direction.
    You need to spell all the characters in the string key one by one
    by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction
    and then by pressing the center button.
At the stage of rotating the ring to spell the key character key[i]:
    1. You can rotate the ring clockwise or anticlockwise one place,
        which counts as 1 step. The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
    2. If the character key[i] has been aligned at the 12:00 direction,
        you need to press the center button to spell, which also counts as 1 step.
        After the pressing, you could begin to spell the next character in the key (next stage),
        otherwise, you've finished all the spelling.
"""

import sys



class Solution(object):
    def dist(self, i, j, n):
        return min(abs(j-i), n - abs(j-i))
    
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        ans = 0
        ## current position of arrow
        n = len(ring)
        
        ## gather all charaters' positions in ring
        char_positions = {}
        for idx, char in enumerate(ring):
            if char in char_positions:
                char_positions[char].append(idx)
            else:
                char_positions[char] = [idx]

        ## 图算法 - 寻找最短路径
        last_level = {0: 0}
        for char in key:
            new_level = {}
            for pos in char_positions[char]:
                ## 计算由上一层的所有点至改层任意字母的最短路径
                new_level[pos] = min([self.dist(pos, last_pos, n) + last_level[last_pos] for last_pos in last_level]) + 1
            
            last_level = new_level
            
        return min(last_level.values())
    

if __name__ == "__main__":
    a = "iotfo"
    b = "fioot"
    print(Solution().findRotateSteps(a, b))
