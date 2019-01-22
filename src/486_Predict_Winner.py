# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       486_Predict_Winner.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-10-29 10:33
@version    0.0.1.20181029
--------------------------------------
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array
    followed by the player 2 and then player 1 and so on. Each time a player picks a number,
    that number will not be available for the next player. This continues until all the scores have been chosen.
    The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False.
Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose,
    player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
"""

from _utils import run_time

class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        (_, p1, p2) = self.BestChoice(nums)
        
        return p1 >= p2
    
    
    def BestChoice(self, nums):
        N = len(nums)
        S = sum(nums)
        
        if N == 1: return 0
        if N == 2: return (nums[0], nums[1]) if nums[0] >= nums[1] else (nums[1], nums[0])
        
        ## Player 1 decides which number to choose:
        ## if he picks first number of array:
        s2_1 = self.BestChoice(nums[1:])[0]
        s1_1 = S - s2_1
        
        ## if he picks last number of array:
        s2_2 = self.BestChoice(nums[0:-1])[0]
        s1_2 = S - s2_2
        
        return (s1_1, s2_1) if s1_1 >= s1_2 else (-1, s1_2, s2_2)


@run_time
def run():
    sol = Solution()

    array1 = [1, 5, 233, 7]
    array2 = [1163573, 4225123, 1034109, 6416120, 4401957, 408968, 8769389,
              7498770, 6003151, 2054050, 2621821, 8204739, 2586055, 6520977,
              2014732, 4750306, 4172182, 6965656, 1861876, 9549339]
    
    print(sol.PredictTheWinner(array2))


if __name__ == "__main__":
    run()
