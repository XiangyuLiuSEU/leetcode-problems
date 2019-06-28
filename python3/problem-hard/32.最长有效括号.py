#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 动态规划
        # https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode/
        
        dp = [0] * len(s)
        maxLength = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2 + (0 if i < 2 else dp[i-2])
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + 2 + (0 if i - dp[i-1] < 2 else dp[i - 2 - dp[i-1]])
                maxLength = max(maxLength, dp[i])

        return maxLength

# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         # 不占用额外空间的方法
#         left_num = right_num = 0
#         maxLength = 0
#         for c in s:
#             if c == '(':
#                 left_num += 1
#             if c == ')':
#                 right_num += 1
            
#             if left_num == right_num:
#                 maxLength = max(maxLength, left_num + right_num)
            
#             if right_num > left_num:
#                 left_num = right_num = 0
        
#         left_num = right_num = 0

#         for c in s[::-1]:
#             if c == ')':
#                 left_num += 1
#             if c == '(':
#                 right_num += 1
            
#             if left_num == right_num:
#                 maxLength = max(maxLength, left_num + right_num)
            
#             if right_num > left_num:
#                 left_num = right_num = 0

#         return maxLength

# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         # 栈
#         maxLength = 0
#         store = [-1]
#         for i, c in enumerate(s):
#             if c == '(':
#                 store.append(i)
#             else:
#                 store.pop()

#                 if len(store) == 0:
#                     store.append(i)

#                 maxLength = max(maxLength, i - store[-1])
        
#         return maxLength
        
