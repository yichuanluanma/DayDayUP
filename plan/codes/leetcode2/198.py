# coding: utf-8
"""
打家劫舍
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 动态规划
        last = now = 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now

