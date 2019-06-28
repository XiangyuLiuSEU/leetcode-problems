#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 没有考虑输入列表为空的情况，官方测试用例也不包括
        
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        # nums长度为1或者整个nums为降序排列
        if i == 0:
            self.reverse(nums, 0, len(nums)-1)
            return

        prior = i - 1
        pointer = 0
        for i in range(len(nums)-1, prior, -1):
            if nums[i] > nums[prior]:
                pointer = i
                break

        # 交换prior和pointer
        nums[prior], nums[pointer] = nums[pointer], nums[prior]

        # 翻转prior之后的元素
        self.reverse(nums, prior+1, len(nums)-1)

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

