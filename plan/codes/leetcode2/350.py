# coding: utf-8
"""
两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。
示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        newNums = []
        for i in nums1:
            if i in nums2:
                newNums.append(i)
                nums2.remove(i)
        return newNums
        """

        inter = set(nums1) & set(nums2)
        l = []
        for i in inter:
            l += [i] * min(nums1.count(i), nums2.count(i))
        return l