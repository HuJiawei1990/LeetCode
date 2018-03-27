# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       648_Replace_Words.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-27 14:46
@version    0.0.1.20180327
--------------------------------------
648. Replace Words

In English, we have a concept called root, which can be followed by some other words
    to form another longer word - let's call this word successor.
    For example, the root an, followed by other, which can form another word another.
Now, given a dictionary consisting of many roots and a sentence. You need to replace
    all the successor in the sentence with the root forming it.
    If a successor has many roots can form it, replace it with the root with the shortest length.
You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Note:
    - The input will only have lower-case letters.
    - 1 <= dict words number <= 1000
    - 1 <= sentence words number <= 1000
    - 1 <= root length <= 100
    - 1 <= sentence words length <= 1000
"""

import sys


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split(" ")
        ans = ""
        for idx, word in enumerate(words):
            root = self.find_root(dict, word)
            if root:
                words[idx] = root
        return " ".join(words)
        
        
    def find_root(self, dict, word):
        is_found = 0
        shortest = len(word)
        ans = word
        for root in dict:
            n = len(root)
            if (word[0:n] == root) & (shortest > n):
                shortest = n
                ans = root
                is_found += 1
        
        return ans if is_found else None
        
        
if __name__ == "__main__":
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    ans = Solution().replaceWords(dict, sentence)
    print(ans)
