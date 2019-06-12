#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
class Solution:
    def reverse(self, x: int) -> int:
        
        s = str(abs(x))[::-1]
        ret = int(s) if x >=0 else -1 * int(s)
        if ret > 2 ** 31 - 1 or ret < -2 ** 31:
            return 0
        return ret

