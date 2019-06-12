#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2 == 0:
            return (self.getkth(nums1, nums2, l // 2) + self.getkth(nums1, nums2, l // 2 - 1)) / 2.0
        else:
            return self.getkth(nums1, nums2, l // 2) * 1.0
    
    def getkth(self, nums1: List[int], nums2: List[int], k: int) -> float:
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        ia, ib = len(nums1) // 2, len(nums2) // 2
        ma, mb = nums1[ia], nums2[ib]

        # k 大于两个数组中位数下标之和时
        if ia + ib < k:
            # nums1 的中位数大于 nums2 的中位数，nums2 的前半部分不包括 k
            if ma > mb:
                return self.getkth(nums1, nums2[ib+1:], k-ib-1)
            else:
                return self.getkth(nums1[ia+1:], nums2, k-ia-1)
        # k 小于两个数组中位数下标之和时
        else:
            # nums1 的中位数大于 nums2 的中位数，nums1 的后半部分不包括 k
            if ma > mb:
                return self.getkth(nums1[:ia], nums2, k)
            else:
                return self.getkth(nums1, nums2[:ib], k)

