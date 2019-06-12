#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        ret = 0
        while end <= len(s):
            substr = s[start:end]
            sublen = len(substr)
            
            if sublen == len(set(substr)):
                end += 1
                if sublen > ret:
                    ret = sublen
            else:
                start += 1
        return ret

