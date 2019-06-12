#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        ret = ListNode((l1.val + l2.val) % 10)
        flag = 1 if l1.val + l2.val >= 10 else 0
        curr1, curr2 = l1.next, l2.next
        curr = ret
        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            val = flag + val1 + val2
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

            curr.next = ListNode(val % 10)
            curr = curr.next
            flag = 1 if val >= 10 else 0
        curr.next = ListNode(flag) if flag else None
        return ret

