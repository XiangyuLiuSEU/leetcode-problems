#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        tmp = intervals + [newInterval]
        res = []
        for i in sorted(tmp, key=lambda x: x[0]):
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        
        return res

