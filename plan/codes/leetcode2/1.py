# coding=utf-8
"""
两数之和
描述：
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那 两个 整数，
并返回他们的数组下标。
"""


class Solution:
    def towSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], i]
            dic[num] = i

s = Solution()
res = s.towSum([2,7,11,5], 9)
print(res)