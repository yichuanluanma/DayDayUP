# coding: utf-8
"""
错误的集合
"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashs = [0] * len(nums)
        for i in range(len(nums)):
            hashs[nums[i] - 1] += 1
        return [hashs.index(2) + 1, hashs.index(0) + 1]

s = Solution()
res = s.findErrorNums([1,2,2,4])
print(res)