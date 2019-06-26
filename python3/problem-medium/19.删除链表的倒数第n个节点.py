#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 双指针
        res = ListNode(-1)
        res.next = head  # 给链表加头部

        fast = slow = res 
        distance = 0
        while fast:
            fast = fast.next
            if distance < n + 1:
                distance += 1
            else:
                slow = slow.next
        slow.next = slow.next.next
        return res.next

