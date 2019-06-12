#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 动态规划
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True

        for i in range(1, len(p)):
            dp[i+1][0] = dp[i-1][0] and p[i] == '*'
        
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i+1][j+1] = dp[i][j+1] or dp[i-1][j+1]
                    if p[i-1] == '.' or p[i-1] == s[j]:
                        dp[i+1][j+1] |= dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')

        return dp[-1][-1]

