# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       443_String_Compression.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-07-29 13:33
@version    0.0.1.20190729
--------------------------------------
Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.

Follow up:
    Could you solve it using only O(1) extra space?

Example 1:
    Input:
        ["a","a","b","b","c","c","c"]
    Output:
        Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    Explanation:
        "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

Example 2:
    Input:
        ["a"]
    Output:
        Return 1, and the first 1 characters of the input array should be: ["a"]
    Explanation:
        Nothing is replaced.

Example 3:
    Input:
        ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    Output:
        Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
    Explanation:
        Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
        Notice each digit has it's own entry in the array.

Note:
    All characters have an ASCII value in [35, 126].
    1 <= len(chars) <= 1000.
"""


class Solution():
    def compress(self, chars: list) -> int:
        # add a end-flag for chars
        chars.append(' ')
        #
        idx, num = 0, 1
        
        while chars[idx] != ' ':
            if chars[idx] == chars[idx + 1]:
                idx += 1
                num += 1
            elif num == 1:
                idx += 1
            else:
                # replace the substring
                chars[idx - num + 1:idx + 1] = [chars[idx]] + [i for i in str(num)]
                idx = idx - num + len(str(num)) + 2
                
                num = 1
                # print(idx, chars)
        del chars[-1]
        
        # print(chars)
        return len(chars)


if __name__ == "__main__":
    sol = Solution()
    sol.compress(["a","a","b","b","c","c","c"])
