# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       621_Task_Scheduler.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-03-23 11:54
@version    0.0.1.20180323
--------------------------------------
621. Task Scheduler

Given a char array representing tasks CPU need to do.
    It contains capital letters A to Z where different letters represent different tasks.
    Tasks could be done without original order.
    Each task could be done in one interval.
    For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks,
    there must be at least n intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will take to finish all the given tasks.
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks_diff = {task: tasks.count(task) for task in set(tasks)}
        nb_tasks = len(tasks_diff)
        ## the max times a single task appear in tasks
        max_times = max(tasks_diff.values())
        ## compute how many tasks appear max_times times in tasks.
        nb_max = list(tasks_diff.values()).count(max_times)
        
        return max(len(tasks), (n + 1) * (max_times - 1) + nb_max)


if __name__ == "__main__":
    ans = Solution().leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2)
    print(ans)
