#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_ones = 0
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] == 1:
                cnt_ones += 1
            if nums[fast] == 0:
                nums[slow] = 0
                slow += 1
        while slow < len(nums):
            if cnt_ones > 0:
                nums[slow] = 1
                cnt_ones -= 1
            else:
                nums[slow] = 2
            slow += 1

