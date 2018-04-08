# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       551_Student_Attendance_Record_1.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-04-04 17:33
@version    0.0.1.20180404
--------------------------------------
551. Student Attendance Record I

You are given a string representing an attendance record for a student. The record only contains the following three characters:
    'A' : Absent.
    'L' : Late.
    'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent)
    or more than two continuous 'L' (late).
You need to return whether the student could be rewarded according to his attendance record.
"""

import sys


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s is None: return False
        count_A = 0
        for idx, char in enumerate(s):
            if char == 'A':
                if count_A == 1:
                    return False
                else:
                    count_A += 1
            if (char == 'L') & (idx <= len(s) - 3):
                if s[idx:idx + 3] == 'LLL': return False
        
        return True


if __name__ == "__main__":
    pass

