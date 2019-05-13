# coding=utf-8
"""
搜索插入位置
描述：
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
假设数组中无重复元素。
"""
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # 使用二分法
        n = len(nums)
        if n ==0 or target <= nums[0]: return 0
        if target > nums[n-1]: return n
        left, right = 0, n-1
        while left < right:
            mid = (left+right)//2
            if target == nums[mid]: return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        if target > mid[left]:
            return left + 1
        else:
            return left
s = Solution()
result = s.searchInsert([1,3,5,6], 5)
print(result)