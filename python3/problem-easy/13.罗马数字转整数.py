#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
class Solution:
    def romanToInt(self, s: str) -> int:
        if s == '':
            return 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, \
            'D': 500, 'M': 1000}
        ret = dic[s[0]]
        for i in range(1, len(s)):
            if dic[s[i]] > dic[s[i-1]]:
                ret = ret - dic[s[i-1]] * 2 + dic[s[i]]
            else:
                ret += dic[s[i]]
        return ret


