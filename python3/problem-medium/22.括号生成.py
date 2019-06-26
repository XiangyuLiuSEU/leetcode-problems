#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 闭合数
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         # 回溯法
#         ans = []
#         def backtrack(s='', left=0, right=0):
#             if len(s) == 2*n:
#                 ans.append(s)
#             if left < n:
#                 backtrack(s+'(', left+1, right)
#             if right < left:
#                 backtrack(s+')', left, right+1)

#         backtrack()
#         return ans
