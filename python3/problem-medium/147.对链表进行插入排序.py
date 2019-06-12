#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        p = dummy = ListNode(0)
        curr = dummy.next = head

        while curr and curr.next:
            val = curr.next.val
            if val >= curr.val:
                curr = curr.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            
            new = curr.next
            curr.next = new.next
            new.next = p.next
            p.next = new
        
        return dummy.next

