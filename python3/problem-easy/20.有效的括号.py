#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
class Solution:
    def isValid(self, s: str) -> bool:
        store  = []
        match = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for ch in s:
            if ch in match.keys():
                store.append(ch)
            else:
                if store and ch == match[store[-1]]:
                    store.pop()
                else:
                    return False
        return True if not store else False

