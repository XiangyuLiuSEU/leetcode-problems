#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 直接逐一合并 TLE，需要分治算法
        def merge(l1: ListNode, l2: ListNode) -> ListNode:
            out = ListNode(-1)
            p = out
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    p.next = ListNode(l2.val)
                    l2 = l2.next
                p = p.next
            p.next = l1 if l1 else l2
            return out.next

        # if len(lists) == 0:
        #     return None
        
        # return lists[0] if len(lists) == 1 else merge(lists[0], self.mergeKLists(lists[1:]))

        num = len(lists)
        interval = 1
        while interval < num:
            for i in range(0, num - interval, 2 * interval):
                lists[i] = merge(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0] if num > 0 else None

