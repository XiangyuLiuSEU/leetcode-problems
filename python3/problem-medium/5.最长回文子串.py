#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 马拉车算法

        # 首先对输入字符串预处理
        T = self.preprocess(s)
        length = len(T)
        P = [0] * length

        C, R = 0, 0
        i = 1
        while i < length - 1:
            i_mirror = 2*C - i  # equals C - (i - C)
            P[i] = min(P[i_mirror], R-i) if R > i else 0

            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            
            # 如果回文字符串超过了 R，更新 R C
            if R < i + P[i]:
                C = i
                R = i + P[i]

            i += 1

        maxLength = max(P)
        centerIndex = P.index(maxLength)

        start = (centerIndex - maxLength) // 2
        stop = start + maxLength

        return s[start:stop]


    def preprocess(self, s: str) -> str:
        r = '#'.join(list(s))
        # 加上 ^ $ 防止出现下标越界问题
        return '^#' + r + '#$'

