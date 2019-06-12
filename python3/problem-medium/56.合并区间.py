#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        # bubble sort TLE
        # for i in range(len(intervals)):
        #     for j in list(range(i+1, len(intervals)))[::-1]:
        #         if intervals[j][0] < intervals[j-1][0]:
        #             tmp = intervals[j]
        #             intervals[j] = intervals[j-1]
        #             intervals[j-1] = tmp
        intervals = sorted(intervals, key=lambda x: x[0])
        
        res = []
        for i in intervals:
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        
        return res


